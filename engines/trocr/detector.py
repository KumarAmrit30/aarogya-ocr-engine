"""trocr detector adapter (stub)."""

from __future__ import annotations

from typing import Any

from aarogya_core.errors import NotImplementedComponentError
from aarogya_core.types.common import BoundingBox


class TrocrDetector:
    """Stub Detector for the trocr engine system."""

    engine_id = "trocr"

    def detect(self, image: Any) -> list[BoundingBox]:
        raise NotImplementedComponentError("trocr detector is not implemented yet")
