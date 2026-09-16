# Aarogya AI Research Platform

Internal **AI Research Platform** powering Aarogya Vault.

This is **not** a product, **not** an application, and **not** a startup landing page.

Today’s primary research track is handwritten prescription OCR / HTR, layout analysis, medical entity extraction, benchmarking, and future vision-language models. The platform is designed so those tracks can expand without architectural rewrites.

## Quick start

```bash
cp .env.example .env
./scripts/bootstrap.sh
source .venv/bin/activate

# Terminal A
make api

# Terminal B
make web
```

- Research console: http://localhost:3000  
- Inference API: http://localhost:8000/docs  
- Health: `GET /api/v1/health`

Or: `make up` (Docker Compose).

## What this repo is for

Does this help us build a better model faster? If no — do not build it.

| Layer | Role |
|-------|------|
| `core/` | Shared types, interfaces, pipelines, registry helpers |
| `engines/` | Vendor/system adapters (Paddle, PARSeq, Qwen, …) |
| `datasets/` + `registry/` | Research Data Platform + stable IDs |
| `benchmarks/` | Comparative suites |
| `research/` + `lab/` | Memory + exploration sandbox |
| `services/inference-api` | Thin HTTP edge |
| `apps/web` | Thin research console |

## Docs

- [Architecture](docs/Architecture.md)
- [Repository structure](docs/Repository-Structure.md)
- [Development guide](docs/Development-Guide.md)
- [API](docs/API.md)
- [Evaluation](docs/Evaluation.md)
- [Metrics](docs/Metrics.md)
- [Benchmarking](docs/Benchmarking.md)
- [Normalization](docs/Normalization.md)
- [Failure analysis](docs/FailureAnalysis.md)
- [Registry](docs/Registry.md)
- [Data Platform](docs/DataPlatform.md)
- [Dataset Pipeline](docs/DatasetPipeline.md)
- [ADRs](docs/adr/README.md)
- [Engines](docs/Engines.md)
- [Lab guidelines](docs/Lab-Guidelines.md)
- [Research principles](docs/Research-Principles.md)
- [Experiment guidelines](docs/Experiment-Guidelines.md)
- [Contributing](docs/Contributing.md)
- [Coding standards](docs/Coding-Standards.md)
- [Roadmap](docs/Roadmap.md)

## License

Proprietary — Aarogya Vault research use.
