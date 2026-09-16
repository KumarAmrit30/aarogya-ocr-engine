"""Image preprocessing interface."""

from __future__ import annotations

from typing import Any, Protocol, runtime_checkable


@runtime_checkable
class Preprocessor(Protocol):
    """Transform raw images before detection/recognition."""

    engine_id: str

    def preprocess(self, image: Any) -> Any: ...
