"""parseq table adapter (stub)."""

from __future__ import annotations

from typing import Any

from aarogya_core.errors import NotImplementedComponentError


class ParseqTableExtractor:
    """Stub TableExtractor for the parseq engine system."""

    engine_id = "parseq"

    def extract_tables(self, image: Any) -> list[dict[str, Any]]:
        raise NotImplementedComponentError("parseq table extractor is not implemented yet")
