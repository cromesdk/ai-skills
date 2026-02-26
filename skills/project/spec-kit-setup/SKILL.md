---
name: spec-kit-setup
description: Install, initialize, reconcile, and verify github/spec-kit in repositories using a deterministic non-destructive workflow. Use when users ask to install spec-kit, initialize specify, fix broken `.specify` or `.github/prompts`, upgrade specify-cli, enable spec-driven development, or verify `/constitution` `/specify` `/plan` `/tasks` readiness.
---

# Spec Kit Setup

## Overview
Set up or repair `github/spec-kit` with fail-fast preflight checks, safe reconcile defaults, and deterministic verification. Prefer minimal, non-destructive changes for repositories that already contain `.specify/`.

## Hard Rules
- Run preflight checks before any install, upgrade, or init action.
- Default to safe reconcile for existing installations; do not force re-init unless the user explicitly requests it.
- Never invent flags or commands; use only command forms documented in `github/spec-kit`.
- Stop on first hard blocker and return a concrete unblock command.
- Prefer `--here` initialization so setup stays in the current repository unless user requests another path.
- Use explicit assistant selection with `--ai <assistant>`; do not rely on implicit defaults.

## Preflight (required)
Run and record:
1. `git rev-parse --is-inside-work-tree`
2. `gh --version`
3. `uv --version`
4. `python --version`

If a check fails:
- Mark preflight as `fail`.
- Do not run setup actions.
- Return one unblock path:
  - Missing `gh`: install GitHub CLI and authenticate.
  - Missing `uv`: install uv from astral.sh.
  - Missing `python`: install Python 3.x and ensure PATH is configured.
  - Not in git repo: switch directory to a repo or run `git init`.

If `gh` is installed, also check auth state:
- `gh auth status`
- If not authenticated, stop and return unblock command: `gh auth login`

## Workflow
1. Detect repository state.
2. Choose fresh setup or safe reconcile path.
3. Verify CLI and generated assets.
4. Confirm workflow command readiness (`/constitution`, `/specify`, `/plan`, `/tasks`).
5. Return a deterministic report with actions taken and next command to run.

## Assistant and Script Selection (required)
1. Resolve assistant:
- Use explicit user-provided target if present (for example: `copilot`, `codex`, `cursor-agent`).
- If not specified, default to `codex`.
2. Resolve script variant:
- In PowerShell environments, prefer `--script ps`.
- Otherwise prefer upstream default script variant unless user requests `ps`.
3. Use resolved values in every init/re-init command:
- `specify init --ai <assistant> --here [--script ps]`

## State Detection
Collect:
- `Test-Path .specify`
- `Test-Path .github/prompts`
- `specify --version` (if command exists)
- `Get-ChildItem .github/prompts -File` (if directory exists)

Classify:
- `fresh`: no `.specify` directory.
- `existing_healthy`: `.specify` exists and prompt/workflow artifacts are present.
- `existing_partial_or_broken`: `.specify` exists but key artifacts are missing or invalid.

## Fresh Setup Path
Use official install and init commands:
1. Install CLI:
   - `uv tool install specify-cli --from git+https://github.com/github/spec-kit.git`
2. Initialize in current repo:
   - `specify init --ai <assistant> --here [--script ps]`
   - Use a supported assistant value from current upstream guidance.
3. Verify:
   - `specify --version`
   - `specify check`
   - `Test-Path .specify`
   - `Test-Path .github/prompts`

## Existing Setup Safe Reconcile Path (default)
1. Upgrade CLI first:
   - `uv tool install specify-cli --from git+https://github.com/github/spec-kit.git --upgrade`
2. Inspect existing assets:
   - `.specify/`
   - `.github/prompts/`
3. Apply only missing/repair actions:
   - If `.github/prompts` is missing or incomplete, run:
     - `specify init --ai <assistant> --here [--script ps]`
   - If core `.specify` templates are missing, run:
     - `specify init --ai <assistant> --here [--script ps]`
4. Re-verify with the same checks as fresh setup.

## Workflow Usage Coverage
After setup/reconcile passes, guide users through:
1. `/constitution` to establish project principles.
2. `/specify` to create a formal feature spec.
3. `/plan` to generate implementation approach.
4. `/tasks` to produce execution-ready task breakdown.

Verify readiness before recommending workflow commands:
- Confirm `.github/prompts` contains command prompt files.
- Confirm repository has `.specify` baseline structure.
- Confirm `specify check` passes.

## Output Contract
Return:
1. `Preflight`
- each required check with `pass/fail` evidence
2. `State Classification`
- `fresh`, `existing_healthy`, or `existing_partial_or_broken`
3. `Actions`
- exact commands executed or recommended
4. `Verification`
- version and artifact checks
5. `Next Step`
- explicit command from `/constitution`, `/specify`, `/plan`, `/tasks`

## Reference Commands (Upstream-Backed)
- Install: `uv tool install specify-cli --from git+https://github.com/github/spec-kit.git`
- Upgrade: `uv tool install specify-cli --from git+https://github.com/github/spec-kit.git --upgrade`
- Initialize current repo: `specify init --ai <assistant> --here [--script ps]`
- Diagnostics: `specify check`
- Version check: `specify --version`
