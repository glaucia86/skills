# implementation-readiness-gate

[![Install](https://img.shields.io/badge/install-npx%20skills-0f766e)](https://skills.sh/)
[![Harness role](https://img.shields.io/badge/role-gate-111827)](#what-this-skill-does)
[![Language](https://img.shields.io/badge/language-agnostic-1f2937)](#language-agnostic)

A final pre-implementation gate that consolidates the current evidence and
returns one explicit execution decision: `go`, `go-with-caveats`, or `no-go`.

## Why this skill exists

Even after clarification and contract review, teams still need one simple answer:

- can we start coding now?
- can we start only with caveats?
- or should we stop and tighten the artifacts first?

This skill exists to make that decision explicit and evidence-based.

## What this skill does

The skill reviews one or both of:

- a clarification artifact
- a contract review verdict

and returns one final gate decision:

- `go`
- `go-with-caveats`
- `no-go`

It does not create the artifact and it does not review the artifact in depth
from scratch. It consolidates what already exists into an execution decision.

## Language agnostic

This skill is language-agnostic.

It only cares whether the artifacts are strong enough, bounded enough, and tied
to real repository validation mechanisms.

## When to use

Use this skill when:

- clarification is complete
- contract review is complete or intentionally skipped
- you want one explicit pre-implementation decision

## What To Do Next

After running this skill, follow the gate decision literally.

- If the decision is `go`, implementation can begin using the existing artifacts
  as execution context.
- If the decision is `go-with-caveats`, implementation can begin only within the
  named caveats, limits, and follow-up obligations.
- If the decision is `no-go`, do not start coding. Strengthen clarification,
  contract review, or user decisions first.

For important tasks, keep the gate output with the other planning artifacts so
future agent runs can see why implementation was allowed or blocked.

## How to use

Example request:

```text
Use implementation-readiness-gate on this Clarification Summary and contract review result. Give me one decision only: go, go-with-caveats, or no-go, with the blockers or caveats made explicit.
```

## Relationship to the other harness skills

This skill is usually the last step in the trio:

1. `task-clarification-harness`
2. `implementation-contract-review-harness`
3. `implementation-readiness-gate`

That order is recommended when you want maximum pre-implementation control.
If needed, this gate can still run with only the clarification artifact, but it
should lower confidence and say what evidence is missing.

## File structure

```text
implementation-readiness-gate/
  SKILL.md
  README.md
  gate-checklist.md
  gate-output-template.md
  example-gate-decision.md
  evals/
    evals.json
```

## Evals

This skill includes eval prompts in `evals/evals.json` covering:

- clean `go` decisions
- refusal to override weak review evidence
- operating with partial input artifacts
- handling contradictory artifacts
