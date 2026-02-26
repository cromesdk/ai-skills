---
name: spec-kit-workflow
description: "Run and enforce the full spec-kit execution flow with deterministic stage gating and prerequisite checks. Use when users ask for spec-driven delivery using `/constitution`, `/specify`, `/plan`, `/tasks` (or `/speckit.*` aliases), want strict artifact-aware progression and rollback, or need implementation-phase guidance after task generation. This workflow assumes CLI provisioning from npm package `@spec-kit/cli` and supports assistant variants including Copilot, Codex, Cursor, and Claude."
---

# Spec Kit Workflow

Drive a deterministic, full spec-kit delivery flow from principles to implementation guidance. Enforce prerequisite checks and command order so outputs remain complete and actionable.

## Hard Rules

- Require `spec-kit-setup` readiness before running this workflow.
- Require CLI provenance from npm package `@spec-kit/cli` (installed globally or invoked via `npx`).
- Keep workflow assistant-agnostic: never lock execution to a single assistant provider.
- Execute native spec-kit commands for real via CLI equivalents only: `specify constitution`, `specify specify "<text>"`, `specify plan`, `specify tasks`.
- Treat `/speckit.*` aliases as user shorthand and normalize to native commands.
- Block progression when an earlier stage artifact is missing or incomplete.
- Require explicit feature text for `/specify <text>`; ask for it when absent.
- Emit deterministic status for every stage and provide the next exact command.
- Never simulate command execution or claim files were generated without command evidence.
- Every completed stage must include executed command evidence and filesystem evidence for created/updated artifacts.

## Assistant Compatibility (required)

Support all configured assistants used with spec-kit setup, including:
- `copilot`
- `codex`
- `cursor` / `cursor-agent`
- `claude`

Rules:
- If the user specifies an assistant, preserve it in remediation/setup commands.
- If no assistant is provided, do not block workflow execution solely for missing assistant identity.
- When setup repair is required, use assistant-aware remediation:
  - `specify init --ai <assistant> --here [--script ps]`
  - If assistant is unknown, use deterministic default: `<assistant>=codex`.
- Do not require assistant-specific prompt naming; validate readiness by required artifacts and `specify check`.

## CLI Resolution (required)

Use whichever invocation is available in the environment:
1. Prefer `specify <command>` when `specify` exists in PATH.
2. Fallback to `npx @spec-kit/cli@latest <command>` when `specify` is unavailable.

Record the exact invocation used in `Execution Log`.

## Preconditions

Run these checks before stage execution:

1. Confirm repository is initialized and contains `.specify/` plus `.github/prompts/` baseline artifacts.
2. Confirm `spec-kit-setup` was run successfully (or run it first).
3. Confirm command readiness for `/constitution`, `/specify`, `/plan`, `/tasks` (and normalize `/speckit.*` aliases to these native commands).
4. Confirm required prior artifacts exist before advancing:
   - constitution: `.specify/memory/constitution.md`
   - specification: feature `spec.md`
   - plan: feature `plan.md`
   - tasks: feature `tasks.md`

If any precondition fails, stop and output:

- `status: blocked`
- failed check(s)
- remediation command (usually invoking `$spec-kit-setup`)
- retry command for this skill

Use this precondition output contract:

- `check`: check name
- `status`: pass|fail
- `evidence`: command/path/result summary
- `remediation`: exact command when `status=fail`

Required checks and evidence commands:

1. `git rev-parse --is-inside-work-tree`
2. `node --version`
3. `npm --version`
4. `npm view @spec-kit/cli version`
5. `specify --version`
6. `specify check`
7. `Test-Path .specify`
8. `Test-Path .github/prompts`
9. Artifact existence checks via `Test-Path` for required stage files
10. CLI resolution check: `specify --version` OR `npx @spec-kit/cli@latest --version`

If command execution is unavailable in the current environment, return `status: blocked` with exact unblock command(s). Do not continue with inferred or hypothetical stage completion.

## Stage Workflow (strict sequence)

Execute stages in order and do not skip forward.

### Stage 1: `/constitution`

Execution requirement:
- Run `specify constitution` (or `npx @spec-kit/cli@latest constitution` when using fallback).
- Verify `.specify/memory/constitution.md` exists after command completion.

Create principles covering all required domains:

- Code quality
- Testing standards
- User experience consistency
- Performance requirements

Output:

- principle set per domain
- constraints and acceptance signals per domain
- `stage_status: complete|blocked`
- `next_command: /specify <text>` (or normalized `/speckit.specify <text>` request)
- `execution_evidence`: executed command + exit status
- `artifact_evidence`: constitution file path existence result

### Stage 2: `/specify <text>`

Input contract:

- `<text>` is mandatory and must describe the target feature/change.
- If missing, ask a single direct question requesting the feature text and set:
  - `stage_status: blocked_missing_input`
  - `next_command: /specify <text>`

When input exists:

- run `specify specify "<text>"` (or `npx @spec-kit/cli@latest specify "<text>"` when using fallback)
- generate or refine feature specification
- ensure consistency with constitution principles
- `next_command: /plan` (or normalized `/speckit.plan` request)
- `execution_evidence`: executed command + exit status
- `artifact_evidence`: resolved feature `spec.md` existence result

### Stage 3: `/plan`

Produce implementation strategy using prior artifacts and relevant installed skills under `.agents/skills/**`.

Execution requirement:
- Run `specify plan` (or `npx @spec-kit/cli@latest plan` when using fallback).
- Verify resolved feature `plan.md` exists.

Requirements:

- select only skills materially relevant to the requested feature
- include short rationale for each selected skill
- define architecture/implementation approach, dependencies, and risk controls
- keep plan consistent with constitution and specification
- `next_command: /tasks` (or normalized `/speckit.tasks` request)
- `execution_evidence`: executed command + exit status
- `artifact_evidence`: resolved feature `plan.md` existence result

### Stage 4: `/tasks`

Generate execution-ready tasks:

Execution requirement:
- Run `specify tasks` (or `npx @spec-kit/cli@latest tasks` when using fallback).
- Verify resolved feature `tasks.md` exists.

- ordered by dependency
- scoped for direct implementation
- include validation checkpoints per task
- identify blockers and prerequisite tasks explicitly

Output:

- task list with order/dependencies
- per-task verification action
- `next_command: implement-phase`
- `execution_evidence`: executed command + exit status
- `artifact_evidence`: resolved feature `tasks.md` existence result

### Stage 5: Implement Phase Guidance

There is no native `/implement` command in spec-kit. Treat this as deterministic execution guidance after `/tasks`.

Implementation-phase behavior:

1. Execute tasks in dependency order.
2. Validate after each completed task.
3. Report progress using concise step status.
4. Surface blockers with concrete remediation and resume point.

Use output format:

- `step`: current task id/title
- `status`: pending|in_progress|complete|blocked
- `evidence`: command/check/result summary
- `next_step`: exact next task or command

## Command Normalization

Normalize incoming slash commands before stage execution:

- `/speckit.constitution` -> `/constitution`
- `/speckit.specify` -> `/specify`
- `/speckit.plan` -> `/plan`
- `/speckit.tasks` -> `/tasks`

Rules:

- Accept both forms from users.
- Emit only native commands (`/constitution`, `/specify`, `/plan`, `/tasks`) in `Next Command`.
- If user asks for unsupported stage commands, respond `status: blocked` with the nearest valid stage command.
- Execute using CLI command forms internally and report both slash-command normalization and executed CLI command.

## Failure and Repair Routing

If a requested stage does not have required prior artifacts, return to the earliest missing stage:

- Missing constitution -> return to `/constitution`
- Missing specification -> return to `/specify <text>`
- Missing plan -> return to `/plan`
- Missing tasks -> return to `/tasks`

Always include:

- reason for rollback
- exact command to resume
- exact CLI command that will run after resume command

## Output Contract

For every invocation, return:

1. `Preconditions`: pass/fail checks with evidence
2. `Stage Status`: status for each relevant stage
3. `Artifacts`: files/sections produced or updated
4. `Next Command`: exact command to run next
5. `Blockers`: explicit remediation commands when blocked
6. `Normalized Command`: original request + normalized command used for execution
7. `Execution Log`: each stage command actually run (`command`, `exit_code`, `stdout/stderr summary`)
8. `Artifact Verification`: per-artifact `path`, `exists`, and check command used
