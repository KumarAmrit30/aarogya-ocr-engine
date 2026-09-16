"""documentai recognizer adapter (stub)."""

from __future__ import annotations

from typing import Any

from aarogya_core.errors import NotImplementedComponentError
from aarogya_core.types.ocr import OCRLine


class DocumentaiRecognizer:
    """Stub Recognizer for the documentai engine system."""

    engine_id = "documentai"

    def recognize(self, image: Any, regions: list[Any] | None = None) -> list[OCRLine]:
        raise NotImplementedComponentError("documentai recognizer is not implemented yet")
