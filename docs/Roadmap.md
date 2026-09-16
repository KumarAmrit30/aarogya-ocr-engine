# Roadmap

## Done (foundation)

- Research Core package + Pipeline stub
- Engine adapter skeletons
- Dataset + experiment/model registries
- Benchmarks / research / lab layout
- FastAPI edge + Next.js research console
- Docker, CI, docs

## Next (research velocity)

1. Dataset loaders + first `DATASET-#####`
2. Wire one engine (likely Paddle) behind interfaces
3. Evaluation metrics (CER/WER) + first eval runner
4. Benchmark suite `handwritten/` comparing stub → real engines
5. OpenAPI → TypeScript codegen (retire manual Zod mirror drift)
6. Experiment runner writing `EXP-#####` records + artifact dirs

## Later

- PARSeq / TrOCR / Qwen2.5-VL / Florence / Document AI adapters
- Distributed training, multi-GPU workers (`gpu-worker` profile)
- MLflow / W&B optional sinks (keep registry IDs primary)
- Medical IE parsers
- Cloud deployment (no architectural rewrite required)

## Explicitly out of scope until needed

Auth/SSO, Kubernetes, fake seed OCR data, customer-facing UI.
