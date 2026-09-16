"""Evaluate endpoint — runs EvaluationEngine on supplied pairs."""

from __future__ import annotations

from fastapi import APIRouter

from aarogya_core.types.evaluation import EvaluationReport
from app.schemas import EvaluateRequest, ReportListResponse
from app.services import EvaluateService

router = APIRouter()
_service = EvaluateService()


@router.post("/evaluate", response_model=EvaluationReport)
def evaluate(request: EvaluateRequest) -> EvaluationReport:
    return _service.run(
        references=request.references,
        predictions=request.predictions,
        config=request.config,
    )


@router.get("/evaluation/reports", response_model=ReportListResponse)
def list_evaluation_reports() -> ReportListResponse:
    return ReportListResponse(reports=_service.list_reports())
