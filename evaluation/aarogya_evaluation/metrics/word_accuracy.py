"""Word-level exact-match accuracy."""

from __future__ import annotations

from aarogya_core.types.evaluation import GroundTruth, MetricResult, Prediction
from aarogya_evaluation.metrics.base import BaseMetric, tokenize_words
from aarogya_evaluation.metrics.registry import register_metric
from aarogya_evaluation.normalization.base import NormalizationMode


@register_metric
class WordAccuracy(BaseMetric):
    name = "word_accuracy"
    required_normalization = NormalizationMode.STANDARD.value

    def evaluate(
        self, ground_truth: GroundTruth, prediction: Prediction
    ) -> MetricResult:
        ref = ground_truth.words or tokenize_words(ground_truth.text)
        hyp = prediction.words or tokenize_words(prediction.text)
        if not ref and not hyp:
            return self._result(
                1.0, sample_id=ground_truth.sample_id, extras={"matched": 0, "total": 0}
            )
        total = max(len(ref), 1)
        matched = sum(1 for i, r in enumerate(ref) if i < len(hyp) and hyp[i] == r)
        return self._result(
            matched / total,
            sample_id=ground_truth.sample_id,
            extras={"matched": matched, "total": total},
        )
