"""Placeholder metric: Medicine Accuracy."""

from __future__ import annotations

from aarogya_core.types.evaluation import GroundTruth, MetricResult, Prediction
from aarogya_evaluation.metrics.base import BaseMetric
from aarogya_evaluation.metrics.registry import register_metric
from aarogya_evaluation.normalization.base import NormalizationMode


@register_metric
class MedicineAccuracy(BaseMetric):
    name = "medicine_accuracy"
    required_normalization = NormalizationMode.RAW.value
    implemented = False

    def evaluate(
        self, ground_truth: GroundTruth, prediction: Prediction
    ) -> MetricResult:
        return self._result(
            None,
            sample_id=ground_truth.sample_id,
            implemented=False,
            message="Medicine Accuracy is not implemented yet",
        )
