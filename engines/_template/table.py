"""Template table adapter (stub)."""

from __future__ import annotations

from typing import Any

from aarogya_core.errors import NotImplementedComponentError


class TemplateTableExtractor:
    """Stub TableExtractor for the template engine system."""

    engine_id = "template"

    def extract_tables(self, image: Any) -> list[dict[str, Any]]:
        raise NotImplementedComponentError("template table extractor is not implemented yet")
