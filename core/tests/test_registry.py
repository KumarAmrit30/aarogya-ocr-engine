"""Registry helper tests."""

from aarogya_core.registry import next_id


def test_next_id_empty() -> None:
    assert next_id("EXP", []) == "EXP-00001"


def test_next_id_increments() -> None:
    assert next_id("DATASET", ["DATASET-00001", "DATASET-00003"]) == "DATASET-00004"
