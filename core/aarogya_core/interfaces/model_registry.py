"""Model registry interface."""

from __future__ import annotations

from typing import Protocol, runtime_checkable

from aarogya_core.types.ids import ModelId
from aarogya_core.types.model import ModelRecord


@runtime_checkable
class ModelRegistry(Protocol):
    """Register and look up model records."""

    def get(self, model_id: ModelId) -> ModelRecord: ...

    def list(self) -> list[ModelRecord]: ...

    def register(self, record: ModelRecord) -> ModelRecord: ...
