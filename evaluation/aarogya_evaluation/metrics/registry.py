"""Metric registry with auto-registration decorator."""

from __future__ import annotations

from typing import TypeVar

from aarogya_core.errors import RegistryError
from aarogya_evaluation.metrics.base import BaseMetric

_REGISTRY: dict[str, type[BaseMetric]] = {}
T = TypeVar("T", bound=type[BaseMetric])


def register_metric(cls: T) -> T:
    """Class decorator — metrics auto-register on import."""
    name = getattr(cls, "name", None)
    if not name or not isinstance(name, str):
        raise RegistryError(f"Metric class {cls.__name__} missing string `name`")
    if name in _REGISTRY:
        raise RegistryError(f"Duplicate metric registration: {name}")
    _REGISTRY[name] = cls
    return cls


def get_metric_class(name: str) -> type[BaseMetric]:
    if name not in _REGISTRY:
        raise RegistryError(f"Unknown metric: {name}. Known: {sorted(_REGISTRY)}")
    return _REGISTRY[name]


def list_metrics(*, implemented_only: bool = False) -> list[str]:
    names = []
    for name, cls in sorted(_REGISTRY.items()):
        if implemented_only and not getattr(cls, "implemented", True):
            continue
        names.append(name)
    return names


def clear_registry() -> None:
    """Test helper."""
    _REGISTRY.clear()
