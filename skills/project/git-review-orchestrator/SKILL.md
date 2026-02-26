---
name: git-review-orchestrator
description: Orchestrate a deterministic, gated git review workflow in Plan Mode only. Use when users ask for git review, pre-release review, quality gate checks, or review + tests + formatter/linter + changelog + readme + version bump preparation. Routes to all relevant installed skills/rules/agents by framework and file type, reviews the current git diff by default, and explicitly forbids automatic git commit.
---

# Git Review Orchestrator

## Overview
Run a fail-fast quality pipeline on the current repository diff with strict gate ordering.
Operate only in Plan Mode and never run `git commit` automatically.

## Hard Rules
- Always run this skill in Plan Mode.
- Never run `git commit` automatically.
- Default review scope is current git diff: staged, unstaged, and untracked files.
- Use all relevant installed skills/rules/agents; do not invoke unrelated skills.
- Stop at first failed gate and report downstream gates as `not_run`.

## Workflow
1. Detect scope and stack from changed files.
2. Run review gate using relevant skills/rules/agents.
3. If review passes, run all available tests.
4. If tests pass, run formatter/linter when available.
5. If all previous gates pass, run changelog/readme update workflow and version bump planning.
6. Return a deterministic report with findings, gate matrix, and planned release-doc/version actions.

## 0) Scope and Stack Detection (required)
- Collect current working-tree evidence with:
  - `git status --short`
  - `git diff --name-only`
  - `git diff --cached --name-only`
- Build a changed-file map and classify by context:
  - Angular: `angular.json`, `src/app/**`, Angular package/config files.
  - NestJS: `nest-cli.json`, `src/**/*.module.ts`, `@nestjs/*` usage.
  - TypeScript Node: `tsconfig*.json`, Node build/test scripts, `src/**/*.ts` non-Angular/Nest contexts.
  - Docs-only: markdown and docs files without runtime code changes.

## 1) Relevant Skill Routing (required)
Select all relevant skills/rules/agents from installed inventory:
- Always include review mindset and repository rules.
- Include framework-specific skills when matching files are detected.
- Include document skills for docs-only or docs-touching changes:
  - `changelog-keepachangelog-update`
  - `readme-updater`
- Exclude skills unrelated to changed stack/file types.

Routing examples:
- Angular app changes -> relevant Angular skills.
- NestJS backend changes -> relevant NestJS skills.
- TypeScript tooling/build changes -> relevant TypeScript skills.
- Docs-only changes -> documentation skills only.

## 2) Gate A: Review (required)
Review changed code/config/docs with this rubric:
- Bugs and behavioral regressions
- Security/privacy/configuration risks
- Performance and reliability risks
- Missing or insufficient tests
- Contract/API/schema compatibility concerns
- Documentation drift and release-note impact

Review gate pass criteria:
- No blocking/high-severity findings remain unresolved.
- Any medium findings are accepted with explicit rationale and follow-up.

If review fails:
- Mark gate as `fail`.
- Mark tests, format/lint, docs/version gates as `not_run`.
- Return findings with severity and file references.

## 3) Gate B: Tests (conditional)
Run all available tests for detected stack(s).
- Discover test commands from package/build config.
- Execute every applicable test target for impacted stacks.
- If no tests exist, set gate to `skipped (not available)` and continue only if policy allows.

Tests gate fail criteria:
- Any executed test command fails.

## 4) Gate C: Formatter and Linter (conditional)
Run formatter and linter if available for impacted stack(s).
- Discover commands from scripts/tooling config.
- Run formatter first, then linter, unless repository convention requires inverse order.
- If command is unavailable, mark corresponding gate item `skipped (not available)`.

Quality gate fail criteria:
- Any executed formatter/linter command fails.

## 5) Gate D: Docs and Version Planning (conditional)
Only when gates A-C are pass/allowed-skipped:
- Route through `changelog-keepachangelog-update` skill to prepare verified changelog updates.
- Route through `readme-updater` skill when README-impacting changes are present or requested.
- Determine release type:
  - Feature -> bump `minor + 1`
  - Bug fix -> bump `patch + 1`
  - Never bump major automatically
- If classification is ambiguous, record assumption and rationale.

## Output Contract
Return sections in this order:
1. `## Review Findings`
- Ordered by severity: `high`, `medium`, `low`
- Each finding includes: `severity`, `summary`, `file reference`, `impact`, `fix recommendation`

2. `## Gate Status Matrix`
- Table: `Gate | Status | Evidence | Reason`
- Status values: `pass`, `fail`, `skipped`, `not_run`

3. `## Relevant Skills and Rules Applied`
- Explicit list of selected skills/rules/agents and why each was included

4. `## Docs and Version Actions`
- Planned changelog updates
- Planned README updates (or `not required`)
- Version decision: `minor+1` for feature or `patch+1` for bugfix, with rationale
- Explicit statement: `No automatic git commit was performed.`

## Verification Gates for This Skill
Before returning:
- Confirm Plan Mode requirement was respected.
- Confirm no automatic commit command was executed.
- Confirm only relevant skills were selected.
- Confirm fail-fast behavior was applied.
- Confirm output matches required section order.
