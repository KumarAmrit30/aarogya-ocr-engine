"""Word Error Rate."""

from __future__ import annotations

from aarogya_core.types.evaluation import GroundTruth, MetricResult, Prediction
from aarogya_evaluation.metrics.base import BaseMetric, tokenize_words
from aarogya_evaluation.metrics.registry import register_metric
from aarogya_evaluation.normalization.base import NormalizationMode


@register_metric
class WordErrorRate(BaseMetric):
    """WER = word-level edit distance / max(len(ref_words), 1)."""

    name = "wer"
    required_normalization = NormalizationMode.RAW.value

    def evaluate(
        self, ground_truth: GroundTruth, prediction: Prediction
    ) -> MetricResult:
        ref_w = tokenize_words(ground_truth.text)
        hyp_w = tokenize_words(prediction.text)
        if not ref_w and not hyp_w:
            value = 0.0
            dist = 0
        else:
            # Levenshtein on token sequences via joined sentinel-free indices
            dist = _token_edit(ref_w, hyp_w)
            value = dist / max(len(ref_w), 1)
        return self._result(
            value,
            sample_id=ground_truth.sample_id,
            extras={
                "edit_distance": dist,
                "ref_words": len(ref_w),
                "hyp_words": len(hyp_w),
            },
        )


def _token_edit(ref: list[str], hyp: list[str]) -> int:
    if ref == hyp:
        return 0
    # Map tokens to single chars via index table for levenshtein on sequences
    # Use dynamic programming directly on lists
    n, m = len(ref), len(hyp)
    if n == 0:
        return m
    if m == 0:
        return n
    prev = list(range(m + 1))
    for i in range(1, n + 1):
        curr = [i]
        for j in range(1, m + 1):
            cost = 0 if ref[i - 1] == hyp[j - 1] else 1
            curr.append(min(curr[j - 1] + 1, prev[j] + 1, prev[j - 1] + cost))
        prev = curr
    return prev[m]
