"""qwen detector adapter (stub)."""

from __future__ import annotations

from typing import Any

from aarogya_core.errors import NotImplementedComponentError
from aarogya_core.types.common import BoundingBox


class QwenDetector:
    """Stub Detector for the qwen engine system."""

    engine_id = "qwen"

    def detect(self, image: Any) -> list[BoundingBox]:
        raise NotImplementedComponentError("qwen detector is not implemented yet")
