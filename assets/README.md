# Assets

Concrete research artifacts that are **not** logical models.

| Path | Purpose |
|------|---------|
| `checkpoints/` | Training checkpoints |
| `tokenizers/` | Tokenizer files |
| `vocabularies/` | Vocab files |
| `lexicons/` | Lexicons / dictionaries |
| `prompts/` | Prompt templates for VLMs |
| `templates/` | Document / output templates |
| `weights/` | Raw weight dumps |
| `exports/` | ONNX, TensorRT, quantized exports |
| `registry.yaml` | Authoritative `ASSET-#####` catalog |

**Models vs assets:** `MODEL-#####` is a logical trained/external model identity.
`ASSET-#####` is a concrete file (or file set) a model or pipeline consumes.

See `docs/Registry.md` and `docs/adr/ADR-0006-assets-registry-separate-from-models.md`.
