"""Build EvaluationReport objects."""

from __future__ import annotations

from datetime import UTC, datetime
from uuid import uuid4

from aarogya_core.types.evaluation import (
    EvaluationConfig,
    EvaluationReport,
    EvaluationSummary,
    FailureCase,
    SampleEvaluation,
)


class ReportBuilder:
    def build(
        self,
        *,
        config: EvaluationConfig,
        summary: EvaluationSummary,
        samples: list[SampleEvaluation],
        failures: list[FailureCase],
        timing: dict[str, float],
        metadata: dict | None = None,
    ) -> EvaluationReport:
        return EvaluationReport(
            report_id=f"rpt-{uuid4().hex[:12]}",
            created_at=datetime.now(UTC),
            config=config,
            dataset_id=config.dataset_id,
            dataset_version=config.dataset_version,
            pipeline_id=config.pipeline_id,
            experiment_id=config.experiment_id,
            summary=summary,
            failures=failures,
            samples=samples,
            timing=timing,
            metadata=metadata or {},
        )
