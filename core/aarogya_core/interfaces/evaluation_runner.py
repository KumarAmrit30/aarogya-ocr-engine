"""Evaluation runner interface."""

from __future__ import annotations

from typing import Any, Protocol, runtime_checkable

from aarogya_core.types.ids import ExperimentId
from aarogya_core.types.metrics import Metrics


@runtime_checkable
class EvaluationRunner(Protocol):
    """Run evaluation for a model/dataset pair."""

    def run(self, config: dict[str, Any], experiment_id: ExperimentId) -> Metrics: ...
