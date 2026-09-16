"""Metric registry / factory tests."""

import aarogya_evaluation.metrics  # noqa: F401 — register
from aarogya_evaluation.metrics.factory import create_metric, create_metrics
from aarogya_evaluation.metrics.registry import list_metrics


def test_cer_registered() -> None:
    assert "cer" in list_metrics(implemented_only=True)


def test_placeholders_listed() -> None:
    all_names = list_metrics(implemented_only=False)
    assert "medicine_accuracy" in all_names
    assert "medicine_accuracy" not in list_metrics(implemented_only=True)


def test_factory_create() -> None:
    m = create_metric("cer")
    assert m.name == "cer"
    coll = create_metrics(["cer", "wer"])
    assert coll.names == ["cer", "wer"]
