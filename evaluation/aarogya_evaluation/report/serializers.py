"""Serialize reports to primitives."""

from __future__ import annotations

from typing import Any

from aarogya_core.types.evaluation import EvaluationReport


def report_to_dict(report: EvaluationReport) -> dict[str, Any]:
    return report.model_dump(mode="json")
