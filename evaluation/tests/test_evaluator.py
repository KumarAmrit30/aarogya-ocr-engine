"""EvaluationEngine tests."""

import threading

from aarogya_core.types.evaluation import EvaluationConfig, EvaluationReport, GroundTruth, Prediction
from aarogya_evaluation.engine import EvaluationEngine


def test_evaluate_basic() -> None:
    refs = [GroundTruth(sample_id="1", text="abc"), GroundTruth(sample_id="2", text="xyz")]
    preds = [Prediction(sample_id="1", text="abc"), Prediction(sample_id="2", text="xy")]
    report = EvaluationEngine().evaluate(
        preds, refs, EvaluationConfig(metrics=["cer", "exact_match"]), return_report=True
    )
    assert isinstance(report, EvaluationReport)
    assert report.summary.sample_count == 2
    assert "cer" in report.summary.metrics
    assert len(report.failures) >= 1


def test_cancel() -> None:
    refs = [GroundTruth(sample_id=str(i), text="a") for i in range(20)]
    preds = [Prediction(sample_id=str(i), text="b") for i in range(20)]
    ev = threading.Event()
    ev.set()
    report = EvaluationEngine().evaluate(
        preds, refs, EvaluationConfig(metrics=["cer"]), cancel_event=ev, return_report=True
    )
    assert isinstance(report, EvaluationReport)
    assert report.summary.sample_count == 0
