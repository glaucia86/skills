# Harness Patterns

Use this reference to place the task-clarification harness inside a broader harness-engineering model.

The clarification skill is primarily a feedforward guide.
It helps the agent start from a narrower and more explicit problem statement before implementation.

## Guides vs sensors

Guides steer the agent before it acts.
Sensors observe the result after or around the action and create pressure to self-correct.

Both can be computational or inferential.

## Common guide patterns

### Inferential guides
- `AGENTS.md` and repository instructions
- skills with reusable workflows
- architecture principles and coding conventions
- implementation contracts and accepted boundaries
- product or behavior specifications

### Computational guides
- bootstrap scripts
- codemods
- project generators
- repository-aware helper scripts
- fixed repository command entry points such as a project verify task or a CI-aligned check command

## Common sensor patterns

### Computational sensors
- linters
- typecheckers
- unit tests
- integration tests
- structural or architecture tests
- contract tests
- build checks
- generated-file consistency checks

### Inferential sensors
- AI review passes
- implementation contract review
- semantic diff review
- UX or API behavior review
- documentation consistency review

## How this skill fits

`task-clarification-harness` should produce a strong guide artifact:

- a repository-grounded task restatement
- explicit ambiguities
- impacted areas
- risks and invariants
- scope boundaries
- an implementation contract
- a validation plan

That artifact becomes stronger when paired with sensors such as:

- a deterministic validator for the clarification summary structure
- a second-pass contract review before implementation
- repository-native lint, typecheck, test, and build checks after implementation

## Design rule

Whenever the agent makes a repeated mistake, ask which layer should absorb the lesson:

- guide: add or refine instruction before the action
- sensor: add or refine feedback after the action
- both: when the issue is common and costly

## Anti-patterns

Avoid these failure modes:

- using the clarification summary as a loose narrative instead of a contract
- listing generic validation steps with no repository grounding
- treating a guide as sufficient when no sensor can detect failure
- creating sensors that are too expensive or too noisy to run regularly
- encoding too much irrelevant context into the skill body instead of references
