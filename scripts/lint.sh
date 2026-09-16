#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

pnpm lint

if [[ -d .venv ]]; then
  # shellcheck disable=SC1091
  source .venv/bin/activate
fi

echo "==> Ruff (core + datasets + inference-api)"
ruff check core/aarogya_core datasets/aarogya_datasets services/inference-api/app
