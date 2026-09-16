# Development guide

## Prerequisites

- Node 20+ (`pnpm` via Corepack)
- Python **3.11–3.12 recommended** (Docker uses 3.12). Local 3.13+ may work for foundation-only deps; pin 3.12 for ML work.
- Docker (optional)

## Bootstrap

```bash
cp .env.example .env
./scripts/bootstrap.sh
source .venv/bin/activate
```

## Common commands

| Command | Purpose |
|---------|---------|
| `make api` | FastAPI reload on :8000 |
| `make web` | Next.js on :3000 |
| `make up` | Docker compose |
| `make lint` / `make typecheck` / `make test` | Quality gates |
| `./scripts/check-structure.sh` | Assert required dirs |

## Adding an engine

See [Engines.md](Engines.md). Copy `engines/_template/`.

## Adding a dataset

1. Allocate `DATASET-#####` via `next_id`.
2. Add entry to `datasets/registry.yaml`.
3. Place raw data under `datasets/raw/<id>/` (gitignored).
4. Add a card under `datasets/cards/`.

## Pre-commit

```bash
pip install pre-commit
pre-commit install
```
