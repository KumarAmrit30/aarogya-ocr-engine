"""parseq layout adapter (stub)."""

from __future__ import annotations

from typing import Any

from aarogya_core.errors import NotImplementedComponentError


class ParseqLayoutAnalyzer:
    """Stub LayoutAnalyzer for the parseq engine system."""

    engine_id = "parseq"

    def analyze(self, image: Any) -> dict[str, Any]:
        raise NotImplementedComponentError("parseq layout analyzer is not implemented yet")
