"""Model-agnostic EvaluationEngine."""

from __future__ import annotations

import threading
import time
from collections.abc import Callable, Sequence
from pathlib import Path

from aarogya_core.types.evaluation import (
    EvaluationConfig,
    EvaluationReport,
    EvaluationSummary,
    GroundTruth,
    Prediction,
    SampleEvaluation,
)
from aarogya_core.types.metrics import Metrics
from aarogya_evaluation.failure.collector import ErrorCollector
from aarogya_evaluation.metrics.runner import MetricRunner
from aarogya_evaluation.report.builder import ReportBuilder
from aarogya_evaluation.report.exporters import export_report

ProgressCallback = Callable[[int, int], None]


class EvaluationEngine:
    """
    Discover metrics dynamically, normalize, evaluate, aggregate, report.

    Does not know which engines exist.
    """

    def evaluate(
        self,
        predictions: Sequence[Prediction] | Sequence[object],
        references: Sequence[GroundTruth] | Sequence[object],
        config: EvaluationConfig | None = None,
        *,
        progress: ProgressCallback | None = None,
        cancel_event: threading.Event | None = None,
        return_report: bool = True,
    ) -> Metrics | EvaluationReport:
        config = config or EvaluationConfig()
        preds = [
            p if isinstance(p, Prediction) else Prediction.model_validate(p)
            for p in predictions
        ]
        refs = [
            r if isinstance(r, GroundTruth) else GroundTruth.model_validate(r)
            for r in references
        ]
        if len(preds) != len(refs):
            raise ValueError(f"predictions ({len(preds)}) != references ({len(refs)})")

        # Align by sample_id when possible
        ref_by_id = {r.sample_id: r for r in refs}
        pairs: list[tuple[GroundTruth, Prediction]] = []
        for pred in preds:
            if pred.sample_id in ref_by_id:
                pairs.append((ref_by_id[pred.sample_id], pred))
            else:
                raise ValueError(f"No ground truth for sample_id={pred.sample_id}")

        runner = MetricRunner(names=config.metrics)
        collector = ErrorCollector() if config.collect_failures else None
        samples: list[SampleEvaluation] = []
        metric_sums: dict[str, float] = {}
        metric_counts: dict[str, int] = {}

        started = time.perf_counter()
        total = len(pairs)
        for i, (gt, pred) in enumerate(pairs):
            if cancel_event is not None and cancel_event.is_set():
                break
            results = runner.run_sample(
                gt, pred, normalization_override=config.normalization
            )
            failure = collector.consider(gt, pred) if collector else None
            samples.append(
                SampleEvaluation(
                    sample_id=gt.sample_id, results=results, failure=failure
                )
            )
            for result in results:
                if result.implemented and result.value is not None:
                    metric_sums[result.name] = (
                        metric_sums.get(result.name, 0.0) + result.value
                    )
                    metric_counts[result.name] = metric_counts.get(result.name, 0) + 1
            if progress is not None:
                progress(i + 1, total)

        duration = time.perf_counter() - started
        averages = {
            name: metric_sums[name] / metric_counts[name]
            for name in metric_sums
            if metric_counts.get(name)
        }
        summary = EvaluationSummary(
            metrics=averages,
            sample_count=len(samples),
            duration_seconds=duration,
            primary_metric=config.primary_metric,
            extras={"failure_counts": collector.summary() if collector else {}},
        )
        timing = {"total_seconds": duration}
        report = ReportBuilder().build(
            config=config,
            summary=summary,
            samples=samples,
            failures=collector.cases if collector else [],
            timing=timing,
        )
        if config.report_dir:
            export_report(report, Path(config.report_dir))
        if return_report:
            return report
        return summary.to_metrics()
