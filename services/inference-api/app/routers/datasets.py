"""Dataset catalog + pipeline HTTP endpoints."""

from __future__ import annotations

from fastapi import APIRouter, HTTPException, Query

from aarogya_core.types.data_platform import (
    DatasetPreview,
    DatasetRecord,
    DatasetSearchQuery,
    PIIStatus,
    PublishedVersionResult,
)
from app.schemas import (
    DatasetListResponse,
    DatasetVersionDetailResponse,
    PipelineRunRequest,
)
from app.services import DatasetService

router = APIRouter()
_service = DatasetService()


@router.get("/datasets", response_model=DatasetListResponse)
def list_datasets(
    language: str | None = None,
    license: str | None = Query(default=None, alias="license"),
    task: str | None = None,
    script: str | None = None,
    domain: str | None = None,
    min_quality: float | None = None,
    tags: str | None = Query(default=None, description="Comma-separated tags"),
    pii_status: PIIStatus | None = None,
    name_contains: str | None = None,
) -> DatasetListResponse:
    query = DatasetSearchQuery(
        language=language,
        license=license,
        task=task,
        script=script,
        domain=domain,
        min_quality=min_quality,
        tags=[t.strip() for t in tags.split(",") if t.strip()] if tags else [],
        pii_status=pii_status,
        name_contains=name_contains,
    )
    return DatasetListResponse(datasets=_service.list_datasets(query))


@router.get("/datasets/{dataset_id}", response_model=DatasetRecord)
def get_dataset(dataset_id: str) -> DatasetRecord:
    try:
        return _service.get_dataset(dataset_id)  # type: ignore[arg-type]
    except KeyError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc


@router.get(
    "/datasets/{dataset_id}/versions/{version}",
    response_model=DatasetVersionDetailResponse,
)
def get_dataset_version(dataset_id: str, version: str) -> DatasetVersionDetailResponse:
    try:
        return _service.get_version_detail(dataset_id, version)  # type: ignore[arg-type]
    except KeyError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc


@router.get("/datasets/{dataset_id}/preview", response_model=DatasetPreview)
def get_dataset_preview(
    dataset_id: str,
    version: str | None = None,
    limit: int = Query(default=5, ge=1, le=50),
) -> DatasetPreview:
    try:
        return _service.preview(dataset_id, version=version, limit=limit)  # type: ignore[arg-type]
    except KeyError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc


@router.post("/datasets/pipeline/run", response_model=PublishedVersionResult)
def run_dataset_pipeline(request: PipelineRunRequest) -> PublishedVersionResult:
    """Run DefaultDatasetPipeline on a synthetic/in-memory source (no downloads)."""
    return _service.run_pipeline(request)
