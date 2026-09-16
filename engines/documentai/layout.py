"""documentai layout adapter (stub)."""

from __future__ import annotations

from typing import Any

from aarogya_core.errors import NotImplementedComponentError


class DocumentaiLayoutAnalyzer:
    """Stub LayoutAnalyzer for the documentai engine system."""

    engine_id = "documentai"

    def analyze(self, image: Any) -> dict[str, Any]:
        raise NotImplementedComponentError("documentai layout analyzer is not implemented yet")
