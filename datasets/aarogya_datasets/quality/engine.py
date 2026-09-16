"""Quality engine — separate from validators."""

from __future__ import annotations

from aarogya_core.types.data_platform import DatasetQualityReport, DatasetSample
from aarogya_core.types.ids import DatasetId, VersionId
from aarogya_datasets.quality import analyzers  # noqa: F401
from aarogya_datasets.quality.registry import get_quality, list_quality


def compute_quality(
    samples: list[DatasetSample],
    *,
    dataset_id: DatasetId | None = None,
    version_id: VersionId | None = None,
) -> DatasetQualityReport:
    issues = []
    metrics: dict[str, float] = {}
    for name in list_quality():
        analyzer = get_quality(name)
        iss, mets = analyzer.analyze(samples)
        issues.extend(iss)
        metrics.update(mets)
    # overall: average of non-placeholder (>=0) metrics inverted where higher is worse
    usable = [v for k, v in metrics.items() if v >= 0 and "ratio" in k]
    if usable:
        # lower ratios better → score = 1 - mean(ratios)
        overall = max(0.0, min(1.0, 1.0 - (sum(usable) / len(usable))))
    else:
        diversity = metrics.get("writer_diversity_score", 0.5)
        overall = float(diversity) if diversity >= 0 else 0.5
    return DatasetQualityReport(
        dataset_id=dataset_id,
        version_id=version_id,
        overall_score=overall,
        issues=issues,
        metrics=metrics,
    )
