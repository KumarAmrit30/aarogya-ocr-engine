"""qwen table adapter (stub)."""

from __future__ import annotations

from typing import Any

from aarogya_core.errors import NotImplementedComponentError


class QwenTableExtractor:
    """Stub TableExtractor for the qwen engine system."""

    engine_id = "qwen"

    def extract_tables(self, image: Any) -> list[dict[str, Any]]:
        raise NotImplementedComponentError("qwen table extractor is not implemented yet")
