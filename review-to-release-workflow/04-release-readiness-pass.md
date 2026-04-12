---
name: release-readiness-pass
description: Perform a final release-readiness review to determine whether the project is ready for merge, handoff, staging, or production, then generate RELEASE_READINESS.md.
version: 1.0.0
phase: release-readiness
requires:
  - QUESTIONS.md
  - IMPLEMENTATION_NOTES.md
  - VERIFICATION.md
produces: RELEASE_READINESS.md
next: none
---

# Release Readiness Pass

## Purpose

Use this skill after implementation and verification are complete.

The goal is to determine whether the project is genuinely ready for:

- merge
- handoff
- staging deployment
- production deployment
- demo delivery
- external release

This skill evaluates not only code correctness, but also operational, configurational, deployment, documentation, and rollout readiness.

---

## Position in the workflow

This is **Phase 4 — Release Readiness**.

### Required inputs
- `QUESTIONS.md`
- `IMPLEMENTATION_NOTES.md`
- `VERIFICATION.md`

### Produces
- `RELEASE_READINESS.md`

### Final phase
This is the final skill in the sequence.

### Do not proceed automatically if
- verification still contains must-fix items
- major blockers remain unresolved
- the release target cannot be confirmed or reasonably inferred

---

## Core mindset

Act as:

- a senior/staff engineer doing a release gate review
- a tech lead checking shipment risk
- an engineering owner validating operational readiness

Your question is not whether the code is elegant.  
Your question is whether the project is safe and ready enough to ship.

---

## Primary question

At the end, answer explicitly:

- **Ready**
- **Ready with caveats**
- **Not ready**

Do not avoid making the call.

---

## Readiness dimensions

Assess readiness across:

### 1. Build and execution readiness
Can the project be built, started, and exercised reliably?

### 2. Configuration readiness
Are env vars, config files, defaults, and secret handling safe and complete?

### 3. Test and validation readiness
Is there enough validation to ship with confidence?

### 4. Deployment readiness
Are deployment workflows, runtime assumptions, and infrastructure dependencies understood?

### 5. Operational readiness
Can the system be observed, debugged, and supported if something goes wrong?

### 6. Documentation and handoff readiness
Can another engineer run, review, or maintain it?

### 7. Product and release risk
Are known limitations and sharp edges communicated appropriately?

---

## Execution process

### 1. Confirm the intended release target
Use the release target confirmed before Phase 1. If missing, infer the most likely target and mark the uncertainty as a caveat.

Target options:

- local demo
- internal prototype
- team handoff
- staging
- production
- open-source release

State the target explicitly in the report and evaluate readiness against that target.

### 2. Review build and runtime entrypoints
Check:

- install flow
- scripts
- startup assumptions
- runtime dependencies
- dev/prod command clarity

### 3. Review environment and configuration safety
Check:

- required env vars
- `.env.example`
- insecure defaults
- secret handling
- config validation
- production-only assumptions

### 4. Review build quality gates
Check whether lint, typecheck, tests, build, and other gates are present and meaningful.

### 5. Review deployment and infrastructure assumptions
Inspect CI/CD, deployment scripts, containers, infra config, migration ordering, secret injection, and rollback implications.

### 6. Review observability and failure handling
Assess logs, error visibility, health checks, traceability, and silent failure risks.

### 7. Review test posture relative to release target
Ask whether the current level of testing is sufficient for the intended release target.

### 8. Review docs and handoff quality
Check whether docs are sufficient for setup, maintenance, deployment, and troubleshooting.

### 9. Review open risks and caveats
Classify unresolved concerns as:

- blocker
- caveat
- known limitation

### 10. Make the final verdict
Return:

- **Ready**
- **Ready with caveats**
- **Not ready**

Tie the verdict to evidence.
If evidence is insufficient to make a confident call, default to **Not ready** and list the missing evidence.

---

## Output

Create:

`RELEASE_READINESS.md`

Suggested structure:

# Release Readiness Report

## Release Target Assumption
State the assumed target.

## Final Verdict
**Ready / Ready with caveats / Not ready**

## Summary
Overall readiness summary.

## Readiness by Dimension

### Build and Runtime
- ...

### Configuration and Environment
- ...

### Quality Gates
- ...

### Deployment and Infrastructure
- ...

### Observability and Operations
- ...

### Tests and Validation
- ...

### Documentation and Handoff
- ...

## Blockers
- ...

## Caveats
- ...

## Known Limitations
- ...

## Recommended Actions Before Release
- ...

## Recommended Actions After Release
- ...

---

## Severity guidance

### Blocker
A condition that should prevent merge, deployment, or handoff for the intended release target.

### Caveat
A non-blocking issue that should be acknowledged before release.

### Known limitation
A deliberate or accepted limitation that should be documented.

Use workflow status labels when useful:
- `verified`
- `partial`
- `blocked`
- `deferred`
- `out-of-scope`
- `caveat`

---

## Quality bar

A good readiness pass:

- makes a clear ship/no-ship recommendation
- distinguishes blockers from caveats
- evaluates readiness relative to the real release target
- surfaces practical risks, not only code-style concerns

A weak readiness pass avoids a verdict and ignores docs, env, deployment, or operational reality.

---

## Constraints

Do not:

- confuse “build passes” with “release ready”
- mark a project ready without checking config/docs/deploy implications
- raise theoretical concerns unsupported by evidence

Do:

- judge readiness relative to the release target
- call out blockers clearly
- separate caveats from true blockers
- make the final verdict explicit

---

## End of workflow

This is the last skill in the sequence.

If the verdict is:

- **Ready** → project may proceed to merge, handoff, or release
- **Ready with caveats** → proceed only with caveats acknowledged
- **Not ready** → return to implementation or verification for corrective work