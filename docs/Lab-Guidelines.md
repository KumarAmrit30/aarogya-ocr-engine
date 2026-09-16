# Lab guidelines

`lab/` is where crazy ideas live.

## Allowed

- One-off notebooks and scripts
- Prototypes that may die
- Personal playgrounds

## Forbidden

- Imports from `core/`, `engines/`, or CI into `lab/`
- Committing large datasets or model weights
- Treating lab code as the source of truth for interfaces

## Graduation path

Prototype in `lab/` → stabilize adapters in `engines/` → keep contracts in `core/` → register experiment/model IDs → document in `research/`.
