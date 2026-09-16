# Repository structure

See root `README.md` for the mission. Folder purposes:

| Path | Why it exists |
|------|----------------|
| `apps/web` | Research console |
| `services/inference-api` | HTTP control plane |
| `core/` | Installable Research Core (`aarogya_core`) |
| `engines/` | Per-vendor adapter stubs |
| `datasets/` | Data lake + `registry.yaml` |
| `registry/` | EXP / MODEL / dataset index |
| `training/` | Task-scoped training runners |
| `evaluation/` | Single-run metrics / reports |
| `benchmarks/` | Comparative suites (first-class) |
| `research/` | Institutional memory |
| `lab/` | Exploration without polluting core |
| `configs/` | Declarative knobs |
| `shared/` | TypeScript contract mirrors |
| `scripts/` | Bootstrap / lint / structure checks |
| `docker/` | Dev compose |
| `docs/` | Lab operating system |
| `.github/` | CI + templates |

There is **no** capability-tree `models/` directory. Implementations live in `engines/`; contracts in `core/interfaces/`.
