"""Model registry record types."""

from typing import Any, Literal

from pydantic import Field

from aarogya_core.types.common import SchemaVersionMixin
from aarogya_core.types.ids import ExperimentId, ModelId


class ModelRecord(SchemaVersionMixin):
    """Registered trained or external model checkpoint."""

    model_id: ModelId
    name: str
    engine_id: str
    role: Literal[
        "detector",
        "recognizer",
        "layout",
        "vlm",
        "pipeline",
        "other",
    ] = "other"
    checkpoint_path: str | None = None
    experiment_id: ExperimentId | None = None
    metrics: dict[str, float] = Field(default_factory=dict)
    extras: dict[str, Any] = Field(default_factory=dict)
