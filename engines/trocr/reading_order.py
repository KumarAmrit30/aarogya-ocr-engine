"""trocr reading-order adapter (stub)."""

from __future__ import annotations

from aarogya_core.errors import NotImplementedComponentError
from aarogya_core.types.ocr import OCRLine


class TrocrReadingOrder:
    """Stub ReadingOrder for the trocr engine system."""

    engine_id = "trocr"

    def order(self, lines: list[OCRLine]) -> list[OCRLine]:
        raise NotImplementedComponentError("trocr reading order is not implemented yet")
