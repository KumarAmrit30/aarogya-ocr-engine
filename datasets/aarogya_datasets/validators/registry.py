"""Validator plugin registry — structural checks only."""

from __future__ import annotations

from typing import TypeVar

from aarogya_core.errors import RegistryError

_REGISTRY: dict[str, type] = {}
T = TypeVar("T")


def register_validator(cls: T) -> T:
    name = getattr(cls, "name", None)
    if not name:
        raise RegistryError(f"{cls} missing name")
    _REGISTRY[str(name)] = cls  # type: ignore[assignment]
    return cls


def get_validator(name: str):
    if name not in _REGISTRY:
        raise RegistryError(f"Unknown validator: {name}")
    return _REGISTRY[name]()


def list_validators() -> list[str]:
    return sorted(_REGISTRY)
