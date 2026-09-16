"""Generic failure classifiers (no vision / medical NLP yet)."""

from __future__ import annotations

from aarogya_core.types.evaluation import FailureCase, GroundTruth, Prediction
from aarogya_evaluation.failure.categories import FailureCategory


def classify_failure(
    ground_truth: GroundTruth, prediction: Prediction
) -> FailureCase | None:
    """Return a FailureCase when texts differ; None on exact match."""
    ref = ground_truth.text
    hyp = prediction.text
    if ref == hyp:
        return None
    if hyp == "" and ref != "":
        category = FailureCategory.EMPTY_PREDICTION
    elif ref == "" and hyp != "":
        category = FailureCategory.EMPTY_REFERENCE
    elif abs(len(ref) - len(hyp)) > max(len(ref), 1) * 0.5:
        category = FailureCategory.LENGTH_DELTA
    else:
        category = FailureCategory.EXACT_MISMATCH
    return FailureCase(
        sample_id=ground_truth.sample_id,
        category=category.value,
        reference=ref,
        prediction=hyp,
        notes="generic classifier",
    )
