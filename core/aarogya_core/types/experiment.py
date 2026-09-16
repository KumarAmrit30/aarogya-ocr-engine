"""Experiment record types."""

from datetime import datetime
from typing import Any, Literal

from pydantic import BaseModel, Field

from aarogya_core.types.common import SchemaVersionMixin
from aarogya_core.types.ids import DatasetId, ExperimentId, ModelId


class ConfigRef(BaseModel):
    """Reference to a config file under configs/."""

    path: str
    hash: str | None = None


class Experiment(SchemaVersionMixin):
    """Tracked experiment metadata (registry record)."""

    experiment_id: ExperimentId
    name: str
    status: Literal["planned", "running", "completed", "failed", "abandoned"] = "planned"
    hypothesis: str | None = None
    engine_id: str | None = None
    model_id: ModelId | None = None
    dataset_ids: list[DatasetId] = Field(default_factory=list)
    config: ConfigRef | None = None
    metrics: dict[str, float] = Field(default_factory=dict)
    artifact_path: str | None = None
    notes_path: str | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None
    extras: dict[str, Any] = Field(default_factory=dict)
