"""parseq detector adapter (stub)."""

from __future__ import annotations

from typing import Any

from aarogya_core.errors import NotImplementedComponentError
from aarogya_core.types.common import BoundingBox


class ParseqDetector:
    """Stub Detector for the parseq engine system."""

    engine_id = "parseq"

    def detect(self, image: Any) -> list[BoundingBox]:
        raise NotImplementedComponentError("parseq detector is not implemented yet")
