"""Text normalization modes for evaluation."""

from aarogya_evaluation.normalization.base import NormalizationMode, normalize_text
from aarogya_evaluation.normalization.medical import normalize_medical
from aarogya_evaluation.normalization.raw import normalize_raw
from aarogya_evaluation.normalization.standard import normalize_standard

__all__ = [
    "NormalizationMode",
    "normalize_medical",
    "normalize_raw",
    "normalize_standard",
    "normalize_text",
]
