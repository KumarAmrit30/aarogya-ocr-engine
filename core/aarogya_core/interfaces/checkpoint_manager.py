"""Checkpoint manager interface."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Protocol, runtime_checkable

from aarogya_core.types.ids import ModelId


@runtime_checkable
class CheckpointManager(Protocol):
    """Save and load model checkpoints."""

    def save(self, model_id: ModelId, obj: Any, path: Path) -> Path:
        ...

    def load(self, path: Path) -> Any:
        ...
