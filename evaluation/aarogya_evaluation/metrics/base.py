"""Base metric helpers implementing the Metric Protocol."""

from __future__ import annotations

from abc import ABC, abstractmethod

from aarogya_core.types.evaluation import GroundTruth, MetricResult, Prediction
from aarogya_evaluation.normalization.base import NormalizationMode


class BaseMetric(ABC):
    """Abstract metric with registration-friendly attributes."""

    name: str = "unnamed"
    required_normalization: str = NormalizationMode.RAW.value
    implemented: bool = True

    @abstractmethod
    def evaluate(
        self, ground_truth: GroundTruth, prediction: Prediction
    ) -> MetricResult: ...

    def _result(
        self,
        value: float | None,
        *,
        sample_id: str | None = None,
        extras: dict | None = None,
        message: str | None = None,
        implemented: bool | None = None,
    ) -> MetricResult:
        return MetricResult(
            name=self.name,
            value=value,
            implemented=self.implemented if implemented is None else implemented,
            normalization=self.required_normalization,
            sample_id=sample_id,
            extras=extras or {},
            message=message,
        )


def levenshtein(a: str, b: str) -> int:
    """Classic Levenshtein edit distance."""
    if a == b:
        return 0
    if not a:
        return len(b)
    if not b:
        return len(a)
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, start=1):
        curr = [i]
        for j, cb in enumerate(b, start=1):
            ins = curr[j - 1] + 1
            delete = prev[j] + 1
            sub = prev[j - 1] + (ca != cb)
            curr.append(min(ins, delete, sub))
        prev = curr
    return prev[-1]


def tokenize_words(text: str) -> list[str]:
    return [t for t in text.split() if t]
