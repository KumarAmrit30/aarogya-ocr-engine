"""Text / region detection interface."""

from __future__ import annotations

from typing import Any, Protocol, runtime_checkable

from aarogya_core.types.common import BoundingBox


@runtime_checkable
class Detector(Protocol):
    """Detect text regions in an image."""

    engine_id: str

    def detect(self, image: Any) -> list[BoundingBox]:
        """Return bounding boxes for text regions."""
        ...
