"""parseq reading-order adapter (stub)."""

from __future__ import annotations

from aarogya_core.errors import NotImplementedComponentError
from aarogya_core.types.ocr import OCRLine


class ParseqReadingOrder:
    """Stub ReadingOrder for the parseq engine system."""

    engine_id = "parseq"

    def order(self, lines: list[OCRLine]) -> list[OCRLine]:
        raise NotImplementedComponentError("parseq reading order is not implemented yet")
