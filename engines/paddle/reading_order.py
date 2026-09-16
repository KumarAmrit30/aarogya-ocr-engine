"""paddle reading-order adapter (stub)."""

from __future__ import annotations

from aarogya_core.errors import NotImplementedComponentError
from aarogya_core.types.ocr import OCRLine


class PaddleReadingOrder:
    """Stub ReadingOrder for the paddle engine system."""

    engine_id = "paddle"

    def order(self, lines: list[OCRLine]) -> list[OCRLine]:
        raise NotImplementedComponentError("paddle reading order is not implemented yet")
