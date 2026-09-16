"""Quality analyzer registry — research goodness only."""

from __future__ import annotations

from typing import TypeVar

from aarogya_core.errors import RegistryError

_REGISTRY: dict[str, type] = {}
T = TypeVar("T")


def register_quality(cls: T) -> T:
    name = getattr(cls, "name", None)
    if not name:
        raise RegistryError(f"{cls} missing name")
    _REGISTRY[str(name)] = cls  # type: ignore[assignment]
    return cls


def list_quality() -> list[str]:
    return sorted(_REGISTRY)


def get_quality(name: str):
    return _REGISTRY[name]()
