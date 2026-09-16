"""WER after STANDARD normalization."""

from __future__ import annotations

from aarogya_core.types.evaluation import GroundTruth, MetricResult, Prediction
from aarogya_evaluation.metrics.base import BaseMetric
from aarogya_evaluation.metrics.registry import register_metric
from aarogya_evaluation.metrics.wer import WordErrorRate
from aarogya_evaluation.normalization.base import NormalizationMode


@register_metric
class NormalizedWER(BaseMetric):
    name = "normalized_wer"
    required_normalization = NormalizationMode.STANDARD.value

    def evaluate(
        self, ground_truth: GroundTruth, prediction: Prediction
    ) -> MetricResult:
        inner = WordErrorRate().evaluate(ground_truth, prediction)
        return self._result(
            inner.value, sample_id=ground_truth.sample_id, extras=inner.extras
        )
