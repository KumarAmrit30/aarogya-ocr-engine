"""CER / WER / exact match / accuracy tests."""

from aarogya_core.types.evaluation import GroundTruth, Prediction
from aarogya_evaluation.metrics.cer import CharacterErrorRate
from aarogya_evaluation.metrics.wer import WordErrorRate
from aarogya_evaluation.metrics.exact_match import ExactMatch
from aarogya_evaluation.metrics.character_accuracy import CharacterAccuracy
from aarogya_evaluation.metrics.normalized_cer import NormalizedCER
from aarogya_evaluation.metrics.runner import MetricRunner


def _pair(ref: str, hyp: str, sid: str = "s1") -> tuple[GroundTruth, Prediction]:
    return GroundTruth(sample_id=sid, text=ref), Prediction(sample_id=sid, text=hyp)


def test_cer_identical() -> None:
    gt, pred = _pair("abc", "abc")
    assert CharacterErrorRate().evaluate(gt, pred).value == 0.0


def test_cer_empty_empty() -> None:
    gt, pred = _pair("", "")
    assert CharacterErrorRate().evaluate(gt, pred).value == 0.0


def test_cer_substitution() -> None:
    gt, pred = _pair("kitten", "sitten")
    r = CharacterErrorRate().evaluate(gt, pred)
    assert r.value == 1 / 6


def test_cer_empty_ref() -> None:
    gt, pred = _pair("", "a")
    assert CharacterErrorRate().evaluate(gt, pred).value == 1.0


def test_wer_basic() -> None:
    gt, pred = _pair("a b c", "a x c")
    assert WordErrorRate().evaluate(gt, pred).value == 1 / 3


def test_wer_whitespace() -> None:
    gt, pred = _pair("a  b", "a b")
    # RAW: tokenized differently? "a  b".split() => ["a","b"] same as "a b"
    assert WordErrorRate().evaluate(gt, pred).value == 0.0


def test_exact_match() -> None:
    assert ExactMatch().evaluate(*_pair("Hi", "Hi")).value == 1.0
    assert ExactMatch().evaluate(*_pair("Hi", "hi")).value == 0.0


def test_character_accuracy() -> None:
    gt, pred = _pair("ab", "ab")
    assert CharacterAccuracy().evaluate(gt, pred).value == 1.0


def test_unicode() -> None:
    gt, pred = _pair("नमस्ते", "नमस्ते")
    assert CharacterErrorRate().evaluate(gt, pred).value == 0.0


def test_multiline() -> None:
    gt, pred = _pair("a\nb", "a\nb")
    assert ExactMatch().evaluate(gt, pred).value == 1.0


def test_normalized_cer_via_runner() -> None:
    runner = MetricRunner(names=["normalized_cer"])
    gt = GroundTruth(sample_id="s", text="  Hello   World ")
    pred = Prediction(sample_id="s", text="Hello World")
    results = runner.run_sample(gt, pred)
    assert results[0].value == 0.0
    assert results[0].normalization == "standard"
