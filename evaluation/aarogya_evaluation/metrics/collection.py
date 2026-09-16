"""Ordered collection of metrics."""

from __future__ import annotations

from collections.abc import Iterator, Sequence

from aarogya_core.types.evaluation import GroundTruth, MetricResult, Prediction
from aarogya_evaluation.metrics.base import BaseMetric


class MetricCollection:
    def __init__(self, metrics: Sequence[BaseMetric]) -> None:
        self._metrics = list(metrics)

    def __iter__(self) -> Iterator[BaseMetric]:
        return iter(self._metrics)

    def __len__(self) -> int:
        return len(self._metrics)

    @property
    def names(self) -> list[str]:
        return [m.name for m in self._metrics]

    def evaluate_sample(
        self, ground_truth: GroundTruth, prediction: Prediction
    ) -> list[MetricResult]:
        return [m.evaluate(ground_truth, prediction) for m in self._metrics]
