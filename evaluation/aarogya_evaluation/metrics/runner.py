"""Run selected metrics on one sample or a batch (after normalization)."""

from __future__ import annotations

from aarogya_core.types.evaluation import GroundTruth, MetricResult, Prediction
from aarogya_evaluation.metrics.collection import MetricCollection
from aarogya_evaluation.metrics.factory import create_metrics
from aarogya_evaluation.normalization.base import normalize_text


def _apply_norm(
    gt: GroundTruth, pred: Prediction, mode: str
) -> tuple[GroundTruth, Prediction]:
    gt_n = gt.model_copy(
        update={
            "text": normalize_text(gt.text, mode),
            "lines": [normalize_text(x, mode) for x in gt.lines],
            "words": [normalize_text(x, mode) for x in gt.words],
        }
    )
    pred_n = pred.model_copy(
        update={
            "text": normalize_text(pred.text, mode),
            "lines": [normalize_text(x, mode) for x in pred.lines],
            "words": [normalize_text(x, mode) for x in pred.words],
        }
    )
    return gt_n, pred_n


class MetricRunner:
    """Runs a MetricCollection with per-metric normalization."""

    def __init__(
        self, metrics: MetricCollection | None = None, names: list[str] | None = None
    ) -> None:
        self.collection = metrics if metrics is not None else create_metrics(names)

    def run_sample(
        self,
        ground_truth: GroundTruth,
        prediction: Prediction,
        *,
        normalization_override: str | None = None,
    ) -> list[MetricResult]:
        results: list[MetricResult] = []
        for metric in self.collection:
            mode = normalization_override or metric.required_normalization
            gt_n, pred_n = _apply_norm(ground_truth, prediction, mode)
            result = metric.evaluate(gt_n, pred_n)
            # Ensure normalization field reflects what was applied
            result = result.model_copy(
                update={"normalization": mode, "sample_id": ground_truth.sample_id}
            )
            results.append(result)
        return results
