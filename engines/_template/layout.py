"""Template layout adapter (stub)."""

from __future__ import annotations

from typing import Any

from aarogya_core.errors import NotImplementedComponentError


class TemplateLayoutAnalyzer:
    """Stub LayoutAnalyzer for the template engine system."""

    engine_id = "template"

    def analyze(self, image: Any) -> dict[str, Any]:
        raise NotImplementedComponentError("template layout analyzer is not implemented yet")
