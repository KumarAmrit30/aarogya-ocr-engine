"""DatasetFingerprint computation."""

from __future__ import annotations

import hashlib
import json

from aarogya_core.types.data_platform import (
    DatasetFingerprint,
    DatasetManifest,
    DatasetStatistics,
)
from aarogya_core.types.ids import DatasetId, VersionId


def compute_fingerprint(
    manifest: DatasetManifest,
    statistics: DatasetStatistics | None = None,
    *,
    dataset_id: DatasetId | None = None,
    version_id: VersionId | None = None,
) -> DatasetFingerprint:
    payload = {
        "sample_ids": [str(s.sample_id) for s in manifest.samples],
        "texts": [s.text for s in manifest.samples],
        "splits": [sp.model_dump(mode="json") for sp in manifest.splits],
        "statistics": statistics.values if statistics else {},
        "dataset_id": dataset_id or manifest.dataset_id,
        "version_id": version_id or manifest.version_id,
    }
    blob = json.dumps(payload, sort_keys=True, default=str)
    digest = hashlib.sha256(blob.encode("utf-8")).hexdigest()
    return DatasetFingerprint(
        value=digest,
        dataset_id=dataset_id or manifest.dataset_id,
        version_id=version_id or manifest.version_id,
        inputs=["manifest.samples", "manifest.splits", "statistics.values"],
    )
