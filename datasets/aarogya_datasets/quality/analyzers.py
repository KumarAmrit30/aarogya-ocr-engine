"""Quality analyzers (goodness) + vision placeholders."""

from __future__ import annotations

from aarogya_core.types.data_platform import DatasetQualityIssue, DatasetSample
from aarogya_datasets.quality.registry import register_quality


@register_quality
class ShortAnnotationQuality:
    name = "short_annotations"

    def analyze(
        self, samples: list[DatasetSample]
    ) -> tuple[list[DatasetQualityIssue], dict[str, float]]:
        issues: list[DatasetQualityIssue] = []
        short = 0
        for s in samples:
            if 0 < len(s.text) < 3:
                short += 1
                issues.append(
                    DatasetQualityIssue(
                        code="short_annotation",
                        message="Very short annotation",
                        sample_id=str(s.sample_id),
                    )
                )
        ratio = short / len(samples) if samples else 0.0
        return issues, {"short_annotation_ratio": ratio}


@register_quality
class DuplicateTextQuality:
    name = "duplicate_text_quality"

    def analyze(
        self, samples: list[DatasetSample]
    ) -> tuple[list[DatasetQualityIssue], dict[str, float]]:
        from collections import Counter

        counts = Counter(s.text for s in samples if s.text)
        issues = [
            DatasetQualityIssue(
                code="duplicate_text",
                message=f"Duplicate text appears {c} times",
                severity="info",
            )
            for t, c in counts.items()
            if c > 1
        ]
        ratio = (
            sum(c - 1 for c in counts.values() if c > 1) / len(samples)
            if samples
            else 0.0
        )
        return issues, {"quality_duplicate_ratio": ratio}


@register_quality
class WriterDiversityQuality:
    name = "writer_diversity"

    def analyze(
        self, samples: list[DatasetSample]
    ) -> tuple[list[DatasetQualityIssue], dict[str, float]]:
        writers = {s.writer_id for s in samples if s.writer_id}
        score = min(1.0, len(writers) / max(len(samples), 1) * 10) if writers else 0.0
        issues: list[DatasetQualityIssue] = []
        if samples and not writers:
            issues.append(
                DatasetQualityIssue(
                    code="missing_writer_ids",
                    message="No writer_id metadata — diversity unknown",
                    severity="info",
                )
            )
        return issues, {"writer_diversity_score": score}


def _make_placeholder(name: str) -> type:
    class _Placeholder:
        def analyze(
            self, samples: list[DatasetSample]
        ) -> tuple[list[DatasetQualityIssue], dict[str, float]]:
            return [], {name: -1.0}  # -1 => not computed

    _Placeholder.name = name  # type: ignore[attr-defined]
    _Placeholder.__name__ = "".join(p.capitalize() for p in name.split("_"))
    return register_quality(_Placeholder)


for _n in (
    "blur_score",
    "noise_score",
    "rotation",
    "contrast",
    "illumination",
    "compression",
    "motion_blur",
):
    _make_placeholder(_n)
