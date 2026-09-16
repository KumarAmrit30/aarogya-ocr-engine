# Contributing

## Branch strategy

- `main` — stable foundation
- `feat/*` — infrastructure / features
- `fix/*` — bugfixes
- `research/*` — research-oriented changes that still belong in the monorepo
- Prefer experiment **directories + registry IDs** over long-lived experiment branches

## Commits

[Conventional Commits](https://www.conventionalcommits.org/):

- `feat:`, `fix:`, `docs:`, `chore:`, `refactor:`, `test:`, `ci:`

## Pull requests

Use the PR template. Link `EXP-#####` / `DATASET-#####` / `MODEL-#####` when relevant.

## Recommended labels

`research` · `models` · `datasets` · `engines` · `infra` · `docs` · `bug` · `blocked`

## Rules

1. No OCR/training logic in foundation PRs unless intentional and reviewed.
2. Do not import `lab/` from `core/`, `engines/`, or CI-critical packages.
3. Do not duplicate domain types — extend `aarogya_core.types`.
