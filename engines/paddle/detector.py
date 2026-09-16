"""paddle detector adapter (stub)."""

from __future__ import annotations

from typing import Any

from aarogya_core.errors import NotImplementedComponentError
from aarogya_core.types.common import BoundingBox


class PaddleDetector:
    """Stub Detector for the paddle engine system."""

    engine_id = "paddle"

    def detect(self, image: Any) -> list[BoundingBox]:
        raise NotImplementedComponentError("paddle detector is not implemented yet")
