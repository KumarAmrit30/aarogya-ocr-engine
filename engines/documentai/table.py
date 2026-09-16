"""documentai table adapter (stub)."""

from __future__ import annotations

from typing import Any

from aarogya_core.errors import NotImplementedComponentError


class DocumentaiTableExtractor:
    """Stub TableExtractor for the documentai engine system."""

    engine_id = "documentai"

    def extract_tables(self, image: Any) -> list[dict[str, Any]]:
        raise NotImplementedComponentError("documentai table extractor is not implemented yet")
