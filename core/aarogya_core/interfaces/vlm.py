"""Vision-language model interface."""

from __future__ import annotations

from typing import Any, Protocol, runtime_checkable


@runtime_checkable
class VisionLanguageModel(Protocol):
    """General VLM for document understanding."""

    engine_id: str

    def generate(self, image: Any, prompt: str, **kwargs: Any) -> str: ...
