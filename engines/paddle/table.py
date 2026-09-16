"""paddle table adapter (stub)."""

from __future__ import annotations

from typing import Any

from aarogya_core.errors import NotImplementedComponentError


class PaddleTableExtractor:
    """Stub TableExtractor for the paddle engine system."""

    engine_id = "paddle"

    def extract_tables(self, image: Any) -> list[dict[str, Any]]:
        raise NotImplementedComponentError("paddle table extractor is not implemented yet")
