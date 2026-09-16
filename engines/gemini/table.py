"""gemini table adapter (stub)."""

from __future__ import annotations

from typing import Any

from aarogya_core.errors import NotImplementedComponentError


class GeminiTableExtractor:
    """Stub TableExtractor for the gemini engine system."""

    engine_id = "gemini"

    def extract_tables(self, image: Any) -> list[dict[str, Any]]:
        raise NotImplementedComponentError("gemini table extractor is not implemented yet")
