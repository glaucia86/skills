# Scope Boundaries

Use this file to prevent scope creep during clarification.
Treat the clarification output as a contract that freezes boundaries before implementation starts.

## In scope
Treat the following as in scope only when directly required:

- the requested change itself
- closely related fixes required for correctness
- small consistency updates necessary to avoid breakage
- tests and documentation directly affected by the change

## Out of scope by default
Treat the following as out of scope unless explicitly approved:

- broad refactors
- unrelated cleanup
- renaming for style only
- architecture redesign
- dependency upgrades not required by the task
- speculative performance improvements
- unrelated test rewrites
- opportunistic file reorganization

## Approval threshold
Explicit approval is required before:

- changing public behavior beyond the request
- modifying architecture significantly
- altering data contracts
- changing auth or security behavior
- introducing new dependencies
- touching multiple domains beyond the original task

## Harness rule
During clarification:

- capture adjacent improvements as deferred work, not as silent scope expansion
- mark uncertain items as questions or investigation tasks, not as implementation assumptions
- prefer the smallest change set that satisfies the request and preserves invariants

## Decision rule
When in doubt:

- prefer narrower scope
- state the possible adjacent improvement
- mark it as deferred unless approved
