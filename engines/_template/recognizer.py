"""Template recognizer adapter (stub)."""

from __future__ import annotations

from typing import Any

from aarogya_core.errors import NotImplementedComponentError
from aarogya_core.types.ocr import OCRLine


class TemplateRecognizer:
    """Stub Recognizer for the template engine system."""

    engine_id = "template"

    def recognize(self, image: Any, regions: list[Any] | None = None) -> list[OCRLine]:
        raise NotImplementedComponentError("template recognizer is not implemented yet")
