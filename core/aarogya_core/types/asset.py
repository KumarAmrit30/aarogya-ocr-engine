"""Asset registry types — concrete files, not logical models."""

from typing import Any, Literal

from pydantic import Field

from aarogya_core.types.common import SchemaVersionMixin
from aarogya_core.types.ids import AssetId, ModelId


class AssetRecord(SchemaVersionMixin):
    """Entry in assets/registry.yaml."""

    asset_id: AssetId
    name: str
    kind: Literal[
        "checkpoint",
        "tokenizer",
        "vocabulary",
        "lexicon",
        "prompt",
        "template",
        "weights",
        "export",
        "other",
    ] = "other"
    path: str | None = Field(default=None, description="Relative path under assets/")
    model_id: ModelId | None = None
    notes: str | None = None
    extras: dict[str, Any] = Field(default_factory=dict)
