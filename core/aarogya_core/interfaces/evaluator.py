"""Single-run evaluator interface."""

from __future__ import annotations

from typing import Any, Protocol, runtime_checkable

from aarogya_core.types.metrics import Metrics


@runtime_checkable
class Evaluator(Protocol):
    """Evaluate predictions against ground truth for one run."""

    def evaluate(self, predictions: Any, references: Any) -> Metrics:
        ...
