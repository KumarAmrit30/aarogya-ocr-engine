"""gemini recognizer adapter (stub)."""

from __future__ import annotations

from typing import Any

from aarogya_core.errors import NotImplementedComponentError
from aarogya_core.types.ocr import OCRLine


class GeminiRecognizer:
    """Stub Recognizer for the gemini engine system."""

    engine_id = "gemini"

    def recognize(self, image: Any, regions: list[Any] | None = None) -> list[OCRLine]:
        raise NotImplementedComponentError("gemini recognizer is not implemented yet")
