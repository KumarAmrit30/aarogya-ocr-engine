"""Default DatasetPipeline orchestrator."""

from __future__ import annotations

from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from aarogya_core.types.data_platform import (
    DatasetEventType,
    DatasetManifest,
    DatasetQualityReport,
    DatasetRecord,
    DatasetSample,
    DatasetSource,
    DatasetSplit,
    DatasetVersion,
    PublishedVersionResult,
    SampleProvenance,
)
from aarogya_core.types.ids import DatasetId
from aarogya_datasets.cards import generate_card
from aarogya_datasets.converters.identity import IdentityConverter
from aarogya_datasets.fingerprint import compute_fingerprint
from aarogya_datasets.lineage import add_edge, empty_graph
from aarogya_datasets.loaders.synthetic import SyntheticLoader
from aarogya_datasets.pipeline.events import EventBus, default_bus
from aarogya_datasets.provenance import ProvenanceStore
from aarogya_datasets.quality import compute_quality
from aarogya_datasets.registry import allocate_version_id, publish_version
from aarogya_datasets.statistics import compute_statistics
from aarogya_datasets.storage.local import LocalStorage
from aarogya_datasets.validators import run_validators


class DefaultDatasetPipeline:
    """
    Executable ingest: load → convert → validate → stats → quality → card → publish.

    Does not hardcode public dataset names; uses plugins/config.
    """

    def __init__(
        self,
        repo_root: Path,
        *,
        bus: EventBus | None = None,
        storage: LocalStorage | None = None,
    ) -> None:
        self.repo_root = Path(repo_root)
        self.bus = bus or default_bus
        self.storage = storage or LocalStorage(self.repo_root)

    def run(
        self, source: DatasetSource, config: dict[str, Any] | None = None
    ) -> PublishedVersionResult:
        config = config or {}
        dataset_id: DatasetId = config.get("dataset_id", "DATASET-00001")  # type: ignore[assignment]
        version_label = config.get("version", "v1")
        human_name = config.get("name", source.name)
        samples_override: list[DatasetSample] | None = config.get("samples")

        # 1. Load
        loader = SyntheticLoader(samples=samples_override)
        samples = list(loader.load(dataset_id, split=config.get("split")))
        self.bus.emit(
            DatasetEventType.LOADED, dataset_id=dataset_id, message=source.name
        )

        # 2. Convert
        samples = IdentityConverter().convert(samples)

        # 3. Validate (structural)
        version_id = allocate_version_id(self.repo_root, dataset_id)
        validation = run_validators(
            samples, dataset_id=dataset_id, version_id=version_id
        )
        self.bus.emit(
            DatasetEventType.VALIDATED,
            dataset_id=dataset_id,
            version_id=version_id,
            payload={"passed": validation.passed},
        )

        # 4–5. Statistics + Quality (quality only if validation passed or allow_failed)
        statistics = compute_statistics(samples)
        self.bus.emit(
            DatasetEventType.STATISTICS_GENERATED,
            dataset_id=dataset_id,
            version_id=version_id,
        )

        allow_failed = bool(config.get("allow_failed_validation", False))
        if validation.passed or allow_failed:
            quality = compute_quality(
                samples, dataset_id=dataset_id, version_id=version_id
            )
        else:
            quality = DatasetQualityReport(
                dataset_id=dataset_id,
                version_id=version_id,
                overall_score=None,
                issues=[],
                metrics={},
                extras={"skipped": True, "reason": "validation_failed"},
            )
        self.bus.emit(
            DatasetEventType.QUALITY_COMPUTED,
            dataset_id=dataset_id,
            version_id=version_id,
        )

        # Manifest + fingerprint
        for s in samples:
            s.dataset_id = dataset_id
            s.version_id = version_id
        splits = [
            DatasetSplit(
                name="train",
                sample_ids=[str(s.sample_id) for s in samples],
                count=len(samples),
            )
        ]
        manifest = DatasetManifest(
            dataset_id=dataset_id,
            version_id=version_id,
            version=version_label,
            samples=samples,
            splits=splits,
        )
        fp = compute_fingerprint(
            manifest, statistics, dataset_id=dataset_id, version_id=version_id
        )
        manifest.fingerprint = fp.value
        self.bus.emit(
            DatasetEventType.FINGERPRINT_COMPUTED,
            dataset_id=dataset_id,
            version_id=version_id,
            payload={"fingerprint": fp.value},
        )
        self.bus.emit(
            DatasetEventType.MANIFEST_WRITTEN,
            dataset_id=dataset_id,
            version_id=version_id,
        )

        # Card
        record = DatasetRecord(
            dataset_id=dataset_id,
            name=human_name,
            source=source.name,
            source_info=source,
            task=config.get("task"),
            domain=config.get("domain"),
            language=list(config.get("language") or []),
            license=config.get("license"),
            tags=list(config.get("tags") or []),
            quality_score=quality.overall_score,
            versions=[],
        )
        version = DatasetVersion(
            version_id=version_id,
            version=version_label,
            status="validated" if validation.passed else "draft",
            change_notes=config.get("change_notes"),
            created_at=datetime.now(UTC),
        )
        card = generate_card(record, version, statistics, quality)
        self.bus.emit(
            DatasetEventType.CARD_GENERATED,
            dataset_id=dataset_id,
            version_id=version_id,
        )

        # Lineage
        lineage = empty_graph(dataset_id)
        lineage = add_edge(
            lineage, source.name, f"{dataset_id}/{version_id}", "converted"
        )
        lineage = add_edge(
            lineage,
            f"{dataset_id}/{version_id}",
            f"{dataset_id}/{version_id}#published",
            "published",
        )

        # Publish immutable version + registry
        path = publish_version(
            self.repo_root,
            record,
            version,
            manifest=manifest,
            statistics=statistics,
            validation=validation,
            quality=quality,
            card=card,
            lineage=lineage,
            storage=self.storage,
        )

        # Provenance (append-only) under published version
        prov_root = str(
            Path("datasets") / "versions" / dataset_id / version_id / "provenance"
        )
        store = ProvenanceStore(self.storage, prov_root)
        for s in samples:
            store.write(
                SampleProvenance(
                    dataset_id=dataset_id,
                    version_id=version_id,
                    sample_id=s.sample_id,
                    source=source.name,
                    original_filename=s.image.uri if s.image else None,
                    converted_by="IdentityConverter v1",
                    validation_status="passed" if validation.passed else "failed",
                    quality_score=quality.overall_score,
                    added_on=datetime.now(UTC),
                )
            )

        self.bus.emit(
            DatasetEventType.VERSION_PUBLISHED,
            dataset_id=dataset_id,
            version_id=version_id,
            message=str(path),
        )

        return PublishedVersionResult(
            dataset_id=dataset_id,
            version_id=version_id,
            version=version_label,
            path=str(path),
            fingerprint=fp.value,
            validation=validation,
            quality=quality,
            statistics=statistics,
            card_path=str(path / "card.md"),
            manifest_path=str(path / "manifest.json"),
        )
