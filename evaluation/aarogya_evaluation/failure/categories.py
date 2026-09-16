"""Failure categories — architecture ready for future vision/medical classifiers."""

from enum import StrEnum


class FailureCategory(StrEnum):
    EMPTY_PREDICTION = "empty_prediction"
    EMPTY_REFERENCE = "empty_reference"
    EXACT_MISMATCH = "exact_mismatch"
    LENGTH_DELTA = "length_delta"
    # Future (reserved)
    BLUR = "blur"
    ROTATION = "rotation"
    CUT_OFF = "cut_off"
    WRONG_DRUG = "wrong_drug"
    WRONG_DOSAGE = "wrong_dosage"
    MERGED_WORDS = "merged_words"
    SPLIT_WORDS = "split_words"
    HALLUCINATION = "hallucination"
    MISSING_TEXT = "missing_text"
    FALSE_DETECTION = "false_detection"
    WRONG_READING_ORDER = "wrong_reading_order"
    UNKNOWN = "unknown"
