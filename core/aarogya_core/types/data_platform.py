"""Research Data Platform domain types — dataset-agnostic."""

from __future__ import annotations

from datetime import datetime
from enum import StrEnum
from typing import Any, Literal

from pydantic import BaseModel, Field, model_validator

from aarogya_core.types.common import BoundingBox, SchemaVersionMixin
from aarogya_core.types.ids import DatasetId, SampleId, VersionId
from aarogya_core.types.media_asset import Asset


class PIIStatus(StrEnum):
    """Privacy status for datasets and samples."""

    UNKNOWN = "unknown"
    CONTAINS_PHI = "contains_phi"
    REDACTED = "redacted"
    VERIFIED_SAFE = "verified_safe"


class PIIMetadata(BaseModel):
    """PII flags — metadata only; no redaction implementation."""

    status: PIIStatus = PIIStatus.UNKNOWN
    contains_patient_name: bool | None = None
    contains_address: bool | None = None
    contains_phone: bool | None = None
    contains_doctor_signature: bool | None = None
    contains_hospital_identifier: bool | None = None
    contains_barcode: bool | None = None
    contains_qr_code: bool | None = None
    requires_redaction: bool = False
    redaction_complete: bool = False
    notes: str | None = None


class DatasetSource(SchemaVersionMixin):
    """Origin of a dataset (public, synthetic, or proprietary)."""

    name: str
    kind: Literal["public", "synthetic", "proprietary", "internal", "unknown"] = "unknown"
    uri: str | None = None
    homepage: str | None = None
    paper: str | None = None
    extras: dict[str, Any] = Field(default_factory=dict)


class DatasetLicense(BaseModel):
    """License metadata."""

    name: str | None = None
    spdx: str | None = None
    path: str | None = Field(default=None, description="Path under datasets/licenses/")
    allows_commercial: bool | None = None
    notes: str | None = None


class DatasetChecksum(BaseModel):
    """Checksum for a file or aggregate artifact."""

    algorithm: str = "sha256"
    value: str
    path: str | None = None


class DatasetArtifact(BaseModel):
    """Named artifact attached to a dataset version."""

    name: str
    asset: Asset | None = None
    path: str | None = None
    kind: str = "other"


class DatasetVersion(BaseModel):
    """
    One scientific version of a dataset (immutable once published).

    Human label `version` (v1, v2) maps to stable `version_id` (VERSION-#####).
    """

    version_id: VersionId | None = None
    version: str = Field(..., description="Human label, e.g. v1, v2, v3")
    path: str | None = Field(default=None, description="Relative path under datasets/versions/")
    card: str | None = None
    manifest_path: str | None = None
    statistics_path: str | None = None
    quality_path: str | None = None
    validation_path: str | None = None
    lineage_path: str | None = None
    fingerprint: str | None = None
    split: dict[str, int | float] | None = None
    parent_version: str | None = None
    parent_version_id: VersionId | None = None
    change_notes: str | None = None
    status: Literal["draft", "validated", "published", "deprecated"] = "draft"
    pii: PIIMetadata | None = None
    page_count: int | None = None
    sample_count: int | None = None
    created_at: datetime | None = None
    extras: dict[str, Any] = Field(default_factory=dict)


class DatasetRecord(SchemaVersionMixin):
    """Catalog entry in datasets/registry.yaml (not blob storage)."""

    dataset_id: DatasetId
    name: str
    license: str | None = None
    license_info: DatasetLicense | None = None
    language: list[str] = Field(default_factory=list)
    script: list[str] = Field(default_factory=list)
    writer_count: int | None = None
    page_count: int | None = None
    source: str | None = None
    source_info: DatasetSource | None = None
    homepage: str | None = None
    paper: str | None = None
    task: str | None = Field(default=None, description="e.g. HTR, OCR, layout")
    domain: str | None = Field(default=None, description="e.g. medical, general")
    quality: Literal["unknown", "low", "medium", "high"] = "unknown"
    quality_score: float | None = None
    status: Literal["registered", "ingesting", "ready", "deprecated"] = "registered"
    tags: list[str] = Field(default_factory=list)
    notes: str | None = None
    versions: list[DatasetVersion] = Field(default_factory=list)
    # Legacy flat fields
    version: str | None = None
    split: dict[str, int | float] | None = None
    path: str | None = None
    card: str | None = None
    extras: dict[str, Any] = Field(default_factory=dict)

    @model_validator(mode="after")
    def ensure_default_version(self) -> DatasetRecord:
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
        """Resolve by human label, VERSION-#####, or latest."""
        if not self.versions:
            raise ValueError(f"Dataset {self.dataset_id} has no versions")
        if version is None:
            return self.versions[-1]
        for item in self.versions:
            if item.version == version or item.version_id == version:
                return item
        raise KeyError(f"Version {version!r} not found for {self.dataset_id}")


class DatasetSample(SchemaVersionMixin):
    """Canonical sample — evaluation consumes this shape only."""

    sample_id: SampleId | str
    dataset_id: DatasetId | None = None
    version_id: VersionId | None = None
    split: str | None = None
    text: str = ""
    lines: list[str] = Field(default_factory=list)
    words: list[str] = Field(default_factory=list)
    bboxes: list[BoundingBox] = Field(default_factory=list)
    image: Asset | None = None
    annotation: Asset | None = None
    extras_assets: list[Asset] = Field(default_factory=list)
    writer_id: str | None = None
    language: str | None = None
    script: str | None = None
    metadata: dict[str, Any] = Field(default_factory=dict)

    @property
    def image_uri(self) -> str | None:
        return self.image.uri if self.image else None


class DatasetSplit(BaseModel):
    """Named split over sample ids."""

    name: str
    sample_ids: list[str] = Field(default_factory=list)
    count: int | None = None


class DatasetStatistics(SchemaVersionMixin):
    """Extensible statistics bag for a dataset version."""

    values: dict[str, float | int | str] = Field(default_factory=dict)
    distributions: dict[str, dict[str, float | int]] = Field(default_factory=dict)
    extras: dict[str, Any] = Field(default_factory=dict)


class DatasetManifest(SchemaVersionMixin):
    """Sample index for a published version (eval-facing)."""

    dataset_id: DatasetId
    version_id: VersionId | None = None
    version: str | None = None
    samples: list[DatasetSample] = Field(default_factory=list)
    splits: list[DatasetSplit] = Field(default_factory=list)
    fingerprint: str | None = None
    extras: dict[str, Any] = Field(default_factory=dict)


class DatasetMetadata(BaseModel):
    """Loose metadata bag."""

    fields: dict[str, Any] = Field(default_factory=dict)


class DatasetCard(SchemaVersionMixin):
    """Structured dataset card content."""

    dataset_id: DatasetId
    version: str | None = None
    overview: str = ""
    source: str | None = None
    license: str | None = None
    paper: str | None = None
    homepage: str | None = None
    statistics_summary: str | None = None
    quality_summary: str | None = None
    limitations: str | None = None
    known_issues: str | None = None
    citation: str | None = None
    recommended_use: str | None = None
    future_improvements: str | None = None
    markdown: str | None = None


class DatasetValidationIssue(BaseModel):
    """One structural validation finding."""

    code: str
    severity: Literal["error", "warning", "info"] = "error"
    message: str
    sample_id: str | None = None
    path: str | None = None


class DatasetValidationReport(SchemaVersionMixin):
    """Structural validity — not research quality."""

    dataset_id: DatasetId | None = None
    version_id: VersionId | None = None
    passed: bool = False
    issues: list[DatasetValidationIssue] = Field(default_factory=list)
    extras: dict[str, Any] = Field(default_factory=dict)


class DatasetQualityIssue(BaseModel):
    """One quality finding (goodness, not structure)."""

    code: str
    severity: Literal["error", "warning", "info"] = "warning"
    message: str
    score: float | None = None
    sample_id: str | None = None


class DatasetQualityReport(SchemaVersionMixin):
    """Research quality — separate from validation."""

    dataset_id: DatasetId | None = None
    version_id: VersionId | None = None
    overall_score: float | None = None
    issues: list[DatasetQualityIssue] = Field(default_factory=list)
    metrics: dict[str, float] = Field(default_factory=dict)
    extras: dict[str, Any] = Field(default_factory=dict)


class DatasetInspectionResult(SchemaVersionMixin):
    """Explorer inspection payload."""

    dataset_id: DatasetId
    version: str | None = None
    validation: DatasetValidationReport | None = None
    quality: DatasetQualityReport | None = None
    statistics: DatasetStatistics | None = None


class DatasetPreview(SchemaVersionMixin):
    """Preview panel data (no OCR rendering)."""

    dataset_id: DatasetId
    version: str | None = None
    samples: list[DatasetSample] = Field(default_factory=list)
    message: str | None = None


class DatasetCollection(SchemaVersionMixin):
    """Named group of datasets."""

    name: str
    dataset_ids: list[DatasetId] = Field(default_factory=list)
    notes: str | None = None


class SampleProvenance(SchemaVersionMixin):
    """Per-sample lineage for medical/research auditability."""

    dataset_id: DatasetId
    version_id: VersionId | None = None
    sample_id: SampleId | str
    source: str | None = None
    original_filename: str | None = None
    original_annotation_ref: str | None = None
    converted_by: str | None = None
    validation_status: str | None = None
    quality_score: float | None = None
    pii_status: PIIStatus = PIIStatus.UNKNOWN
    added_on: datetime | None = None
    extras: dict[str, Any] = Field(default_factory=dict)


class DatasetFingerprint(SchemaVersionMixin):
    """Stable hash over manifest + splits + checksums + metadata + stats."""

    algorithm: str = "sha256"
    value: str
    dataset_id: DatasetId | None = None
    version_id: VersionId | None = None
    inputs: list[str] = Field(default_factory=list)


class LineageEdge(BaseModel):
    """Edge in a dataset-level lineage DAG."""

    from_node: str
    to_node: str
    relation: Literal[
        "converted",
        "canonicalized",
        "augmented",
        "filtered",
        "split",
        "published",
        "derived",
    ] = "derived"
    notes: str | None = None


class DatasetLineageGraph(SchemaVersionMixin):
    """Dataset-level transformation graph (not only sample provenance)."""

    dataset_id: DatasetId
    nodes: list[str] = Field(default_factory=list)
    edges: list[LineageEdge] = Field(default_factory=list)


class DatasetEventType(StrEnum):
    LOADED = "dataset_loaded"
    VALIDATED = "dataset_validated"
    VERSION_PUBLISHED = "version_published"
    QUALITY_COMPUTED = "quality_computed"
    STATISTICS_GENERATED = "statistics_generated"
    MANIFEST_WRITTEN = "manifest_written"
    CARD_GENERATED = "card_generated"
    FINGERPRINT_COMPUTED = "fingerprint_computed"


class DatasetEvent(SchemaVersionMixin):
    """In-process dataset lifecycle event."""

    type: DatasetEventType
    dataset_id: DatasetId | None = None
    version_id: VersionId | None = None
    message: str | None = None
    payload: dict[str, Any] = Field(default_factory=dict)
    created_at: datetime | None = None


class DatasetSearchQuery(BaseModel):
    """Explorer search/filter contract."""

    language: str | None = None
    license: str | None = None
    task: str | None = None
    script: str | None = None
    domain: str | None = None
    min_quality: float | None = None
    tags: list[str] = Field(default_factory=list)
    pii_status: PIIStatus | None = None
    name_contains: str | None = None


class PublishedVersionResult(SchemaVersionMixin):
    """Result of DatasetPipeline.run."""

    dataset_id: DatasetId
    version_id: VersionId | None = None
    version: str
    path: str | None = None
    fingerprint: str | None = None
    validation: DatasetValidationReport | None = None
    quality: DatasetQualityReport | None = None
    statistics: DatasetStatistics | None = None
    card_path: str | None = None
    manifest_path: str | None = None
