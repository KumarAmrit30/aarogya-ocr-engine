"""Generic file/blob Asset — multimodal-ready alternative to raw paths."""

from datetime import datetime
from typing import Any

from pydantic import Field

from aarogya_core.types.common import SchemaVersionMixin
from aarogya_core.types.ids import AssetId


class Asset(SchemaVersionMixin):
    """
    Addressable research artifact (image, pdf, json, annotation, …).

    Prefer Asset over bare Path strings in DatasetSample and pipelines.
    """

    asset_id: AssetId | str
    uri: str = Field(..., description="Backend URI or relative path")
    checksum: str | None = None
    mime: str | None = None
    size: int | None = Field(default=None, description="Bytes")
    created_at: datetime | None = None
    backend: str = Field(default="local", description="Storage backend id")
    extras: dict[str, Any] = Field(default_factory=dict)
