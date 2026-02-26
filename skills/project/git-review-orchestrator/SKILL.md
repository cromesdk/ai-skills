---
name: git-review-orchestrator
description: Run a deterministic, fail-fast git quality review pipeline in Plan Mode only. Use when users ask for git/code review, release-readiness checks, quality gates, or combined review + tests + formatter/linter + changelog/readme/version planning. Detects changed files, routes only relevant installed skills/rules/agents by stack and file type, reviews the current git diff by default, and explicitly forbids automatic git commit.
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

## Preflight (required)
Complete all checks before Gate A:
- Confirm execution is in Plan Mode.
- Confirm `git` is available in PATH.
- Confirm current directory is inside a git repository.
- Collect scope evidence commands successfully.

If any preflight check fails:
- Stop immediately.
- Return `Gate Status Matrix` with `Preflight | fail | <evidence> | <reason>`.
- Mark gates A-D as `not_run`.
- Include a concrete unblock action.

## Workflow
1. Run preflight checks and fail fast on any preflight failure.
2. Detect scope and stack from changed files.
3. Run review gate using relevant skills/rules/agents.
4. If review passes, run all available tests.
5. If tests pass, run formatter/linter when available.
6. If all previous gates are pass/allowed-skipped and scope is not `no_changes`, run both `changelog-keepachangelog-update` and `readme-updater` and produce concrete update actions for both.
7. Return a deterministic report with findings, gate matrix, and planned release-doc/version actions.

## 0) Scope and Stack Detection (required)
- Collect current working-tree evidence with:
  - `git status --short`
  - `git diff --name-only`
  - `git diff --cached --name-only`
- Include untracked file paths from `git status --short` in the changed-file map.
- If all sources produce an empty changed-file map, classify as `no_changes`.
- Build a changed-file map and classify by context:
  - Angular: `angular.json`, `src/app/**`, Angular package/config files.
  - NestJS: `nest-cli.json`, `src/**/*.module.ts`, `@nestjs/*` usage.
  - TypeScript Node: `tsconfig*.json`, Node build/test scripts, `src/**/*.ts` non-Angular/Nest contexts.
  - Docs-only: markdown and docs files without runtime code changes.
  - No changes: empty diff scope after staged/unstaged/untracked detection.

## 1) Relevant Skill Routing (required)
Select all relevant skills/rules/agents from installed inventory:
- Always include review mindset and repository rules.
- Include framework-specific skills when matching files are detected.
- For any non-`no_changes` scope, Gate D must include both:
  - `changelog-keepachangelog-update`
  - `readme-updater`
- Include document skills for docs-only or docs-touching changes:
  - `changelog-keepachangelog-update`
  - `readme-updater`
- Exclude skills unrelated to changed stack/file types.

Routing examples:
- Angular app changes -> relevant Angular skills.
- NestJS backend changes -> relevant NestJS skills.
- TypeScript tooling/build changes -> relevant TypeScript skills.
- Docs-only changes -> documentation skills only.
- No changes -> run Gate A as informational review (`pass` with "no changed files"), skip gates B-D with reason `not applicable`.

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
- If scope is `no_changes`, set tests gate to `skipped (not applicable)`.

Tests gate fail criteria:
- Any executed test command fails.

## 4) Gate C: Formatter and Linter (conditional)
Run formatter and linter if available for impacted stack(s).
- Discover commands from scripts/tooling config.
- Run formatter first, then linter, unless repository convention requires inverse order.
- If command is unavailable, mark corresponding gate item `skipped (not available)`.
- If scope is `no_changes`, set formatter/linter gate to `skipped (not applicable)`.

Quality gate fail criteria:
- Any executed formatter/linter command fails.

## 5) Gate D: Docs and Version Planning (conditional)
Only when gates A-C are pass/allowed-skipped:
- If scope is non-empty (not `no_changes`), route through both `changelog-keepachangelog-update` and `readme-updater`.
- For non-empty scope, both changelog and README update actions are mandatory and must be concrete.
- For non-empty scope, do not return `not required` for changelog or README actions.
- Determine release type:
  - Feature -> bump `minor + 1`
  - Bug fix -> bump `patch + 1`
  - Never bump major automatically
- If classification is ambiguous, record assumption and rationale.
- If scope is `no_changes`, set docs/version gate to `skipped (not applicable)`.

## Output Contract
Return sections in this order:
1. `## Review Findings`
- Ordered by severity: `high`, `medium`, `low`
- Each finding includes: `severity`, `summary`, `file reference`, `impact`, `fix recommendation`

2. `## Gate Status Matrix`
- Table: `Gate | Status | Evidence | Reason`
- Required rows in order: `Preflight`, `Gate A: Review`, `Gate B: Tests`, `Gate C: Formatter/Linter`, `Gate D: Docs/Version`
- Status values: `pass`, `fail`, `skipped`, `not_run`

3. `## Relevant Skills and Rules Applied`
- Explicit list of selected skills/rules/agents and why each was included

4. `## Docs and Version Actions`
- Planned changelog updates (mandatory when scope is non-empty and Gate D runs)
- Planned README updates (mandatory when scope is non-empty and Gate D runs)
- Version decision: `minor+1` for feature or `patch+1` for bugfix, with rationale
- Explicit statement: `No automatic git commit was performed.`

## Verification Gates for This Skill
Before returning:
- Confirm Plan Mode requirement was respected.
- Confirm no automatic commit command was executed.
- Confirm only relevant skills were selected.
- Confirm fail-fast behavior was applied.
- Confirm output matches required section order.
- Confirm `Preflight` row exists in the gate matrix.
- Confirm that when scope is non-empty and Gate D ran, both README and CHANGELOG actions are present.
- Confirm no `not required` is emitted for README/CHANGELOG in that condition.
