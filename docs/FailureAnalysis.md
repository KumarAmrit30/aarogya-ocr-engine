# Failure Analysis

Generic classifiers today; category enum reserved for future vision/medical rules.

## Categories (current)

- `empty_prediction`
- `empty_reference`
- `exact_mismatch`
- `length_delta`
- `unknown`

## Reserved (future)

blur, rotation, cut_off, wrong_drug, wrong_dosage, merged/split words, hallucination, missing_text, false_detection, wrong_reading_order.

## API

```python
from aarogya_evaluation.failure import ErrorCollector, classify_failure
```

Failures are attached to `EvaluationReport.failures`.
