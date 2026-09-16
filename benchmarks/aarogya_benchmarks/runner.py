"""Benchmark runner — pipelines × dataset versions (no engines)."""

from __future__ import annotations

from typing import Any
from uuid import uuid4

from aarogya_benchmarks.comparison import compare_suite_by_pipeline
from aarogya_benchmarks.config import BenchmarkConfig
from aarogya_benchmarks.leaderboard import build_leaderboard
from aarogya_core.types.evaluation import (
    BenchmarkRun,
    BenchmarkSuite,
    EvaluationConfig,
    GroundTruth,
    Prediction,
)
from aarogya_core.types.metrics import Metrics
from aarogya_evaluation.engine.evaluator import EvaluationEngine


class PipelineBenchmarkRunner:
    """
    Compare multiple pipelines on one dataset version using precomputed predictions.

    Future: parallel execution hook (sequential for now).
    """

    suite: str = "handwritten"

    def __init__(self, suite: str | None = None) -> None:
        if suite:
            self.suite = suite
        self._engine = EvaluationEngine()

    def run(self, config: dict[str, Any] | BenchmarkConfig) -> BenchmarkSuite:
        cfg = (
            config
            if isinstance(config, BenchmarkConfig)
            else BenchmarkConfig.model_validate(config)
        )
        self.suite = cfg.suite
        refs = [GroundTruth.model_validate(r) for r in cfg.references]
        runs: list[BenchmarkRun] = []

        for pset in cfg.pipeline_sets:
            preds = [
                Prediction.model_validate(
                    {**p, "pipeline_id": p.get("pipeline_id", pset.pipeline_id)}
                )
                for p in pset.predictions
            ]
            eval_config = EvaluationConfig(
                metrics=cfg.metrics,
                primary_metric=cfg.primary_metric,
                dataset_id=cfg.dataset_id,
                dataset_version=cfg.dataset_version,
                pipeline_id=pset.pipeline_id,
                collect_failures=True,
            )
            report = self._engine.evaluate(preds, refs, eval_config, return_report=True)
            assert not isinstance(report, Metrics)
            run = BenchmarkRun(
                run_id=f"brun-{uuid4().hex[:10]}",
                pipeline_id=pset.pipeline_id,
                dataset_id=cfg.dataset_id,
                dataset_version=cfg.dataset_version,
                summary=report.summary,
                report_id=report.report_id,
                status="completed",
            )
            runs.append(run)

        leaderboard = build_leaderboard(
            runs, primary_metric=cfg.primary_metric, lower_is_better=cfg.lower_is_better
        )
        suite = BenchmarkSuite(
            suite=cfg.suite,
            runs=runs,
            leaderboard=leaderboard,
            metadata={
                "dataset_id": cfg.dataset_id,
                "dataset_version": cfg.dataset_version,
            },
        )
        suite.comparison = compare_suite_by_pipeline(suite, metric=cfg.primary_metric)
        return suite


# Backward-compatible name used by Protocol examples
BenchmarkRunnerImpl = PipelineBenchmarkRunner
