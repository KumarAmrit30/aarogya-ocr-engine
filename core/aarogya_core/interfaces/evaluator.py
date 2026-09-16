"""Single-run evaluator interface."""

from __future__ import annotations

from collections.abc import Sequence
from typing import Protocol, runtime_checkable

from aarogya_core.types.evaluation import (
    EvaluationConfig,
    EvaluationReport,
    GroundTruth,
    Prediction,
)
from aarogya_core.types.metrics import Metrics


@runtime_checkable
class Evaluator(Protocol):
    """
    Evaluate predictions against ground truth for one run.

    Implementations must remain model-agnostic (GT/Prediction only).
    """

    def evaluate(
        self,
        predictions: Sequence[Prediction] | Sequence[object],
        references: Sequence[GroundTruth] | Sequence[object],
        config: EvaluationConfig | None = None,
    ) -> Metrics | EvaluationReport: ...
