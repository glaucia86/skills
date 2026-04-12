# Ambiguity Checklist

Use this checklist before implementation.

## Repository grounding
- Did you inspect the current code before proposing changes?
- Are the referenced files, modules, symbols, or routes real?
- Are you relying on existing patterns instead of imagined ones?
- Is the current behavior evidenced from the repository or still inferred?

## Product behavior
- Is the intended behavior explicitly defined?
- Is the current behavior known?
- Is this a bug fix or a behavior change?
- Are edge cases specified?

## Inputs and outputs
- Are accepted inputs clearly defined?
- Are expected outputs clearly defined?
- Are invalid inputs addressed?

## Scope
- Is the requested change clearly bounded?
- Are adjacent systems implicitly affected?
- Is cleanup being confused with core scope?
- Does this require a human approval checkpoint before implementation?

## Data and persistence
- Does this change affect stored data?
- Are migrations needed?
- Are backward compatibility concerns present?

## Security and access
- Does this affect authentication or authorization?
- Could this expose sensitive data?
- Are trust boundaries changing?

## Testing and validation
- Is success measurable?
- Are expected test updates obvious?
- Are manual validation scenarios needed?
- Are acceptance criteria concrete enough to verify behavior after implementation?

## Operational concerns
- Does this affect configuration or env vars?
- Does this affect build, deploy, or runtime behavior?
- Does this change observability or error handling?

## Handoff quality
- Could another agent implement from this clarification summary without re-guessing the architecture?
- Does the summary distinguish confirmed facts from inferences and unknowns?
- Is there a clear readiness decision with a reason?

## Decision rule

If any critical ambiguity remains in behavior, scope, security, or validation, do not proceed silently.
Call it out explicitly.
