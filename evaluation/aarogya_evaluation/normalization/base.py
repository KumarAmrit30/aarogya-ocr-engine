"""Normalization mode enum and dispatcher."""

from __future__ import annotations

from enum import StrEnum

from aarogya_core.errors import NotImplementedComponentError


class NormalizationMode(StrEnum):
    RAW = "raw"
    STANDARD = "standard"
    MEDICAL = "medical"


def normalize_text(text: str, mode: str | NormalizationMode) -> str:
    """Apply the requested normalization mode."""
    from aarogya_evaluation.normalization.medical import normalize_medical
    from aarogya_evaluation.normalization.raw import normalize_raw
    from aarogya_evaluation.normalization.standard import normalize_standard

    mode = NormalizationMode(str(mode).lower())
    if mode is NormalizationMode.RAW:
        return normalize_raw(text)
    if mode is NormalizationMode.STANDARD:
        return normalize_standard(text)
    if mode is NormalizationMode.MEDICAL:
        return normalize_medical(text)
    raise NotImplementedComponentError(f"Unknown normalization mode: {mode}")
