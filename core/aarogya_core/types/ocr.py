"""OCR domain types."""

from enum import StrEnum
from typing import Any

from pydantic import BaseModel, Field

from aarogya_core.types.common import BoundingBox, SchemaVersionMixin


class PipelineStatus(StrEnum):
    """Pipeline execution status."""

    OK = "ok"
    NOT_IMPLEMENTED = "not_implemented"
    ERROR = "error"


class OCRWord(BaseModel):
    """A single recognized word."""

    text: str
    bbox: BoundingBox | None = None
    confidence: float | None = Field(default=None, ge=0.0, le=1.0)


class OCRLine(BaseModel):
    """A line of recognized text."""

    text: str
    words: list[OCRWord] = Field(default_factory=list)
    bbox: BoundingBox | None = None
    confidence: float | None = Field(default=None, ge=0.0, le=1.0)


class OCRRequest(SchemaVersionMixin):
    """Input for an OCR / HTR pipeline."""

    image_path: str | None = Field(default=None, description="Path relative to repo or absolute")
    image_base64: str | None = None
    engine_id: str | None = Field(default=None, description="e.g. paddle, qwen")
    config_ref: str | None = Field(default=None, description="Path under configs/")
    metadata: dict[str, Any] = Field(default_factory=dict)


class OCRResult(SchemaVersionMixin):
    """Output of an OCR / HTR pipeline."""

    status: PipelineStatus = PipelineStatus.NOT_IMPLEMENTED
    message: str | None = None
    full_text: str = ""
    lines: list[OCRLine] = Field(default_factory=list)
    engine_id: str | None = None
    config_hash: str | None = None
    metadata: dict[str, Any] = Field(default_factory=dict)
