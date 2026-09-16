"""Dataset loader interface."""

from __future__ import annotations

from collections.abc import Iterator
from typing import Any, Protocol, runtime_checkable

from aarogya_core.types.ids import DatasetId


@runtime_checkable
class DatasetLoader(Protocol):
    """Load samples from a registered dataset."""

    def load(
        self, dataset_id: DatasetId, split: str | None = None
    ) -> Iterator[Any]: ...
