"""Registry helper tests."""

from pathlib import Path

import pytest

from aarogya_core.errors import RegistryError
from aarogya_core.registry import next_id, write_experiment
from aarogya_core.types.dataset import DatasetRecord
from aarogya_core.types.experiment import Experiment


def test_next_id_empty() -> None:
    assert next_id("EXP", []) == "EXP-00001"


def test_next_id_increments() -> None:
    assert next_id("DATASET", ["DATASET-00001", "DATASET-00003"]) == "DATASET-00004"


def test_next_id_asset_pipeline() -> None:
    assert next_id("ASSET", []) == "ASSET-00001"
    assert next_id("PIPELINE", ["PIPELINE-00001"]) == "PIPELINE-00002"


def test_dataset_default_version() -> None:
    record = DatasetRecord(dataset_id="DATASET-00001", name="demo", path="datasets/raw/x")
    assert len(record.versions) == 1
    assert record.versions[0].version == "v1"
    assert record.get_version().path == "datasets/raw/x"


def test_write_experiment_immutable(tmp_path: Path) -> None:
    exp = Experiment(experiment_id="EXP-00001", name="first")
    write_experiment(tmp_path, exp)
    with pytest.raises(RegistryError, match="immutable"):
        write_experiment(tmp_path, Experiment(experiment_id="EXP-00001", name="again"))
