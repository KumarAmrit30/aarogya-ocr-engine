"""Built-in statistics analyzers."""

from __future__ import annotations

from collections import Counter

from aarogya_core.types.data_platform import DatasetSample
from aarogya_datasets.statistics.registry import register_stat


@register_stat
class SampleCountStat:
    name = "sample_count"

    def compute(self, samples: list[DatasetSample]) -> dict[str, float | int | str]:
        return {"sample_count": len(samples)}


@register_stat
class TextLengthStat:
    name = "text_length"

    def compute(self, samples: list[DatasetSample]) -> dict[str, float | int | str]:
        lengths = [len(s.text) for s in samples]
        if not lengths:
            return {
                "avg_text_length": 0,
                "min_text_length": 0,
                "max_text_length": 0,
                "total_chars": 0,
            }
        return {
            "avg_text_length": sum(lengths) / len(lengths),
            "min_text_length": min(lengths),
            "max_text_length": max(lengths),
            "total_chars": sum(lengths),
        }


@register_stat
class WordCountStat:
    name = "word_count"

    def compute(self, samples: list[DatasetSample]) -> dict[str, float | int | str]:
        total = sum(len(s.words) if s.words else len(s.text.split()) for s in samples)
        return {"total_words": total}


@register_stat
class VocabularyStat:
    name = "vocabulary"

    def compute(self, samples: list[DatasetSample]) -> dict[str, float | int | str]:
        vocab: set[str] = set()
        for s in samples:
            vocab.update(s.words or s.text.split())
        return {"vocabulary_size": len(vocab)}


@register_stat
class EmptyRatioStat:
    name = "empty_ratio"

    def compute(self, samples: list[DatasetSample]) -> dict[str, float | int | str]:
        if not samples:
            return {"empty_sample_ratio": 0.0}
        empty = sum(1 for s in samples if not s.text.strip())
        return {"empty_sample_ratio": empty / len(samples)}


@register_stat
class DuplicateTextStat:
    name = "duplicate_ratio"

    def compute(self, samples: list[DatasetSample]) -> dict[str, float | int | str]:
        if not samples:
            return {"duplicate_ratio": 0.0}
        counts = Counter(s.text for s in samples)
        dups = sum(c - 1 for c in counts.values() if c > 1)
        return {"duplicate_ratio": dups / len(samples)}


@register_stat
class WriterCountStat:
    name = "writer_count"

    def compute(self, samples: list[DatasetSample]) -> dict[str, float | int | str]:
        writers = {s.writer_id for s in samples if s.writer_id}
        return {"writer_count": len(writers)}


@register_stat
class LanguageDistStat:
    name = "language_distribution"

    def compute(self, samples: list[DatasetSample]) -> dict[str, float | int | str]:
        return {}  # distributions filled in engine

    def distribution(self, samples: list[DatasetSample]) -> dict[str, int]:
        c: Counter[str] = Counter(s.language or "unknown" for s in samples)
        return dict(c)
