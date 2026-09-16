"""Template detector adapter (stub)."""

from __future__ import annotations

from typing import Any

from aarogya_core.errors import NotImplementedComponentError
from aarogya_core.types.common import BoundingBox


class TemplateDetector:
    """Stub Detector for the template engine system."""

    engine_id = "template"

    def detect(self, image: Any) -> list[BoundingBox]:
        raise NotImplementedComponentError("template detector is not implemented yet")
