"""Inference engine interface (engine system entrypoint)."""

from __future__ import annotations

from typing import Protocol, runtime_checkable

from aarogya_core.interfaces.pipeline import Pipeline


@runtime_checkable
class InferenceEngine(Protocol):
    """Factory-like entry for an engine system (e.g. paddle, qwen)."""

    engine_id: str

    def build_pipeline(self, config_ref: str | None = None) -> Pipeline: ...
