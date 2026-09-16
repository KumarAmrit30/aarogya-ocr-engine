"""In-memory synthetic loader for pipeline demos/tests."""

from __future__ import annotations

from collections.abc import Iterator

from aarogya_core.types.data_platform import DatasetSample
from aarogya_core.types.ids import DatasetId
from aarogya_core.types.media_asset import Asset
from aarogya_datasets.loaders.registry import register_loader


@register_loader
class SyntheticLoader:
    """Yields synthetic samples — used by DefaultDatasetPipeline demos."""

    name = "synthetic"

    def __init__(self, samples: list[DatasetSample] | None = None) -> None:
        self._samples = samples

    def load(
        self, dataset_id: DatasetId, split: str | None = None
    ) -> Iterator[DatasetSample]:
        if self._samples is not None:
            yield from self._samples
            return
        for i in range(1, 4):
            sid = f"SAMPLE-{i:05d}"
            yield DatasetSample(
                sample_id=sid,
                dataset_id=dataset_id,
                split=split or "train",
                text=f"sample text {i}",
                words=f"sample text {i}".split(),
                image=Asset(
                    asset_id=f"ASSET-{i:05d}",
                    uri=f"synthetic://{sid}.png",
                    mime="image/png",
                ),
            )
