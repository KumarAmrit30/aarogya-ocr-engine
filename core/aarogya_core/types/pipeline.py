"""Pipeline registry types — composable adapter graphs."""

from typing import Any

from pydantic import BaseModel, Field

from aarogya_core.types.common import SchemaVersionMixin
from aarogya_core.types.ids import AssetId, PipelineId


class PipelineStep(BaseModel):
    """One step in a registered pipeline (opaque engine/component refs)."""

    role: str = Field(
        ..., description="e.g. detector, recognizer, layout, medical_parser"
    )
    engine_id: str = Field(
        ..., description="Opaque engine system id, e.g. paddle, qwen"
    )
    config_ref: str | None = None
    asset_ids: list[AssetId] = Field(default_factory=list)
    extras: dict[str, Any] = Field(default_factory=dict)


class PipelineRecord(SchemaVersionMixin):
    """Entry under registry/pipelines/PIPELINE-#####.yaml."""

    pipeline_id: PipelineId
    name: str
    description: str | None = None
    steps: list[PipelineStep] = Field(default_factory=list)
    asset_ids: list[AssetId] = Field(default_factory=list)
    extras: dict[str, Any] = Field(default_factory=dict)
