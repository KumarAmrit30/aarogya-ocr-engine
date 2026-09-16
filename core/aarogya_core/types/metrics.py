"""Evaluation metrics types."""

from typing import Any

from pydantic import Field

from aarogya_core.types.common import SchemaVersionMixin


class Metrics(SchemaVersionMixin):
    """Generic metrics bag for evaluation and benchmarks."""

    name: str = "unnamed"
    values: dict[str, float] = Field(default_factory=dict)
    extras: dict[str, Any] = Field(default_factory=dict)
