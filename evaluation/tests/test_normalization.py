"""Normalization tests."""

from aarogya_evaluation.normalization import normalize_raw, normalize_standard, normalize_text


def test_raw_identity() -> None:
    assert normalize_raw("  Ab  C  ") == "  Ab  C  "


def test_standard_trim_collapse_unicode() -> None:
    # NFKC: ﬁ -> fi
    assert normalize_standard("  hello   world  ") == "hello world"
    assert "fi" in normalize_standard("ﬁ")


def test_normalize_text_dispatcher() -> None:
    assert normalize_text(" A  B ", "standard") == "A B"
    assert normalize_text(" A  B ", "raw") == " A  B "
