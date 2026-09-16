"""Exact string match accuracy (1.0 or 0.0)."""

from __future__ import annotations

from aarogya_core.types.evaluation import GroundTruth, MetricResult, Prediction
from aarogya_evaluation.metrics.base import BaseMetric
from aarogya_evaluation.metrics.registry import register_metric
from aarogya_evaluation.normalization.base import NormalizationMode


@register_metric
class ExactMatch(BaseMetric):
    name = "exact_match"
    required_normalization = NormalizationMode.RAW.value

    def evaluate(
        self, ground_truth: GroundTruth, prediction: Prediction
    ) -> MetricResult:
        value = 1.0 if ground_truth.text == prediction.text else 0.0
        return self._result(value, sample_id=ground_truth.sample_id)
