"""Collect failure cases across a run."""

from __future__ import annotations

from aarogya_core.types.evaluation import FailureCase, GroundTruth, Prediction
from aarogya_evaluation.failure.analysis import classify_failure


class ErrorCollector:
    def __init__(self) -> None:
        self.cases: list[FailureCase] = []

    def consider(
        self, ground_truth: GroundTruth, prediction: Prediction
    ) -> FailureCase | None:
        case = classify_failure(ground_truth, prediction)
        if case is not None:
            self.cases.append(case)
        return case

    def summary(self) -> dict[str, int]:
        counts: dict[str, int] = {}
        for case in self.cases:
            counts[case.category] = counts.get(case.category, 0) + 1
        return counts
