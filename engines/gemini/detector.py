"""gemini detector adapter (stub)."""

from __future__ import annotations

from typing import Any

from aarogya_core.errors import NotImplementedComponentError
from aarogya_core.types.common import BoundingBox


class GeminiDetector:
    """Stub Detector for the gemini engine system."""

    engine_id = "gemini"

    def detect(self, image: Any) -> list[BoundingBox]:
        raise NotImplementedComponentError("gemini detector is not implemented yet")
