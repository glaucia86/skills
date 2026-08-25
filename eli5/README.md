# eli5

[![Install](https://img.shields.io/badge/install-npx%20skills-0f766e)](https://skills.sh/)
[![Category](https://img.shields.io/badge/category-learning-111827)](#what-this-skill-does)
[![Output](https://img.shields.io/badge/output-standalone%20html-1f2937)](#output)

A visual-first explainer skill that turns complex topics into beginner-friendly,
self-contained HTML pages with simple language, clear flow, and big visuals.

## Why this skill exists

Many explanations are either accurate but dense, or simple but misleading.
This skill is designed to keep both clarity and truth by constraining the
explanation into a small visual story.

## What this skill does

When triggered, the skill guides the agent to:

1. identify the one core idea to teach
2. choose a familiar analogy
3. map the analogy to real terms
4. explain the causal flow in three to six scenes
5. produce a single standalone HTML artifact

## Output

Primary output:

- one self-contained HTML file named using the topic slug

The HTML output should:

- embed CSS and JavaScript locally
- avoid external dependencies
- remain readable on mobile and desktop
- include accessible structure and reduced-motion support

## When to use

Use this skill when the user asks for:

- explain like I am five
- beginner visual explanation
- simple visual teaching page
- intuitive understanding before technical depth

## When not to use

Do not use this skill when the user needs:

- a deep technical tutorial
- code-only implementation details
- an exhaustive reference document

## How to use

Example prompt:

```text
Use eli5 to explain how DNS works. Create a single HTML file with a visual analogy and very little text.
```

Expected outcome:

- a compact visual page that a beginner can understand in one scan

## File structure

```text
eli5/
  SKILL.md
  README.md
  evals/
    evals.json
```

## Evals

This skill includes eval prompts in `evals/evals.json` covering:

- correct ELI5 flow and beginner framing
- standalone HTML output requirements
- refusal to oversimplify into false claims
- avoidance of unnecessary jargon

---

[← Back to skills catalog](../README.md)
