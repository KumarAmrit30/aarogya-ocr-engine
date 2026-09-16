"""parseq recognizer adapter (stub)."""

from __future__ import annotations

from typing import Any

from aarogya_core.errors import NotImplementedComponentError
from aarogya_core.types.ocr import OCRLine


class ParseqRecognizer:
    """Stub Recognizer for the parseq engine system."""

    engine_id = "parseq"

    def recognize(self, image: Any, regions: list[Any] | None = None) -> list[OCRLine]:
        raise NotImplementedComponentError("parseq recognizer is not implemented yet")
