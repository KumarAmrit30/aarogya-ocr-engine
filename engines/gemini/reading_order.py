"""gemini reading-order adapter (stub)."""

from __future__ import annotations

from aarogya_core.errors import NotImplementedComponentError
from aarogya_core.types.ocr import OCRLine


class GeminiReadingOrder:
    """Stub ReadingOrder for the gemini engine system."""

    engine_id = "gemini"

    def order(self, lines: list[OCRLine]) -> list[OCRLine]:
        raise NotImplementedComponentError("gemini reading order is not implemented yet")
