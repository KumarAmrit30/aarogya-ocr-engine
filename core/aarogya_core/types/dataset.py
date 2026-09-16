"""Dataset registry record types."""

from typing import Any, Literal

from pydantic import Field

from aarogya_core.types.common import SchemaVersionMixin
from aarogya_core.types.ids import DatasetId


class DatasetRecord(SchemaVersionMixin):
    """Entry in datasets/registry.yaml."""

    dataset_id: DatasetId
    name: str
    version: str = "0.1.0"
    license: str | None = None
    language: list[str] = Field(default_factory=list)
    writer_count: int | None = None
    source: str | None = None
    quality: Literal["unknown", "low", "medium", "high"] = "unknown"
    split: dict[str, int | float] | None = None
    path: str | None = Field(default=None, description="Relative path under datasets/")
    card: str | None = Field(default=None, description="Path to dataset card markdown")
    extras: dict[str, Any] = Field(default_factory=dict)
