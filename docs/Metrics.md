# Metrics

All metric math lives in `evaluation/aarogya_evaluation/metrics/`.

## Implemented

| Name | Formula notes |
|------|----------------|
| `cer` | Levenshtein(ref, hyp) / max(len(ref), 1); empty-empty = 0 |
| `wer` | Word-level edit distance / max(#ref_words, 1) |
| `exact_match` | 1 if strings equal else 0 |
| `character_accuracy` | clip(1 − CER, 0, 1) |
| `normalized_cer` | CER after STANDARD norm |
| `normalized_wer` | WER after STANDARD norm |
| `line_accuracy` | Positional exact line matches / max(#lines, 1) |
| `word_accuracy` | Positional exact word matches / max(#words, 1) |
| `page_accuracy` | Exact match of full page text |
| `document_accuracy` | Exact match of full document text |

## Placeholders (`implemented=False`)

medicine/dosage/frequency/duration/route accuracy, entity_f1, precision, recall, f1, calibration, latency, gpu/cpu usage, cost, robustness.

## Registry

```python
from aarogya_evaluation.metrics import list_metrics, create_metric
list_metrics(implemented_only=True)
```
