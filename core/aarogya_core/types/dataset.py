"""Dataset registry record types with versioned scientific artifacts."""

from datetime import datetime
from typing import Any, Literal

from pydantic import BaseModel, Field, model_validator

from aarogya_core.types.common import SchemaVersionMixin
from aarogya_core.types.ids import DatasetId


class DatasetVersion(BaseModel):
    """
    One scientific version of a dataset (immutable once published).

    Example: DATASET-00007 @ v3 after label cleanup and a new train split.
    """

    version: str = Field(..., description="Version label, e.g. v1, v2, v3")
    path: str | None = Field(default=None, description="Relative path under datasets/")
    card: str | None = None
    split: dict[str, int | float] | None = Field(
        default=None,
        description="Split sizes or ratios for this version",
    )
    parent_version: str | None = Field(
        default=None,
        description="Prior version this was derived from",
    )
    change_notes: str | None = None
    created_at: datetime | None = None
    extras: dict[str, Any] = Field(default_factory=dict)


class DatasetRecord(SchemaVersionMixin):
    """Entry in datasets/registry.yaml."""

    dataset_id: DatasetId
    name: str
    license: str | None = None
    language: list[str] = Field(default_factory=list)
    writer_count: int | None = None
    source: str | None = None
    quality: Literal["unknown", "low", "medium", "high"] = "unknown"
    versions: list[DatasetVersion] = Field(default_factory=list)
    # Legacy flat fields — used to synthesize v1 when versions is empty
    version: str | None = Field(
        default=None,
        description="Deprecated flat version string; prefer versions[].version",
    )
    split: dict[str, int | float] | None = None
    path: str | None = Field(
        default=None, description="Legacy path; prefer versions[].path"
    )
    card: str | None = None
    extras: dict[str, Any] = Field(default_factory=dict)

    @model_validator(mode="after")
    def ensure_default_version(self) -> "DatasetRecord":
        if not self.versions:
            self.versions = [
                DatasetVersion(
                    version=self.version or "v1",
                    path=self.path,
                    card=self.card,
                    split=self.split,
                )
            ]
        return self

    def get_version(self, version: str | None = None) -> DatasetVersion:
        """Return a named version or the latest listed version."""
        if not self.versions:
            raise ValueError(f"Dataset {self.dataset_id} has no versions")
        if version is None:
            return self.versions[-1]
        for item in self.versions:
            if item.version == version:
                return item
        raise KeyError(f"Version {version!r} not found for {self.dataset_id}")
