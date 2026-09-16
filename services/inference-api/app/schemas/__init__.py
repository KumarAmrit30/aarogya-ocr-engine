"""HTTP DTOs — thin wrappers over core types."""

from aarogya_core.types.ocr import OCRRequest, OCRResult
from pydantic import BaseModel, Field


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
    config_ref: str | None = None
    model_id: str | None = None
    dataset_id: str | None = None


# Re-export core OCR types for OpenAPI
__all__ = [
    "EvaluateRequest",
    "HealthResponse",
    "ModelInfo",
    "ModelListResponse",
    "OCRRequest",
    "OCRResult",
    "PlaceholderResponse",
    "TrainRequest",
    "VersionResponse",
]
