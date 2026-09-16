"""HTTP DTOs — thin wrappers over core types."""

from typing import Any

from pydantic import BaseModel, Field

from aarogya_core.types.data_platform import (
    DatasetLineageGraph,
    DatasetQualityReport,
    DatasetRecord,
    DatasetStatistics,
    DatasetValidationReport,
    DatasetVersion,
)
from aarogya_core.types.evaluation import (
    EvaluationConfig,
    EvaluationReport,
    GroundTruth,
    Prediction,
)
from aarogya_core.types.ocr import OCRRequest, OCRResult


class HealthResponse(BaseModel):
    status: str = "ok"
    service: str
    time: str


class VersionResponse(BaseModel):
    version: str
    api_schema_version: str
    git_sha: str | None = None
    platform: str = "aarogya-ai-research-platform"


class PlaceholderResponse(BaseModel):
    status: str = "not_implemented"
    message: str


class ModelInfo(BaseModel):
    model_id: str | None = None
    name: str
    engine_id: str | None = None
    role: str | None = None


class ModelListResponse(BaseModel):
    models: list[ModelInfo] = Field(default_factory=list)
    message: str = "Model registry wiring not implemented yet"


class TrainRequest(BaseModel):
    config_ref: str | None = None
    experiment_name: str | None = None


class EvaluateRequest(BaseModel):
    """GT/prediction pairs for the evaluation engine (no OCR)."""

    references: list[GroundTruth] = Field(default_factory=list)
    predictions: list[Prediction] = Field(default_factory=list)
    config: EvaluationConfig | None = None


class ReportListResponse(BaseModel):
    reports: list[dict[str, str]] = Field(default_factory=list)


class BenchmarkListResponse(BaseModel):
    suites: list[dict[str, str]] = Field(default_factory=list)


class DatasetListResponse(BaseModel):
    datasets: list[DatasetRecord] = Field(default_factory=list)


class DatasetVersionDetailResponse(BaseModel):
    dataset: DatasetRecord
    version: DatasetVersion
    fingerprint: str | None = None
    validation: DatasetValidationReport | None = None
    quality: DatasetQualityReport | None = None
    statistics: DatasetStatistics | None = None
    lineage: DatasetLineageGraph | None = None
    card_markdown: str | None = None


class PipelineRunRequest(BaseModel):
    """Synthetic pipeline demo — no downloads/OCR."""

    name: str = "synthetic-demo"
    dataset_id: str = "DATASET-00001"
    version: str = "v1"
    task: str | None = "HTR"
    domain: str | None = "medical"
    language: list[str] = Field(default_factory=lambda: ["en"])
    license: str | None = "research-only"
    tags: list[str] = Field(default_factory=list)
    config: dict[str, Any] = Field(default_factory=dict)


__all__ = [
    "BenchmarkListResponse",
    "DatasetListResponse",
    "DatasetVersionDetailResponse",
    "EvaluateRequest",
    "EvaluationReport",
    "HealthResponse",
    "ModelInfo",
    "ModelListResponse",
    "OCRRequest",
    "OCRResult",
    "PipelineRunRequest",
    "PlaceholderResponse",
    "ReportListResponse",
    "TrainRequest",
    "VersionResponse",
]
