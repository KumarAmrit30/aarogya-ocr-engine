# Coding standards

## TypeScript

- `strict: true`
- Prefer Zod for runtime validation at API boundaries
- Keep the research UI minimal — no marketing, no animations

## Python

- Ruff + Black + isort + mypy (strict in `core`)
- Protocols in `core/interfaces/`; implementations in `engines/`
- No hardcoded absolute paths — use `aarogya_core.config`

## Logging

JSON structured logs with `request_id` / `experiment_id` / `run_id` / `config_hash` / `engine_id` when available.

## Formatting

EditorConfig at repo root. Prettier for TS/JSON/MD. Black line length 100.
