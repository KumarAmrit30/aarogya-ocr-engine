"""Failure analysis for evaluation runs."""

from aarogya_evaluation.failure.analysis import classify_failure
from aarogya_evaluation.failure.categories import FailureCategory
from aarogya_evaluation.failure.collector import ErrorCollector

__all__ = ["ErrorCollector", "FailureCategory", "classify_failure"]
