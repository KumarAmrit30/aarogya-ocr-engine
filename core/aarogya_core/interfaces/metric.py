"""Pluggable metric Protocol — implementations live under evaluation/."""

from __future__ import annotations

from typing import Protocol, runtime_checkable

from aarogya_core.types.evaluation import GroundTruth, MetricResult, Prediction


@runtime_checkable
class Metric(Protocol):
    """Single evaluation metric. Must not know about engines."""

    name: str
    required_normalization: str
    implemented: bool

    def evaluate(
        self, ground_truth: GroundTruth, prediction: Prediction
    ) -> MetricResult:
        """Score one sample pair."""
        ...
