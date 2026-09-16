"""documentai detector adapter (stub)."""

from __future__ import annotations

from typing import Any

from aarogya_core.errors import NotImplementedComponentError
from aarogya_core.types.common import BoundingBox


class DocumentaiDetector:
    """Stub Detector for the documentai engine system."""

    engine_id = "documentai"

    def detect(self, image: Any) -> list[BoundingBox]:
        raise NotImplementedComponentError("documentai detector is not implemented yet")
