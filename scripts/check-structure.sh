#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

REQUIRED=(
  apps
  services
  core
  engines
  datasets
  training
  evaluation
  benchmarks
  registry
  research
  lab
  shared
  configs
  scripts
  docker
  docs
  core/aarogya_core/interfaces
  core/aarogya_core/pipeline
  engines/paddle
  datasets/registry.yaml
  registry/README.md
)

missing=0
for path in "${REQUIRED[@]}"; do
  if [[ ! -e "$path" ]]; then
    echo "MISSING: $path"
    missing=1
  fi
done

if [[ "$missing" -ne 0 ]]; then
  echo "Structure check failed"
  exit 1
fi

echo "Structure check OK"
