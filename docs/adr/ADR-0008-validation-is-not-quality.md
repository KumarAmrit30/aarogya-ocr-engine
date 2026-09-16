# ADR-0008: Validation is not Quality

- Status: Accepted
- Date: 2026-09-16
- Deciders: Research team

## Context

Structural failures (missing files, duplicate IDs) and research goodness (blur, short text, writer diversity) are often conflated in ML tooling.

## Decision

Forever keep separate packages:

- `aarogya_datasets.validators` → `DatasetValidationReport`
- `aarogya_datasets.quality` → `DatasetQualityReport`

Pipeline runs validators before quality; quality may no-op if validation failed.

## Consequences

- Clear APIs and UI panels
- Independent evolution of vision quality later
- Slightly more types/files — intentional

## Alternatives considered

- Single “dataset health” score — rejected (hides structure vs goodness)
