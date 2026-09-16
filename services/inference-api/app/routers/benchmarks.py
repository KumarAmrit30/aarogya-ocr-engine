"""Benchmarks listing endpoint."""

from __future__ import annotations

from fastapi import APIRouter

from app.schemas import BenchmarkListResponse
from app.services import BenchmarkService

router = APIRouter()
_service = BenchmarkService()


@router.get("/benchmarks", response_model=BenchmarkListResponse)
def list_benchmarks() -> BenchmarkListResponse:
    return BenchmarkListResponse(suites=_service.list_suites())
