# Normalization

Applied before metric computation (per metric `required_normalization`, overridable globally).

| Mode | Behavior |
|------|----------|
| `raw` | Identity — case and whitespace sensitive |
| `standard` | Unicode NFKC, trim, collapse whitespace |
| `medical` | Placeholder — currently passthrough to STANDARD |

```python
from aarogya_evaluation.normalization import normalize_text
normalize_text("  A  B ", "standard")  # "A B"
```
