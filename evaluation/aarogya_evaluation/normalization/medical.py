"""MEDICAL normalization — placeholder for future Rx-specific rules."""

from __future__ import annotations

from aarogya_core.errors import NotImplementedComponentError
from aarogya_evaluation.normalization.standard import normalize_standard


def normalize_medical(text: str, *, allow_passthrough: bool = True) -> str:
    """
    Future: medicine/abbreviation/dose/entity normalization.

    Until implemented, optionally falls back to STANDARD when allow_passthrough=True.
    """
    if allow_passthrough:
        return normalize_standard(text)
    raise NotImplementedComponentError(
        "MEDICAL normalization is not implemented yet "
        "(medicine, abbreviation, dose, entity rules)."
    )
