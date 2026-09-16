"""Compose / register dataset pipelines."""

from __future__ import annotations

from collections.abc import Callable
from pathlib import Path
from typing import Any

from aarogya_core.errors import NotImplementedComponentError
from aarogya_datasets.pipeline.base import DatasetPipeline
from aarogya_datasets.pipeline.default import DefaultDatasetPipeline

PIPELINE_FACTORIES: dict[str, Callable[[Path, dict[str, Any]], DatasetPipeline]] = {
    "default": lambda root, _cfg: DefaultDatasetPipeline(root),
}


def register_pipeline_factory(
    name: str, factory: Callable[[Path, dict[str, Any]], DatasetPipeline]
) -> None:
    PIPELINE_FACTORIES[name] = factory


def compose_pipeline(
    repo_root: Path, name: str = "default", config: dict[str, Any] | None = None
) -> DatasetPipeline:
    factory = PIPELINE_FACTORIES.get(name)
    if factory is None:
        raise NotImplementedComponentError(f"Unknown dataset pipeline: {name}")
    return factory(repo_root, config or {})
