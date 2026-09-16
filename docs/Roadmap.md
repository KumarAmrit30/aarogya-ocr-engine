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

## Phase 3 (next)

1. Dataset loaders for `DATASET-#####@vN`
2. First real engine adapter emitting `Prediction`s
3. Register a real `PIPELINE-#####` and run handwritten suite
4. OpenAPI → TypeScript codegen
5. MEDICAL normalization + medicine field metrics

## Later

Distributed benches, MLflow/W&B sinks, cloud deploy, Document AI baseline studies (with ADRs).

## Phase 2 self-review

1. Model-agnostic? **Yes**
2. Engines plug in without eval changes? **Yes**
3. New metrics without evaluator edits? **Yes** (`@register_metric`)
4. Medical metrics later? **Placeholders + MEDICAL mode ready**
5. Scale to hundreds of experiments? **Immutable EXP dirs + IDs**
6. Duplication? **Avoided** (metrics only in evaluation/)
7. Over-engineered? **No ML deps; sequential benches**
8. Three-year fit? **Pipelines + versions + ADRs**
9. Debt: MEDICAL empty; TS mirror drift; no parallel benches yet
10. Phase 3: loaders + first pipeline with real engines
