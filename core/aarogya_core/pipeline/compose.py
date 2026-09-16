"""Compose pipeline steps from config without hard-coding engine imports."""

from __future__ import annotations

from collections.abc import Callable
from typing import Any

from aarogya_core.errors import ConfigError, NotImplementedComponentError
from aarogya_core.pipeline.base import BasePipeline
from aarogya_core.pipeline.ocr_pipeline import StubOCRPipeline
from aarogya_core.utils import config_hash

# Registry of named pipeline factories. Engines register here at import time later.
PIPELINE_FACTORIES: dict[str, Callable[[dict[str, Any]], BasePipeline]] = {
    "stub": lambda _cfg: StubOCRPipeline(),
}


def register_pipeline_factory(name: str, factory: Callable[[dict[str, Any]], BasePipeline]) -> None:
    PIPELINE_FACTORIES[name] = factory


def compose_pipeline(
    engine_id: str | None = None,
    config: dict[str, Any] | None = None,
) -> BasePipeline:
    """
    Build a pipeline by engine name.

    Foundation: only 'stub' is registered. Engines add factories without
    core importing engine packages directly.
    """
    config = config or {}
    name = (engine_id or config.get("engine_id") or "stub").lower()
    factory = PIPELINE_FACTORIES.get(name)
    if factory is None:
        raise NotImplementedComponentError(
            f"No pipeline factory registered for engine '{name}'. "
            f"Available: {sorted(PIPELINE_FACTORIES)}"
        )
    try:
        pipeline = factory(config)
    except Exception as exc:  # noqa: BLE001 — surface as config/composition error
        raise ConfigError(f"Failed to compose pipeline '{name}': {exc}") from exc
    pipeline.config_hash = config_hash(config) if config else None
    return pipeline
