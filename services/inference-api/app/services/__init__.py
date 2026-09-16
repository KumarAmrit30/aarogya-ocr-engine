"""Service layer — thin wrappers over Research Core / evaluation."""

from __future__ import annotations

from pathlib import Path

from aarogya_core.pipeline import StubOCRPipeline, compose_pipeline
from aarogya_core.types.evaluation import (
    EvaluationConfig,
    EvaluationReport,
    GroundTruth,
    Prediction,
)
from aarogya_core.types.ocr import OCRRequest, OCRResult
from aarogya_evaluation.engine import EvaluationEngine
from app.schemas import PlaceholderResponse


class OCRService:
    """Delegates to core Pipeline stub — no OCR logic."""

    def __init__(self) -> None:
        self._pipeline = StubOCRPipeline()

    def run(self, request: OCRRequest) -> OCRResult:
        pipeline = compose_pipeline(engine_id=request.engine_id or "stub")
        return pipeline.run(request)


class TrainService:
    def run(self, *_args: object, **_kwargs: object) -> PlaceholderResponse:
        return PlaceholderResponse(
            message="Training endpoint is a placeholder. Implement TrainingRunner next."
        )


class EvaluateService:
    """Runs the model-agnostic EvaluationEngine on supplied GT/prediction pairs."""

    def __init__(self) -> None:
        self._engine = EvaluationEngine()

    def run(
        self,
        *,
        references: list[GroundTruth],
        predictions: list[Prediction],
        config: EvaluationConfig | None = None,
    ) -> EvaluationReport:
        report = self._engine.evaluate(
            predictions,
            references,
            config or EvaluationConfig(),
            return_report=True,
        )
        assert isinstance(report, EvaluationReport)
        return report

    def list_reports(self, report_dir: Path | None = None) -> list[dict[str, str]]:
        from aarogya_core.config import get_settings

        directory = report_dir or (
            get_settings().repo_root() / "evaluation" / "reports"
        )
        if not directory.exists():
            return []
        items: list[dict[str, str]] = []
        for path in sorted(directory.glob("*.json")):
            items.append({"report_id": path.stem, "path": str(path)})
        return items


class BenchmarkService:
    def list_suites(self) -> list[dict[str, str]]:
        """List suite folders under benchmarks/ (metadata only; no fake scores)."""
        from aarogya_core.config import get_settings

        root = get_settings().repo_root() / "benchmarks"
        suites: list[dict[str, str]] = []
        for path in sorted(root.iterdir()):
            if path.is_dir() and path.name not in {
                "aarogya_benchmarks",
                "tests",
                "__pycache__",
            }:
                suites.append({"suite": path.name, "status": "configured"})
        return suites


class ModelService:
    def list_models(self) -> list[object]:
        return []
