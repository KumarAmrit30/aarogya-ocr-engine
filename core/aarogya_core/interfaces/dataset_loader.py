"""Dataset loader interface — yields canonical DatasetSample."""

from __future__ import annotations

from collections.abc import Iterator
from typing import Protocol, runtime_checkable

from aarogya_core.types.data_platform import DatasetSample
from aarogya_core.types.ids import DatasetId


@runtime_checkable
class DatasetLoader(Protocol):
    """Load samples from a registered dataset (dataset-agnostic)."""

    name: str

    def load(
        self, dataset_id: DatasetId, split: str | None = None
    ) -> Iterator[DatasetSample]: ...
