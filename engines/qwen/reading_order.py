"""qwen reading-order adapter (stub)."""

from __future__ import annotations

from aarogya_core.errors import NotImplementedComponentError
from aarogya_core.types.ocr import OCRLine


class QwenReadingOrder:
    """Stub ReadingOrder for the qwen engine system."""

    engine_id = "qwen"

    def order(self, lines: list[OCRLine]) -> list[OCRLine]:
        raise NotImplementedComponentError("qwen reading order is not implemented yet")
