"""Placeholder loader: IAM — no download."""

from __future__ import annotations

from collections.abc import Iterator

from aarogya_core.errors import NotImplementedComponentError
from aarogya_core.types.data_platform import DatasetSample
from aarogya_core.types.ids import DatasetId
from aarogya_datasets.loaders.registry import register_loader


@register_loader
class IAMLoader:
    name = "iam"

    def load(
        self, dataset_id: DatasetId, split: str | None = None
    ) -> Iterator[DatasetSample]:
        raise NotImplementedComponentError(
            "IAM loader is a scaffold only — no downloading in Phase 3"
        )
