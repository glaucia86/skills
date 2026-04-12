# Agent Skills

A collection of agent skills focused on structured engineering workflows for
discovery, implementation, verification, and release readiness.

## Engineering Workflow

These skills help teams run safer end-to-end delivery flows with explicit
Human in the Loop checkpoints and go/no-go gates.

- **review-to-release-workflow** - Run a structured four-phase workflow:
	discovery, implementation, verification, and release-readiness.

	Install this skill directly:

	```bash
	npx skills@latest add glaucia86/skills/review-to-release-workflow
	```

	Or install from this repo by name:

	```bash
	npx skills@latest add glaucia86/skills --skill review-to-release-workflow
	```

## Install All Skills From This Repository

```bash
npx skills@latest add glaucia86/skills
```

## Local Validation

List discoverable skills from a local clone:

```bash
npx skills add ./ --list
```
