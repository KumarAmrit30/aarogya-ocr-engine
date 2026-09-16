"""florence detector adapter (stub)."""

from __future__ import annotations

from typing import Any

from aarogya_core.errors import NotImplementedComponentError
from aarogya_core.types.common import BoundingBox


class FlorenceDetector:
    """Stub Detector for the florence engine system."""

    engine_id = "florence"

    def detect(self, image: Any) -> list[BoundingBox]:
        raise NotImplementedComponentError("florence detector is not implemented yet")
