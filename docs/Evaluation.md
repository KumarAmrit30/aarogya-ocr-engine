# Evaluation

Model-agnostic **Research Evaluation Engine** — single source of truth for metrics.

## Purpose

Score `GroundTruth` vs `Prediction` without knowing which OCR/VLM engine produced the prediction.

## Architecture

```text
Prediction + GroundTruth
        ↓
  Normalization (per metric)
        ↓
  Metric registry (auto-discovered)
        ↓
  EvaluationEngine
        ↓
  EvaluationReport (JSON / CSV / Markdown / console)
```

Package: `aarogya_evaluation` under [`evaluation/`](../evaluation/).

## Extension

1. Add `evaluation/aarogya_evaluation/metrics/my_metric.py`
2. Decorate with `@register_metric`
3. Import the module from `metrics/__init__.py`
4. No evaluator changes required

## Example

```python
from aarogya_core.types.evaluation import EvaluationConfig, GroundTruth, Prediction
from aarogya_evaluation.engine import EvaluationEngine

report = EvaluationEngine().evaluate(
    [Prediction(sample_id="1", text="hello")],
    [GroundTruth(sample_id="1", text="hello")],
    EvaluationConfig(metrics=["cer", "wer"]),
)
```

## Related ADRs

- ADR-0001 evaluation model-agnostic
- ADR-0005 CER primary metric
