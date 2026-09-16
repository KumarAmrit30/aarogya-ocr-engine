"""documentai reading-order adapter (stub)."""

from __future__ import annotations

from aarogya_core.errors import NotImplementedComponentError
from aarogya_core.types.ocr import OCRLine


class DocumentaiReadingOrder:
    """Stub ReadingOrder for the documentai engine system."""

    engine_id = "documentai"

    def order(self, lines: list[OCRLine]) -> list[OCRLine]:
        raise NotImplementedComponentError("documentai reading order is not implemented yet")
