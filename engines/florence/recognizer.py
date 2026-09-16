"""florence recognizer adapter (stub)."""

from __future__ import annotations

from typing import Any

from aarogya_core.errors import NotImplementedComponentError
from aarogya_core.types.ocr import OCRLine


class FlorenceRecognizer:
    """Stub Recognizer for the florence engine system."""

    engine_id = "florence"

    def recognize(self, image: Any, regions: list[Any] | None = None) -> list[OCRLine]:
        raise NotImplementedComponentError("florence recognizer is not implemented yet")
