"""In-memory catalog search/filter."""

from __future__ import annotations

from aarogya_core.types.data_platform import (
    DatasetRecord,
    DatasetSearchQuery,
    PIIStatus,
)


def filter_datasets(
    records: list[DatasetRecord], query: DatasetSearchQuery
) -> list[DatasetRecord]:
    results: list[DatasetRecord] = []
    for r in records:
        if query.language and query.language not in r.language:
            continue
        if query.license and (r.license or "") != query.license:
            continue
        if query.task and (r.task or "") != query.task:
            continue
        if query.script and query.script not in r.script:
            continue
        if query.domain and (r.domain or "") != query.domain:
            continue
        if query.min_quality is not None:
            score = r.quality_score if r.quality_score is not None else -1.0
            if score < query.min_quality:
                continue
        if query.tags and not set(query.tags).issubset(set(r.tags)):
            continue
        if query.pii_status:
            # check latest version pii if present
            ver = r.versions[-1] if r.versions else None
            status = ver.pii.status if ver and ver.pii else PIIStatus.UNKNOWN
            if status != query.pii_status:
                continue
        if query.name_contains and query.name_contains.lower() not in r.name.lower():
            continue
        results.append(r)
    return results
