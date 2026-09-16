"""Preview builder — metadata only, no OCR rendering."""

from __future__ import annotations

from aarogya_core.types.data_platform import DatasetPreview, DatasetSample
from aarogya_core.types.ids import DatasetId


def build_preview(
    dataset_id: DatasetId,
    samples: list[DatasetSample],
    *,
    version: str | None = None,
    limit: int = 5,
) -> DatasetPreview:
    return DatasetPreview(
        dataset_id=dataset_id,
        version=version,
        samples=samples[:limit],
        message="Preview shows sample metadata/assets only — no OCR overlays",
    )
