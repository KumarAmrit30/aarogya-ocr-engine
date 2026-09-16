"""trocr table adapter (stub)."""

from __future__ import annotations

from typing import Any

from aarogya_core.errors import NotImplementedComponentError


class TrocrTableExtractor:
    """Stub TableExtractor for the trocr engine system."""

    engine_id = "trocr"

    def extract_tables(self, image: Any) -> list[dict[str, Any]]:
        raise NotImplementedComponentError("trocr table extractor is not implemented yet")
