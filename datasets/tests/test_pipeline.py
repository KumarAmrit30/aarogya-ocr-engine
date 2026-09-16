"""Dataset pipeline and storage tests."""

from __future__ import annotations

from pathlib import Path

import pytest
import yaml

from aarogya_core.types.data_platform import (
    DatasetEventType,
    DatasetManifest,
    DatasetSample,
    DatasetSearchQuery,
    DatasetSource,
    SampleProvenance,
)
from aarogya_core.types.media_asset import Asset
from aarogya_datasets.fingerprint import compute_fingerprint
from aarogya_datasets.lineage import add_edge, empty_graph
from aarogya_datasets.pipeline import DefaultDatasetPipeline, EventBus
from aarogya_datasets.provenance import ProvenanceStore
from aarogya_datasets.quality import compute_quality
from aarogya_datasets.registry import load_catalog, publish_version
from aarogya_datasets.search import filter_datasets
from aarogya_datasets.statistics import compute_statistics
from aarogya_datasets.storage.local import LocalStorage
from aarogya_datasets.validators import run_validators


@pytest.fixture()
def repo(tmp_path: Path) -> Path:
    (tmp_path / "datasets").mkdir()
    (tmp_path / "datasets" / "registry.yaml").write_text(
        "schema_version: '1.0'\ndatasets: []\n", encoding="utf-8"
    )
    (tmp_path / "datasets" / "versions").mkdir()
    return tmp_path


def test_local_storage_roundtrip(tmp_path: Path) -> None:
    storage = LocalStorage(tmp_path)
    storage.write_text("a/b.txt", "hello")
    assert storage.exists("a/b.txt")
    assert storage.read_text("a/b.txt") == "hello"
    assert any("b.txt" in p for p in storage.list("a"))


def test_events_publish() -> None:
    bus = EventBus()
    seen: list[str] = []
    bus.subscribe(DatasetEventType.LOADED, lambda e: seen.append(e.type.value))
    bus.emit(DatasetEventType.LOADED, dataset_id="DATASET-00001")
    assert seen == ["dataset_loaded"]


def test_validation_not_quality() -> None:
    samples = [
        DatasetSample(
            sample_id="SAMPLE-00001",
            text="ok",
            image=Asset(asset_id="ASSET-00001", uri="x.png"),
        ),
        DatasetSample(
            sample_id="SAMPLE-00001",
            text="dup id",
            image=Asset(asset_id="ASSET-00002", uri="y.png"),
        ),
    ]
    validation = run_validators(samples, dataset_id="DATASET-00001")
    assert validation.passed is False
    quality = compute_quality(samples, dataset_id="DATASET-00001")
    assert quality.overall_score is not None
    # separate report types
    assert type(validation).__name__ == "DatasetValidationReport"
    assert type(quality).__name__ == "DatasetQualityReport"


def test_fingerprint_stable() -> None:
    samples = [
        DatasetSample(sample_id="SAMPLE-00001", text="a"),
        DatasetSample(sample_id="SAMPLE-00002", text="b"),
    ]
    manifest = DatasetManifest(dataset_id="DATASET-00001", samples=samples)
    stats = compute_statistics(samples)
    a = compute_fingerprint(manifest, stats, dataset_id="DATASET-00001")
    b = compute_fingerprint(manifest, stats, dataset_id="DATASET-00001")
    assert a.value == b.value


def test_lineage_edges() -> None:
    g = empty_graph("DATASET-00001")
    g = add_edge(g, "src", "converted", "converted")
    g = add_edge(g, "converted", "published", "published")
    assert len(g.edges) == 2
    assert "src" in g.nodes


def test_provenance_append_only(tmp_path: Path) -> None:
    storage = LocalStorage(tmp_path)
    store = ProvenanceStore(storage, "prov")
    rec = SampleProvenance(
        dataset_id="DATASET-00001",
        sample_id="SAMPLE-00001",
        source="test",
    )
    store.write(rec)
    with pytest.raises(Exception):
        store.write(rec)


def test_search_filters(repo: Path) -> None:
    # seed via pipeline
    pipe = DefaultDatasetPipeline(repo)
    pipe.run(
        DatasetSource(name="s", kind="synthetic"),
        {
            "dataset_id": "DATASET-00001",
            "name": "alpha",
            "task": "HTR",
            "domain": "medical",
            "language": ["en"],
            "license": "research-only",
            "tags": ["demo"],
        },
    )
    records = load_catalog(repo)
    hit = filter_datasets(records, DatasetSearchQuery(task="HTR", language="en"))
    assert len(hit) == 1
    miss = filter_datasets(records, DatasetSearchQuery(task="layout"))
    assert miss == []


def test_pipeline_run_and_immutability(repo: Path) -> None:
    bus = EventBus()
    events: list[str] = []
    bus.subscribe(None, lambda e: events.append(e.type.value))
    pipe = DefaultDatasetPipeline(repo, bus=bus)
    result = pipe.run(
        DatasetSource(name="synthetic", kind="synthetic"),
        {"dataset_id": "DATASET-00001", "version": "v1", "name": "demo"},
    )
    assert result.version_id
    assert result.fingerprint
    assert Path(result.path or "").exists()
    assert "version_published" in events
    catalog = load_catalog(repo)
    assert catalog[0].dataset_id == "DATASET-00001"
    # second publish with same version_id path blocked via allocate new id
    result2 = pipe.run(
        DatasetSource(name="synthetic", kind="synthetic"),
        {"dataset_id": "DATASET-00001", "version": "v2", "name": "demo"},
    )
    assert result2.version_id != result.version_id
    # direct overwrite of same version_id must fail
    from aarogya_core.errors import RegistryError
    from aarogya_core.types.data_platform import (
        DatasetCard,
        DatasetQualityReport,
        DatasetRecord,
        DatasetStatistics,
        DatasetValidationReport,
        DatasetVersion,
    )

    with pytest.raises(RegistryError):
        publish_version(
            repo,
            DatasetRecord(dataset_id="DATASET-00001", name="demo"),
            DatasetVersion(version_id=result.version_id, version="v1"),
            manifest=DatasetManifest(
                dataset_id="DATASET-00001", version_id=result.version_id
            ),
            statistics=DatasetStatistics(),
            validation=DatasetValidationReport(passed=True),
            quality=DatasetQualityReport(),
            card=DatasetCard(dataset_id="DATASET-00001"),
        )


def test_validators_package_separate_from_quality() -> None:
    import aarogya_datasets.quality as q
    import aarogya_datasets.validators as v

    assert v.__name__ != q.__name__
