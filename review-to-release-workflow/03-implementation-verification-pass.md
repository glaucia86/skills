---
name: implementation-verification-pass
description: Perform a post-implementation verification pass to validate that approved changes were implemented correctly, consistently, and safely, then generate VERIFICATION.md.
version: 1.0.0
phase: verification
requires:
  - QUESTIONS.md
  - IMPLEMENTATION_NOTES.md
produces: VERIFICATION.md
next: release-readiness-pass
---

# Implementation Verification Pass

## Purpose

Use this skill after implementation has already been completed.

The goal is to verify that recent changes:

1. align with the decisions clarified in `QUESTIONS.md`
2. were implemented correctly and consistently
3. did not introduce regressions, scope creep, or architectural drift
4. updated tests, docs, and related modules where necessary
5. left the codebase in a stable and maintainable state

This skill is about verification, not new feature work.

---

## Position in the workflow

This is **Phase 3 — Verification**.

### Required inputs
- `QUESTIONS.md`
- `IMPLEMENTATION_NOTES.md`

### Produces
- `VERIFICATION.md`

### Recommended next skill
- `release-readiness-pass`

### Do not proceed automatically if
- implementation is incomplete
- key decisions are still blocked
- verification cannot be done with confidence due to missing artifacts

Confidence means:
- `IMPLEMENTATION_NOTES.md` exists and matches the implemented changes
- changed files and directly adjacent integration points are reviewable
- build/test signals required for the target release are available

---

## Core mindset

Act as:

- a principal engineer doing a final technical review
- a tech lead validating execution quality
- a guardian of consistency, safety, and scope discipline

Review what changed.  
Check whether it matches intent.  
Validate whether it is complete enough.  
Identify residual risk or regression.

---

## Verification goals

This skill must verify:

### 1. Decision alignment
Did implementation honor approved answers?

### 2. Technical correctness
Do the changes look correct and coherent?

### 3. Scope discipline
Did implementation avoid unnecessary drift?

### 4. Regression risk
Did the changes introduce fragility or hidden breakage?

### 5. Project hygiene
Were tests, docs, types, validation, and related files updated appropriately?

---

## Execution process

### 1. Reconstruct intended outcomes
Read `QUESTIONS.md` and infer:

- confirmed bugs
- intended behaviors
- approved improvements
- deferred items
- blocked areas

### 2. Identify the implementation surface
Review changed files and adjacent areas that may be indirectly affected.

### 3. Verify change-by-change alignment
Ask for each significant change:

- does it trace back to an approved decision?
- is behavior consistent with clarified intent?
- was anything left partial?
- was any deferred item changed accidentally?

### 3a. Verify deferred boundaries explicitly
For each item tagged `[DEFERRED]` in `QUESTIONS.md`, confirm it was not changed during implementation.
If a deferred item was changed without explicit approval, classify it as `Must Fix`.

### 4. Review technical quality
Inspect for:

- correctness
- consistency with architecture
- naming quality
- duplication
- broken invariants
- missing validation
- brittle logic
- weak error handling
- hidden coupling

### 5. Verify tests
Check whether tests were:

- added or updated when needed
- aligned with clarified behavior
- broad enough to reduce regression risk

### 6. Verify documentation
Check whether relevant docs, comments, setup guides, examples, or env files were updated where needed.

### 7. Check for regression and integration risk
Look beyond changed files and assess cross-module consistency and stale leftovers.

### 8. Classify findings
Use categories such as:

- `verified`
- `partial`
- `blocked`
- `caveat`
- `out-of-scope`

Severity guidance for findings:

### Must Fix
Use when a finding should block progression, including:
- mismatch with approved decisions in `QUESTIONS.md`
- correctness regressions, broken invariants, or high-risk error handling gaps
- security-impacting mistakes
- accidental changes in deferred or out-of-scope areas

### Should Fix
Use when the issue is non-blocking but important, including:
- maintainability or consistency concerns with low immediate risk
- missing or weak tests outside the critical path
- documentation drift that does not invalidate behavior

### Acceptable / Noted
Use when the concern is explicitly deferred, out-of-scope, or a documented known limitation.

---

## Output

Create:

`VERIFICATION.md`

Suggested structure:

# Verification Report

## Summary
What was reviewed and the overall result.

## Verified Areas
- ...

## Findings

### Must Fix
- ...

### Should Fix
- ...

### Acceptable / Noted
- ...

## Alignment with QUESTIONS.md
- what was implemented correctly
- what was partial
- what remained untouched appropriately
- what exceeded scope

## Tests Review
- what was covered
- what is missing

## Documentation Review
- what was updated
- what remains stale

## Status Summary
- `verified`
- `partial`
- `blocked`
- `caveat`
- `out-of-scope`

## Recommended Next Steps
- ...

---

## Quality bar

A good verification pass:

- confirms implementation truly matches approved decisions
- detects regressions and inconsistencies
- distinguishes partial from complete work
- leaves a clear factual record of remaining risk

A weak pass only restates what changed and ignores decision alignment, tests, docs, and indirect regressions.

---

## Constraints

Do not:

- start a broad new refactor
- confuse new ideas with verification findings
- mark work correct without checking related areas

Do:

- verify against clarified intent
- inspect integration points
- classify severity clearly
- use evidence, not speculation

---

## Handoff to next phase

This skill ends when `VERIFICATION.md` is complete.

### Recommended next step
Run `release-readiness-pass` to determine whether the project is actually ready for merge, handoff, staging, or production.

### Stop condition
If `VERIFICATION.md` contains unresolved must-fix findings, do not mark the project as ready for release.