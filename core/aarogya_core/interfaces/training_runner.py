"""Training runner interface."""

from __future__ import annotations

from typing import Any, Protocol, runtime_checkable

from aarogya_core.types.ids import ExperimentId


@runtime_checkable
class TrainingRunner(Protocol):
    """Run a training job from config."""

    def train(
        self, config: dict[str, Any], experiment_id: ExperimentId
    ) -> dict[str, Any]: ...
