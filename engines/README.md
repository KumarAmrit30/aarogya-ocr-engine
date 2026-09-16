# Engines

Vendor/system adapters that implement `aarogya_core.interfaces`.

An engine is a *system* (e.g. PaddleOCR = detector + recognizer + layout + …), not a single model file.

| Engine | Status | Future deps |
|--------|--------|-------------|
| `paddle` | stub | paddlepaddle, paddleocr (future) |
| `parseq` | stub | torch, parseq (future) |
| `trocr` | stub | torch, transformers (future) |
| `qwen` | stub | transformers / vLLM for Qwen2.5-VL (future) |
| `florence` | stub | transformers Florence-2 (future) |
| `gemini` | stub | google-genai (future) |
| `documentai` | stub | google-cloud-documentai (future) |

See `docs/Engines.md` for how to add a new engine. Copy `_template/`.
