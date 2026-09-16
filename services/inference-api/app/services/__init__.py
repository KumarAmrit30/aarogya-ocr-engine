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


class DatasetService:
    """Catalog search + synthetic DatasetPipeline demos."""

    def list_datasets(self, query: object | None = None) -> list[object]:
        from aarogya_core.config import get_settings
        from aarogya_core.types.data_platform import DatasetSearchQuery
        from aarogya_datasets.registry import load_catalog
        from aarogya_datasets.search import filter_datasets

        records = load_catalog(get_settings().repo_root())
        if query is None:
            return list(records)
        assert isinstance(query, DatasetSearchQuery)
        return list(filter_datasets(records, query))

    def get_dataset(self, dataset_id: str) -> object:
        from aarogya_core.config import get_settings
        from aarogya_datasets.registry import load_catalog

        for record in load_catalog(get_settings().repo_root()):
            if record.dataset_id == dataset_id:
                return record
        raise KeyError(f"Dataset not found: {dataset_id}")

    def get_version_detail(self, dataset_id: str, version: str) -> object:
        import yaml

        from aarogya_core.config import get_settings
        from aarogya_core.types.data_platform import (
            DatasetLineageGraph,
            DatasetQualityReport,
            DatasetStatistics,
            DatasetValidationReport,
        )
        from app.schemas import DatasetVersionDetailResponse

        record = self.get_dataset(dataset_id)
        ver = record.get_version(version)  # type: ignore[union-attr]
        root = get_settings().repo_root()
        validation = quality = statistics = lineage = None
        card_md = None
        if ver.validation_path:
            path = root / ver.validation_path
            if path.exists():
                validation = DatasetValidationReport.model_validate_json(
                    path.read_text()
                )
        if ver.quality_path:
            path = root / ver.quality_path
            if path.exists():
                quality = DatasetQualityReport.model_validate_json(path.read_text())
        if ver.statistics_path:
            path = root / ver.statistics_path
            if path.exists():
                statistics = DatasetStatistics.model_validate_json(path.read_text())
        if ver.lineage_path:
            path = root / ver.lineage_path
            if path.exists():
                lineage = DatasetLineageGraph.model_validate(
                    yaml.safe_load(path.read_text()) or {}
                )
        if ver.card:
            path = root / ver.card
            if path.exists():
                card_md = path.read_text(encoding="utf-8")
        return DatasetVersionDetailResponse(
            dataset=record,  # type: ignore[arg-type]
            version=ver,
            fingerprint=ver.fingerprint,
            validation=validation,
            quality=quality,
            statistics=statistics,
            lineage=lineage,
            card_markdown=card_md,
        )

    def preview(
        self, dataset_id: str, *, version: str | None = None, limit: int = 5
    ) -> object:
        import json

        from aarogya_core.config import get_settings
        from aarogya_core.types.data_platform import DatasetManifest
        from aarogya_datasets.visualization import build_preview

        record = self.get_dataset(dataset_id)
        ver = record.get_version(version)  # type: ignore[union-attr]
        root = get_settings().repo_root()
        samples = []
        if ver.manifest_path:
            path = root / ver.manifest_path
            if path.exists():
                manifest = DatasetManifest.model_validate(json.loads(path.read_text()))
                samples = list(manifest.samples)
        return build_preview(dataset_id, samples, version=ver.version, limit=limit)  # type: ignore[arg-type]

    def run_pipeline(self, request: object) -> object:
        from aarogya_core.config import get_settings
        from aarogya_core.types.data_platform import DatasetSource
        from aarogya_datasets.pipeline import DefaultDatasetPipeline
        from app.schemas import PipelineRunRequest

        assert isinstance(request, PipelineRunRequest)
        root = get_settings().repo_root()
        config = {
            "dataset_id": request.dataset_id,
            "version": request.version,
            "name": request.name,
            "task": request.task,
            "domain": request.domain,
            "language": request.language,
            "license": request.license,
            "tags": request.tags,
            **request.config,
        }
        source = DatasetSource(name=request.name, kind="synthetic")
        return DefaultDatasetPipeline(root).run(source, config)
