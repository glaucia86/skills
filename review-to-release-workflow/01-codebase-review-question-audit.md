---
name: codebase-review-question-audit
description: Perform a deep structured review of the codebase, identify ambiguities, risks, and missing decisions, and generate a QUESTIONS.md file to clarify architecture, behavior, security, performance, and refactoring concerns before implementation.
version: 1.0.0
phase: discovery
produces: QUESTIONS.md
next: questions-md-resolution-implementation
---

# Codebase Review Question Audit

## Purpose

Use this skill to perform a deep, structured review of a project before implementation or refactoring begins.

The purpose is to understand the codebase holistically and generate a `QUESTIONS.md` file containing all relevant technical, architectural, behavioral, product, security, and maintainability questions that should be answered before making broad changes.

This skill is designed for discovery, not implementation.

---

## Position in the workflow

This is **Phase 1 — Discovery** of the review-to-release workflow.

### Inputs
This skill expects access to the codebase and any supporting project documentation.

### Produces
- `QUESTIONS.md`

### Recommended next skill
- `questions-md-resolution-implementation`

### Do not proceed automatically if
- `QUESTIONS.md` still needs human answers
- major ambiguities remain unresolved
- the user wants to review the questions first

---

## When to use

Use this skill when the user asks to:

- review the whole codebase
- identify odd patterns, unclear decisions, or risks
- prepare questions before refactoring
- understand the architecture before making changes
- perform a discovery pass as a tech lead or staff engineer

Do not use this skill when the user explicitly wants direct implementation without a discovery phase.

---

## Core mindset

Act as:

- a professional code reviewer
- a staff/principal engineer
- a tech lead performing technical discovery

Your job is to understand first, question second, and change later.

If something looks unclear, risky, inconsistent, incomplete, or surprising, turn it into a question.

Do not assume intent when the code is ambiguous.

---

## Review scope

Review the project as broadly and deeply as possible, including where applicable:

- folder and module structure
- architecture and boundaries
- framework conventions
- dependency choices
- environment variable usage
- build and deployment assumptions
- pages, routes, screens, and layouts
- API endpoints and handlers
- domain modeling and business logic
- persistence and data access
- authentication and authorization
- validation and error handling
- async flows and retries
- performance hotspots and caching
- observability and logging
- tests and coverage strategy
- duplication, dead code, and naming consistency
- security flaws
- missing docs and implicit decisions

---

## Execution process

### 1. Understand the system first
Infer internally:

- what the project appears to do
- who the likely users are
- what the critical flows are
- what the stack and architectural center are
- what seems mature versus unfinished

### 2. Review the codebase systematically
Inspect the repository area by area and identify:

- ambiguity
- weak boundaries
- fragile logic
- missing invariants
- hidden assumptions
- missing validation
- missing tests
- security concerns
- product behavior ambiguity
- performance risks
- under-documented decisions

### 3. Convert findings into questions
Every relevant concern must be phrased as a question, not as a refactor prescription.

Good:
- “Should this endpoint be authenticated, or is open access intentional?”

Avoid:
- “Refactor this into a service.”

### 4. Group questions by area
Organize questions into sections such as:

- Product & Intended Behavior
- Architecture
- Code Structure & Boundaries
- API Design
- Data & Persistence
- Security
- Performance
- Error Handling & Resilience
- Testing & QA
- Observability
- Documentation
- Technical Debt / Suspicious Areas
- Possible Bugs
- Missing Decisions / Open Design Gaps

### 5. Make each question independently answerable
Each question should be:

- specific
- contextualized
- self-contained
- easy to answer directly

Include when useful:

- file path
- symbol or module name
- why the question matters
- risk if unanswered

### 6. Be exhaustive
Do not optimize for brevity. Optimize for completeness and clarity.

---

## Output

Create:

`QUESTIONS.md`

Suggested structure:

# QUESTIONS.md

## Project Understanding Summary
Brief summary of what the system appears to do, how it seems structured, and what high-risk areas were identified.

## How to Answer
Require the project owner to answer each question inline, directly below the question block.

For every answer, require one decision tag:
- `[INTENDED]` current behavior is intentional and should remain unchanged
- `[BUG]` current behavior is incorrect and should be fixed now
- `[APPROVED]` improvement approved for implementation in this workflow run
- `[DEFERRED]` valid improvement, intentionally postponed for a later cycle
- `[OUT-OF-SCOPE]` not part of this project or this workflow run
- `[BLOCKED]` cannot decide yet due to missing information or external dependency

Require clear, concrete answers. Vague responses such as "maybe" or "decide later" are unresolved and block Phase 2.

Example answer format:

```markdown
#### Q3. Should this endpoint require authentication?
- **Where:** `src/api/orders.ts`
- **Why this matters:** exposed write operations without auth can cause data abuse
- **Question:** Should this endpoint be authenticated, or is open access intentional?
- **Answer:** [APPROVED] Require authentication using the existing middleware in `src/auth/jwt.ts`.
```

## Questions

### 1. Product & Intended Behavior
#### Q1. ...
- **Where:** `...`
- **Why this matters:** ...
- **Question:** ...

### 2. Architecture
#### Q2. ...
- **Where:** `...`
- **Why this matters:** ...
- **Question:** ...

Continue until all relevant questions are captured.

## Suggested answer tags
Use these tags consistently in answers:
- `[INTENDED]`
- `[BUG]`
- `[APPROVED]`
- `[DEFERRED]`
- `[OUT-OF-SCOPE]`
- `[BLOCKED]`

---

## Quality bar

A strong `QUESTIONS.md`:

- reveals ambiguity before implementation
- creates a real decision backlog
- exposes risky assumptions
- improves the quality of future refactors
- reduces the chance of changing the wrong thing

A weak `QUESTIONS.md` is shallow, generic, and misses behavior/security/performance/design risks.

---

## Constraints

Do not:

- change code automatically
- assume intended behavior silently
- jump into implementation
- collapse multiple concerns into vague notes

Do:

- inspect broadly
- question precisely
- anchor questions in evidence
- prefer clarity over politeness

---

## Handoff to next phase

This skill ends when `QUESTIONS.md` is complete.

### Recommended next step
Run `questions-md-resolution-implementation` **only after** the project owner has answered `QUESTIONS.md`.

### Stop condition
If `QUESTIONS.md` is unanswered, incomplete, or contains unclear decisions (missing tags, contradictory tags, or vague answers), do not continue to implementation.