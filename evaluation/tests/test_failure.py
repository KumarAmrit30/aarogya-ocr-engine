"""Failure analysis tests."""

from aarogya_core.types.evaluation import GroundTruth, Prediction
from aarogya_evaluation.failure import ErrorCollector, classify_failure


def test_exact_match_no_failure() -> None:
    assert classify_failure(GroundTruth(sample_id="1", text="a"), Prediction(sample_id="1", text="a")) is None


def test_empty_prediction() -> None:
    case = classify_failure(GroundTruth(sample_id="1", text="abc"), Prediction(sample_id="1", text=""))
    assert case is not None
    assert case.category == "empty_prediction"


def test_collector() -> None:
    c = ErrorCollector()
    c.consider(GroundTruth(sample_id="1", text="a"), Prediction(sample_id="1", text="b"))
    assert c.summary()["exact_mismatch"] == 1
