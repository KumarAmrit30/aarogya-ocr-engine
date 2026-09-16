"""Generate Dataset Card markdown."""

from __future__ import annotations

from aarogya_core.types.data_platform import (
    DatasetCard,
    DatasetQualityReport,
    DatasetRecord,
    DatasetStatistics,
    DatasetVersion,
)


def generate_card(
    record: DatasetRecord,
    version: DatasetVersion,
    statistics: DatasetStatistics | None = None,
    quality: DatasetQualityReport | None = None,
) -> DatasetCard:
    stats_summary = ""
    if statistics:
        stats_summary = ", ".join(
            f"{k}={v}" for k, v in sorted(statistics.values.items())[:12]
        )
    quality_summary = None
    if quality and quality.overall_score is not None:
        quality_summary = f"overall_score={quality.overall_score:.3f}"
    license_name = record.license or (
        record.license_info.name if record.license_info else "unknown"
    )
    overview = (
        record.notes
        or f"{record.name} registered in the Aarogya Research Data Platform."
    )
    markdown = f"""# Dataset Card: {record.name}

- **dataset_id**: `{record.dataset_id}`
- **version**: `{version.version}` (`{version.version_id}`)
- **license**: {license_name}
- **source**: {record.source or ""}
- **homepage**: {record.homepage or ""}
- **paper**: {record.paper or ""}
- **task**: {record.task or ""}
- **domain**: {record.domain or ""}

## Overview
{overview}

## Statistics
{stats_summary or "_not computed_"}

## Quality
{quality_summary or "_not computed_"}

## Limitations
_TBD_

## Known issues
_None recorded_

## Citation
{record.paper or "_TBD_"}

## Recommended use
Research evaluation and benchmarking only.

## Future improvements
_TBD_
"""
    return DatasetCard(
        dataset_id=record.dataset_id,
        version=version.version,
        overview=overview,
        source=record.source,
        license=record.license,
        paper=record.paper,
        homepage=record.homepage,
        statistics_summary=stats_summary or None,
        quality_summary=quality_summary,
        citation=record.paper,
        recommended_use="Research evaluation and benchmarking only.",
        markdown=markdown,
    )
