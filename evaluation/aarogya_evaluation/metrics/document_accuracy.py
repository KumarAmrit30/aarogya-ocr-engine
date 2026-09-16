"""Document accuracy: exact match of full document text."""

from __future__ import annotations

from aarogya_core.types.evaluation import GroundTruth, MetricResult, Prediction
from aarogya_evaluation.metrics.base import BaseMetric
from aarogya_evaluation.metrics.registry import register_metric
from aarogya_evaluation.normalization.base import NormalizationMode


@register_metric
class DocumentAccuracy(BaseMetric):
    name = "document_accuracy"
    required_normalization = NormalizationMode.STANDARD.value

    def evaluate(
        self, ground_truth: GroundTruth, prediction: Prediction
    ) -> MetricResult:
        ref = ground_truth.text
        hyp = prediction.text
        value = 1.0 if ref == hyp else 0.0
        return self._result(value, sample_id=ground_truth.sample_id)
