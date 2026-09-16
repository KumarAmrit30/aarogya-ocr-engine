"""Experiment record types — immutable once written."""

from datetime import datetime
from typing import Any, Literal

from pydantic import BaseModel, Field

from aarogya_core.types.common import SchemaVersionMixin
from aarogya_core.types.ids import DatasetId, ExperimentId, ModelId, PipelineId


class ConfigRef(BaseModel):
    """Reference to a config file under configs/."""

    path: str
    hash: str | None = None


class ExperimentArtifactLayout(BaseModel):
    """Frozen on-disk layout under registry/experiments/EXP-#####/."""

    root: str
    config_dir: str = "config"
    results_dir: str = "results"
    report_dir: str = "report"
    artifacts_dir: str = "artifacts"


class Experiment(SchemaVersionMixin):
    """
    Tracked experiment metadata (registry record).

    Experiments are immutable after creation. Reruns allocate a new EXP-#####.
    """

    experiment_id: ExperimentId
    name: str
    status: Literal["planned", "running", "completed", "failed", "abandoned"] = (
        "planned"
    )
    hypothesis: str | None = None
    pipeline_id: PipelineId | None = None
    engine_id: str | None = None
    model_id: ModelId | None = None
    dataset_ids: list[DatasetId] = Field(default_factory=list)
    dataset_version: str | None = Field(
        default=None,
        description="Dataset version label used for this run, e.g. v3",
    )
    config: ConfigRef | None = None
    metrics: dict[str, float] = Field(default_factory=dict)
    artifact_path: str | None = None
    notes_path: str | None = None
    immutable: Literal[True] = True
    supersedes: ExperimentId | None = Field(
        default=None,
        description="Prior experiment this run replaces (never mutates the prior)",
    )
    forked_from: ExperimentId | None = None
    artifact_layout: ExperimentArtifactLayout | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None
    extras: dict[str, Any] = Field(default_factory=dict)
