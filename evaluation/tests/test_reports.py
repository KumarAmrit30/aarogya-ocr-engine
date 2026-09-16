"""Report export tests."""

from pathlib import Path

from aarogya_core.types.evaluation import EvaluationConfig, GroundTruth, Prediction
from aarogya_evaluation.engine import EvaluationEngine
from aarogya_evaluation.report.exporters import export_console, export_report


def test_export_formats(tmp_path: Path) -> None:
    report = EvaluationEngine().evaluate(
        [Prediction(sample_id="1", text="a")],
        [GroundTruth(sample_id="1", text="a")],
        EvaluationConfig(metrics=["cer"]),
        return_report=True,
    )
    written = export_report(report, tmp_path)  # type: ignore[arg-type]
    assert "json" in written and written["json"].exists()
    assert "csv" in written and written["csv"].exists()
    assert "markdown" in written and written["markdown"].exists()
    text = export_console(report)  # type: ignore[arg-type]
    assert "cer" in text
