"""Common type primitives."""

from typing import Literal

from pydantic import BaseModel, Field

SCHEMA_VERSION: Literal["1.0"] = "1.0"


class SchemaVersionMixin(BaseModel):
    """Mixin that stamps domain objects with a schema version."""

    schema_version: Literal["1.0"] = SCHEMA_VERSION


class BoundingBox(BaseModel):
    """Axis-aligned bounding box in image pixel coordinates."""

    x1: float = Field(..., description="Left")
    y1: float = Field(..., description="Top")
    x2: float = Field(..., description="Right")
    y2: float = Field(..., description="Bottom")
    confidence: float | None = Field(default=None, ge=0.0, le=1.0)
