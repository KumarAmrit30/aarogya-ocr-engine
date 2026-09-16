# Roadmap

## Done — Phase 1 (Foundation)

- Research Core, engines stubs, registries, lab/research, API, web console, Docker/CI/docs

## Done — Phase 2 (Research Evaluation Engine)

- Evaluation domain types + Metric Protocol
- Pluggable metrics (CER/WER/…) + placeholders
- Normalization (RAW/STANDARD/MEDICAL stub)
- EvaluationEngine, failure analysis, report exporters
- Benchmarks keyed by pipeline × dataset version
- Assets registry, pipeline registry, dataset versions, immutable experiments
- ADRs 0001–0006
- API `/evaluate`, `/evaluation/reports`, `/benchmarks` + UI wiring

## Done — Phase 3 (Research Data Platform)

- `aarogya-datasets` package + `DatasetPipeline` orchestrator + EventBus
- `StorageBackend` / `LocalStorage`, Asset-based samples
- Validators ≠ quality, statistics, cards, PII metadata, provenance, lineage, fingerprints
- Catalog search filters + Dataset Explorer UI + `POST /datasets/pipeline/run` (synthetic)
- Docs + ADRs 0007–0009 + tests/CI install

## Phase 4 (next)

1. First real `pipeline.run` on a public dataset with one real converter + LocalStorage
2. First real engine adapter emitting `Prediction`s
3. Register a real `PIPELINE-#####` and run handwritten suite
4. OpenAPI → TypeScript codegen
5. MEDICAL normalization + medicine field metrics

## Later

Distributed benches, MLflow/W&B sinks, cloud storage backends, Document AI baseline studies (with ADRs).

## Phase 3 self-review

1. Pipeline orchestrator like OCR? **Yes** (`DefaultDatasetPipeline`)
2. Evaluation independent of RDP internals? **Yes** (ADR-0007)
3. Validation ≠ quality? **Yes** (separate packages + ADR-0008)
4. Asset-based samples? **Yes**
5. Lineage + provenance + fingerprints? **Yes**
6. Search filter contract? **Yes** (in-memory)
7. No downloads/OCR/real converters? **Yes**
8. Debt: event bus in-process only; converter stubs; vision quality placeholders; linear catalog filter
9. Phase 4: real converter + first public dataset ingest
