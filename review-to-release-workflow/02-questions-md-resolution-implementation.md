---
name: questions-md-resolution-implementation
description: Read an answered QUESTIONS.md file, convert clarified decisions into a scoped implementation plan, apply approved changes safely, and generate IMPLEMENTATION_NOTES.md.
version: 1.0.0
phase: implementation
requires: QUESTIONS.md
produces: IMPLEMENTATION_NOTES.md
next: implementation-verification-pass
---

# QUESTIONS.md Resolution and Implementation

## Purpose

Use this skill after a prior discovery pass has generated a `QUESTIONS.md` file and the project owner has answered it.

The goal is to:

1. read the answered `QUESTIONS.md`
2. extract confirmed decisions and constraints
3. transform answers into an implementation strategy
4. apply approved improvements safely
5. generate `IMPLEMENTATION_NOTES.md`

This skill exists to ensure implementation is based on clarified intent, not guesswork.

---

## Position in the workflow

This is **Phase 2 — Implementation**.

### Required input
- `QUESTIONS.md` with answers

### Produces
- `IMPLEMENTATION_NOTES.md`
- approved code changes
- optionally updated tests/docs

### Recommended next skill
- `implementation-verification-pass`

### Do not proceed automatically if
- `QUESTIONS.md` is unanswered
- answers are contradictory or too vague
- major blockers remain unresolved

---

## Preconditions

Before implementation begins, validate each answered question using the decision tags defined in `QUESTIONS.md`:

- `[INTENDED]`
- `[BUG]`
- `[APPROVED]`
- `[DEFERRED]`
- `[OUT-OF-SCOPE]`
- `[BLOCKED]`

Intake checks:

- every relevant question has one explicit tag and one concrete inline answer
- no answer uses conflicting tags
- no answer is vague or non-committal for in-scope items
- blockers are explicitly explained

Tag semantics for execution:

- `[DEFERRED]`: known item intentionally postponed; no implementation in this run
- `[BLOCKED]`: cannot proceed due to missing information or external dependency

Stop and request clarification if 2 or more relevant questions are unclear, contradictory, or untagged.

If safe classification is not possible, do not guess.

---

## Core mindset

Act as:

- a staff/principal engineer
- a tech lead responsible for safe execution
- a steward translating decisions into code changes

Your job is to respect the answers, preserve scope boundaries, and implement only what was actually approved.

Understand first.  
Plan second.  
Implement third.  
Verify fourth.

---

## Execution process

### 1. Read and normalize the answers
Read `QUESTIONS.md` carefully and determine for each answered item:

- which explicit decision tag applies
- what the user confirmed
- whether current behavior is intentional or a bug
- whether change is requested now
- whether the item is in scope
- whether constraints exist

### 2. Build a decision map
Map each answered question into an execution outcome:

- no change required
- small targeted fix
- refactor
- behavioral change
- security hardening
- performance improvement
- test improvement
- documentation update
- deferred
- blocked

### 3. Derive an implementation plan
Group approved work into buckets such as:

- correctness fixes
- bug fixes
- architecture cleanup
- security improvements
- performance improvements
- validation and resilience
- testing
- documentation

Sequence work in a low-risk order.

### 4. Human checkpoint: approve the plan before coding
Present the decision map and implementation plan to the user and request explicit approval.

Include:

- what will change now
- what will remain deferred
- what is blocked and why

Do not apply code changes until the user approves the scoped plan.

### 5. Respect scope boundaries
Do not redesign unrelated parts of the system.

Only change what is:

- explicitly approved
- strongly implied by approved decisions
- necessary to complete an approved fix safely
- required to preserve consistency

### 6. Implement systematically
Apply changes area by area while preserving architecture, naming consistency, and intended behavior.

Avoid overengineering.

### 7. Update tests
When behavior changes or bugs are fixed, update or add tests where feasible and valuable.

### 8. Validate consistency
Ensure implementation matches clarified intent and did not accidentally change deferred or out-of-scope areas.

---

## Output

Create:

`IMPLEMENTATION_NOTES.md`

Suggested structure:

# Implementation Notes

## Summary
What was implemented and why.

## Decision Mapping
For each major answered question:
- decision tag (`[INTENDED]`, `[BUG]`, `[APPROVED]`, `[DEFERRED]`, `[OUT-OF-SCOPE]`, `[BLOCKED]`)
- action taken
- status (`verified`, `partial`, `blocked`, `deferred`, `out-of-scope`, `caveat`)

## Applied Changes
- ...

## Tests Updated
- ...

## Docs Updated
- ...

## Deferred Items
- ...

## Blocked Items
- ...

For each blocked item, include:
- blocker reason
- what information or dependency is missing
- recommended unblock action

---

## Implementation guidelines

- prioritize correctness over elegance
- keep changes explainable
- avoid hidden scope creep
- preserve intended behavior unless change was explicitly approved
- improve docs when clarified decisions should be captured

---

## Quality bar

A good implementation pass:

- faithfully reflects `QUESTIONS.md` answers
- avoids speculative refactors
- improves code quality without destabilizing the system
- leaves a clear record of what changed and why

A weak pass ignores answers, introduces assumptions, and expands scope unnecessarily.

---

## Constraints

Do not:

- invent requirements
- silently override intended behavior
- refactor unrelated areas
- interpret vague answers as approval for broad changes

Do:

- implement only confirmed work
- preserve out-of-scope boundaries
- document blocked items clearly
- keep answer-to-change traceability

---

## Handoff to next phase

This skill ends when approved changes are applied and `IMPLEMENTATION_NOTES.md` is complete.

### Recommended next step
Run `implementation-verification-pass` to validate correctness, consistency, and regression risk.

### Stop condition
If 2 or more relevant items remain `blocked`, or any blocked item affects the approved critical path, do not claim implementation is complete.