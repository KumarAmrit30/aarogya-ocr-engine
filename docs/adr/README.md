# Architecture Decision Records (ADRs)

ADRs capture **why** a decision was made—not how to implement it.

## Process

1. Copy the template below into `ADR-NNNN-short-title.md`
2. Status: Proposed → Accepted → Deprecated / Superseded
3. Never rewrite history; supersede with a new ADR

## Template

```markdown
# ADR-NNNN: Title

- Status: Accepted
- Date: YYYY-MM-DD
- Deciders: Research team

## Context

## Decision

## Consequences

## Alternatives considered
```

## Index

| ADR | Title |
|-----|-------|
| 0001 | Evaluation is model-agnostic |
| 0002 | Pipelines are registry-driven |
| 0003 | Datasets are versioned (and scientifically immutable) |
| 0004 | Experiments are immutable |
| 0005 | CER is the primary metric |
| 0006 | Assets registry separate from models |
