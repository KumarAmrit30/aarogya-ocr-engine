"""qwen recognizer adapter (stub)."""

from __future__ import annotations

from typing import Any

from aarogya_core.errors import NotImplementedComponentError
from aarogya_core.types.ocr import OCRLine


class QwenRecognizer:
    """Stub Recognizer for the qwen engine system."""

    engine_id = "qwen"

    def recognize(self, image: Any, regions: list[Any] | None = None) -> list[OCRLine]:
        raise NotImplementedComponentError("qwen recognizer is not implemented yet")
