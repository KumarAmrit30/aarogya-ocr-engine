"""Statistics engine — auto-discovers registered analyzers."""

from __future__ import annotations

from aarogya_core.types.data_platform import DatasetSample, DatasetStatistics
from aarogya_datasets.statistics import analyzers  # noqa: F401
from aarogya_datasets.statistics.registry import get_stat, list_stats


def compute_statistics(samples: list[DatasetSample]) -> DatasetStatistics:
    values: dict[str, float | int | str] = {}
    distributions: dict[str, dict[str, float | int]] = {}
    for name in list_stats():
        analyzer = get_stat(name)
        values.update(analyzer.compute(samples))
        if hasattr(analyzer, "distribution"):
            distributions[name] = analyzer.distribution(samples)  # type: ignore[attr-defined]
    values["pages"] = len(samples)
    return DatasetStatistics(values=values, distributions=distributions)
