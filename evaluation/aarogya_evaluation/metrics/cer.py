"""Character Error Rate."""

from __future__ import annotations

from aarogya_core.types.evaluation import GroundTruth, MetricResult, Prediction
from aarogya_evaluation.metrics.base import BaseMetric, levenshtein
from aarogya_evaluation.metrics.registry import register_metric
from aarogya_evaluation.normalization.base import NormalizationMode


@register_metric
class CharacterErrorRate(BaseMetric):
    """CER = edit_distance(ref, hyp) / max(len(ref), 1). Empty-empty => 0."""

    name = "cer"
    required_normalization = NormalizationMode.RAW.value

    def evaluate(
        self, ground_truth: GroundTruth, prediction: Prediction
    ) -> MetricResult:
        ref = ground_truth.text
        hyp = prediction.text
        if ref == "" and hyp == "":
            value = 0.0
            dist = 0
        else:
            dist = levenshtein(ref, hyp)
            denom = max(len(ref), 1)
            value = dist / denom
        return self._result(
            value,
            sample_id=ground_truth.sample_id,
            extras={"edit_distance": dist, "ref_len": len(ref), "hyp_len": len(hyp)},
        )
