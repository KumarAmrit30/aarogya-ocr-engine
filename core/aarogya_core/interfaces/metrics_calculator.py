"""Metrics calculator interface."""

from __future__ import annotations

from typing import Any, Protocol, runtime_checkable

from aarogya_core.types.metrics import Metrics


@runtime_checkable
class MetricsCalculator(Protocol):
    """Compute named metrics from predictions and references."""

    def calculate(self, predictions: Any, references: Any) -> Metrics:
        ...
