#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

echo "==> Installing pnpm workspace dependencies"
pnpm install

echo "==> Creating Python virtualenv (.venv)"
if [[ ! -d .venv ]]; then
  python3 -m venv .venv
fi
# shellcheck disable=SC1091
source .venv/bin/activate

echo "==> Installing aarogya-core (editable)"
pip install -e "./core[dev]"

echo "==> Installing inference-api (editable)"
pip install -e "./services/inference-api[dev]"

echo "==> Bootstrap complete"
echo "Activate venv: source .venv/bin/activate"
echo "API: make api   | Web: make web   | Stack: make up"
