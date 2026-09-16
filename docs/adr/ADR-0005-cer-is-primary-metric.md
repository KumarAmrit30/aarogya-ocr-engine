# ADR-0005: CER is the primary metric

- Status: Accepted
- Date: 2026-09-16
- Deciders: Research team

## Context

OCR/HTR research needs one default scalar for ranking while still tracking WER, exact match, and future medical field metrics.

## Decision

**Character Error Rate (CER)** is the primary metric for default evaluation and benchmark configs. Other metrics are secondary unless a study explicitly declares otherwise.

## Consequences

- Default `EvaluationConfig.metrics` starts with `cer`.
- Leaderboards sort by CER ascending unless configured otherwise.
- Medical entity metrics will be added later without demoting CER for transcription studies.

## Alternatives considered

- WER-primary — useful but less sensitive for short medical tokens.
- Exact match only — too coarse for handwriting research.
