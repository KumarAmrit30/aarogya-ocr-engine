"""Template reading-order adapter (stub)."""

from __future__ import annotations

from aarogya_core.errors import NotImplementedComponentError
from aarogya_core.types.ocr import OCRLine


class TemplateReadingOrder:
    """Stub ReadingOrder for the template engine system."""

    engine_id = "template"

    def order(self, lines: list[OCRLine]) -> list[OCRLine]:
        raise NotImplementedComponentError("template reading order is not implemented yet")
