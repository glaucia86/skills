---
name: task-clarification-harness
description: Build a pre-implementation harness for ambiguous or risky coding tasks by grounding the request in the repository, producing a structured impact map, surfacing ambiguities and risks, defining scope boundaries, and creating a validation-ready implementation contract before any code changes are made. Use when a task is broad, underspecified, cross-cutting, or likely to drift without an explicit planning checkpoint.
---

# Task Clarification Harness

## Purpose

Use this skill before implementation when the task may be underspecified, risky, broad, or likely to affect multiple parts of the system.

The goal is to prevent premature coding by forcing a structured, repository-grounded clarification pass first.

This skill helps the agent:

- restate the task clearly
- inspect the codebase before assuming implementation details
- identify ambiguities and missing decisions
- map impacted files, modules, symbols, or systems
- surface technical and product risks
- define scope boundaries
- create an implementation contract with validation steps before making changes

This is a pre-implementation harness.
It exists to improve correctness, reduce scope drift, and make execution safer by turning vague requests into a constrained engineering artifact.

---

## Required behavior

Before making any code changes, the agent must complete a clarification pass.

The agent must:

1. restate the task in concrete terms
2. inspect the repository when it is available
3. identify ambiguities or unanswered questions
4. identify likely impacted areas
5. assess risks and assumptions
6. define scope boundaries
7. define an implementation contract
8. define how success will be validated

Do not implement before this pass is complete.

---

## Workflow files

This skill relies on the following files in the same folder:

- `ambiguity-checklist.md`
- `scope-boundaries.md`
- `output-template.md`
- `references/harness-patterns.md`
- `references/validation-linking-criteria.md`
- `references/contract-review-handoff-template.md`
- `references/example-clarification-summary.md`

Read and apply them during the clarification pass.

If you write the clarification summary to disk, validate it with:

- `python scripts/validate_clarification_summary.py <path-to-summary.md>`

---

## Clarification workflow

### Step 1 - Restate the task

Rewrite the request in operational language.

Capture:

- what is being asked
- what kind of change this is
- whether it is a bug fix, enhancement, refactor, migration, cleanup, or investigation
- what appears in scope
- what appears intentionally out of scope

Do not repeat the user loosely.
Translate the request into engineering intent.

---

### Step 2 - Ground the task in the repository

Inspect the repository before making implementation claims when repository access is available.

Look for:

- real file paths
- real symbols, modules, routes, or services
- existing patterns to follow
- current behavior relevant to the request
- nearby tests, docs, config, or observability hooks

Separate:

- confirmed facts from repository inspection
- likely inferences
- unknowns that still need clarification

Do not invent file paths, APIs, or architectural patterns.

If the repository cannot yet support a safe conclusion, prefer `needs-codebase-investigation`.

---

### Step 3 - Check for ambiguity

Read `ambiguity-checklist.md`.

Look for ambiguity in:

- product behavior
- expected inputs and outputs
- edge cases
- authorization or security expectations
- data handling
- UX or API behavior
- backward compatibility
- deployment or environment assumptions
- acceptance criteria

If important ambiguity exists, explicitly call it out.

---

### Step 4 - Map impact surface

Identify what parts of the system are likely affected.

Include where relevant:

- files
- modules
- services
- routes
- UI surfaces
- data models
- tests
- config
- docs
- CI/CD or runtime assumptions

Do not claim certainty when still inferring.
Mark inferred impact as likely, possible, or unclear.

---

### Step 5 - Assess risks and invariants

Identify execution risks such as:

- regression risk
- hidden coupling
- unclear invariants
- missing tests
- auth/security exposure
- performance implications
- data migration concerns
- scope creep risk
- architecture drift

Be specific.
Name the risk and why it matters.

Also capture important invariants such as:

- API or UI behavior that must remain stable
- data contracts that must not break
- security boundaries that must not weaken
- performance or operational expectations that must hold

---

### Step 6 - Define scope boundaries

Read `scope-boundaries.md`.

State clearly:

- what should be changed
- what should not be changed
- what would require explicit approval
- what adjacent improvements should be deferred

Do not treat nearby cleanup as automatically in scope.

---

### Step 7 - Define the implementation contract

Turn the clarification pass into a concrete handoff artifact.

Include:

- the files, modules, or symbols that are most likely to change
- the existing patterns or references to follow
- the acceptance criteria or expected outcomes
- the approval-required edges that must not be crossed silently
- the evidence level for each major claim: confirmed, inferred, or unknown

The contract should narrow the solution space enough that implementation becomes targeted instead of exploratory.

If the contract is important enough to gate implementation, hand it to the sister skill `implementation-contract-review-harness` for a second-pass review before coding.

Use the handoff shape in `references/contract-review-handoff-template.md`.

If both the clarification artifact and the contract review verdict exist, an optional final gate can be run with `implementation-readiness-gate` before implementation starts.

---

### Step 8 - Define validation plan

Before implementation, define how success will be checked.

Read `references/validation-linking-criteria.md`.

Include likely checks such as:

- lint
- typecheck
- unit tests
- integration tests
- manual scenario validation
- smoke tests
- API contract checks
- behavior comparison
- documentation review

Do not say "done" without a validation path.

Choose checks that are actually supported by the repository. Prefer repository-native commands over generic placeholders.

Use these selection rules:

- if the repository exposes scripts or task runners such as `package.json`, `Makefile`, `justfile`, `Taskfile.yml`, `tox.ini`, or `noxfile.py`, prefer those entry points
- if CI workflows already define validation commands, prefer the same commands or the same command family
- if typed languages or frameworks expose built-in validators, include them explicitly
- if no deterministic check exists for a risk you identified, call that out and add the smallest practical manual validation scenario
- if a full suite is expensive, propose the narrowest credible subset for pre-implementation confidence

Never list `lint`, `typecheck`, or `tests` unless you can point to the repository mechanism that would run them or explicitly mark them unavailable.

---

## Output

Before implementation, produce a structured clarification summary using the template in `output-template.md`.

Treat this summary as the harness artifact that sits between request intake and implementation.

The output must include:

- task restatement
- task classification
- repository-grounded evidence
- key ambiguities
- likely impacted areas
- risks
- scope boundaries
- implementation contract
- validation plan
- readiness decision

When the summary is persisted to disk, run the validator script and fix any reported structural issues before treating the artifact as complete.

---

## Readiness decision

At the end of the clarification pass, return exactly one of:

- `ready-for-implementation`
- `needs-user-clarification`
- `needs-codebase-investigation`
- `not-safe-to-proceed`

Use:

### `ready-for-implementation`
when the task is clear enough and the likely impact is understood.

### `needs-user-clarification`
when important product or behavioral decisions are missing.

### `needs-codebase-investigation`
when more repository inspection is needed before safe implementation.

### `not-safe-to-proceed`
when the task is too ambiguous, risky, or underspecified to execute responsibly.

---

## Constraints

Do not:

- start implementing before clarifying
- silently assume intended behavior
- invent repository facts
- hide ambiguity behind confident language
- expand scope through cleanup impulses
- claim readiness without a validation strategy

Do:

- reduce ambiguity
- ground claims in the real codebase when possible
- make assumptions visible
- separate known facts from inferences
- define boundaries clearly
- create a constrained handoff artifact before implementation
- make execution safer before code changes begin

---

## Operating mindset

Act as:

- a senior engineer clarifying execution before coding
- a technical lead reducing delivery risk
- a harness layer that improves agent reliability through structure, evidence, and checkpoints

Clarify first.
Then implement only if justified.
