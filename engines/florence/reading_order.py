"""florence reading-order adapter (stub)."""

from __future__ import annotations

from aarogya_core.errors import NotImplementedComponentError
from aarogya_core.types.ocr import OCRLine


class FlorenceReadingOrder:
    """Stub ReadingOrder for the florence engine system."""

    engine_id = "florence"

    def order(self, lines: list[OCRLine]) -> list[OCRLine]:
        raise NotImplementedComponentError("florence reading order is not implemented yet")
