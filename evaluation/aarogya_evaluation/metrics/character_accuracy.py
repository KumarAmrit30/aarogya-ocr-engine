"""Character accuracy = 1 - CER (clipped to [0, 1])."""

from __future__ import annotations

from aarogya_core.types.evaluation import GroundTruth, MetricResult, Prediction
from aarogya_evaluation.metrics.base import BaseMetric
from aarogya_evaluation.metrics.cer import CharacterErrorRate
from aarogya_evaluation.metrics.registry import register_metric
from aarogya_evaluation.normalization.base import NormalizationMode


@register_metric
class CharacterAccuracy(BaseMetric):
    name = "character_accuracy"
    required_normalization = NormalizationMode.RAW.value

    def evaluate(
        self, ground_truth: GroundTruth, prediction: Prediction
    ) -> MetricResult:
        cer = CharacterErrorRate().evaluate(ground_truth, prediction)
        assert cer.value is not None
        value = max(0.0, min(1.0, 1.0 - cer.value))
        return self._result(
            value, sample_id=ground_truth.sample_id, extras={"cer": cer.value}
        )
