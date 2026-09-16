"""Catalog load + immutable version publish helpers."""

from __future__ import annotations

from datetime import UTC, datetime
from pathlib import Path

import yaml

from aarogya_core.errors import RegistryError
from aarogya_core.registry import dump_yaml, load_dataset_registry, next_id
from aarogya_core.types.data_platform import (
    DatasetCard,
    DatasetLineageGraph,
    DatasetManifest,
    DatasetQualityReport,
    DatasetRecord,
    DatasetStatistics,
    DatasetValidationReport,
    DatasetVersion,
)
from aarogya_core.types.ids import DatasetId, VersionId
from aarogya_datasets.storage.local import LocalStorage


def catalog_path(repo_root: Path) -> Path:
    return repo_root / "datasets" / "registry.yaml"


def load_catalog(repo_root: Path) -> list[DatasetRecord]:
    path = catalog_path(repo_root)
    if not path.exists():
        return []
    return load_dataset_registry(path)


def save_catalog(repo_root: Path, records: list[DatasetRecord]) -> None:
    path = catalog_path(repo_root)
    dump_yaml(
        path,
        {
            "schema_version": "1.0",
            "datasets": [r.model_dump(mode="json") for r in records],
        },
    )


def version_dir(repo_root: Path, dataset_id: DatasetId, version_id: VersionId) -> Path:
    return repo_root / "datasets" / "versions" / dataset_id / version_id


def publish_version(
    repo_root: Path,
    record: DatasetRecord,
    version: DatasetVersion,
    *,
    manifest: DatasetManifest,
    statistics: DatasetStatistics,
    validation: DatasetValidationReport,
    quality: DatasetQualityReport,
    card: DatasetCard,
    lineage: DatasetLineageGraph | None = None,
    storage: LocalStorage | None = None,
    overwrite: bool = False,
) -> Path:
    """Write immutable version directory and update catalog."""
    if not version.version_id:
        raise RegistryError("version_id required to publish")
    root = version_dir(repo_root, record.dataset_id, version.version_id)
    marker = root / f"{version.version_id}.yaml"
    if marker.exists() and not overwrite:
        raise RegistryError(
            f"{version.version_id} already published under {record.dataset_id} — immutable"
        )
    storage = storage or LocalStorage(repo_root)
    root.mkdir(parents=True, exist_ok=True)

    version = version.model_copy(
        update={
            "path": str(root.relative_to(repo_root)),
            "manifest_path": str((root / "manifest.json").relative_to(repo_root)),
            "statistics_path": str((root / "statistics.json").relative_to(repo_root)),
            "quality_path": str((root / "quality.json").relative_to(repo_root)),
            "validation_path": str((root / "validation.json").relative_to(repo_root)),
            "card": str((root / "card.md").relative_to(repo_root)),
            "lineage_path": str((root / "lineage.yaml").relative_to(repo_root)),
            "status": "published",
            "created_at": version.created_at or datetime.now(UTC),
            "fingerprint": manifest.fingerprint,
            "sample_count": len(manifest.samples),
        }
    )

    (root / f"{version.version_id}.yaml").write_text(
        yaml.safe_dump(version.model_dump(mode="json"), sort_keys=False),
        encoding="utf-8",
    )
    (root / "manifest.json").write_text(
        manifest.model_dump_json(indent=2), encoding="utf-8"
    )
    (root / "statistics.json").write_text(
        statistics.model_dump_json(indent=2), encoding="utf-8"
    )
    (root / "quality.json").write_text(
        quality.model_dump_json(indent=2), encoding="utf-8"
    )
    (root / "validation.json").write_text(
        validation.model_dump_json(indent=2), encoding="utf-8"
    )
    if card.markdown:
        (root / "card.md").write_text(card.markdown, encoding="utf-8")
    if lineage:
        (root / "lineage.yaml").write_text(
            yaml.safe_dump(lineage.model_dump(mode="json"), sort_keys=False),
            encoding="utf-8",
        )

    # update catalog
    records = load_catalog(repo_root)
    by_id = {r.dataset_id: r for r in records}
    existing = by_id.get(record.dataset_id)
    if existing is None:
        record = record.model_copy(update={"versions": [version]})
        records.append(record)
    else:
        versions = [v for v in existing.versions if v.version_id != version.version_id]
        versions.append(version)
        by_id[record.dataset_id] = existing.model_copy(update={"versions": versions})
        records = list(by_id.values())
    save_catalog(repo_root, records)
    return root


def allocate_version_id(repo_root: Path, dataset_id: DatasetId) -> VersionId:
    existing: list[str] = []
    base = repo_root / "datasets" / "versions" / dataset_id
    if base.exists():
        existing = [p.name for p in base.iterdir() if p.is_dir()]
    return next_id("VERSION", existing)  # type: ignore[return-value]
