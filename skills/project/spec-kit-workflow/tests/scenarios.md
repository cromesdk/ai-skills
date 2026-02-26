# Spec Kit Workflow Scenarios

## Scenario 1: full_flow_happy_path
### Input
User asks: "Run the full spec-kit flow for adding team audit logs."

### Repository/Context State
- `.specify/` and `.github/prompts/` exist.
- Prerequisites from `spec-kit-setup` are already healthy.
- `@spec-kit/cli` is available via npm-backed `specify` command.
- No target feature artifacts exist yet.

### Expected behavior
- Preconditions return pass with evidence.
- Workflow runs strict sequence: `/constitution` -> `/specify <text>` -> `/plan` -> `/tasks` -> implementation guidance.
- Every stage includes deterministic `stage_status` and `Next Command`.
- Output includes `Normalized Command` field.
- Preconditions include npm/CLI readiness evidence for `@spec-kit/cli`.
- Workflow executes real commands (`specify constitution`, `specify specify "<text>"`, `specify plan`, `specify tasks`) and reports exit codes.
- Output includes `Execution Log` and `Artifact Verification` entries proving files were created.

## Scenario 11: multi_assistant_context_supported
### Input
User asks: "Run the workflow for this feature using Claude."

### Repository/Context State
- Setup was previously initialized with assistant `claude`.
- `.specify/` and `.github/prompts/` exist.
- CLI is available.

### Expected behavior
- Workflow does not block due to assistant choice.
- Stage execution proceeds normally.
- If remediation is needed, commands preserve the provided assistant (`--ai claude`).

## Scenario 2: specify_missing_text_block
### Input
User asks: "Run /specify now."

### Repository/Context State
- Constitution exists.
- No feature text provided.

### Expected behavior
- Stage returns `stage_status: blocked_missing_input`.
- Assistant asks one direct question requesting feature text.
- `next_command` is `/specify <text>`.

## Scenario 3: prerequisite_not_ready_routes_setup
### Input
User asks: "Start the workflow."

### Repository/Context State
- `.specify/` directory missing.
- `.github/prompts/` missing.

### Expected behavior
- Preconditions fail fast with explicit failed checks.
- No downstream stage execution is attempted.
- Blocker includes remediation command invoking `$spec-kit-setup`.
- No stage may be marked complete without executed command evidence.

## Scenario 10: npm_cli_not_available_blocks_workflow
### Input
User asks: "Run /plan now."

### Repository/Context State
- `.specify/` and `.github/prompts/` exist.
- `specify` command is missing because `@spec-kit/cli` is not installed/available.

### Expected behavior
- Preconditions fail on CLI readiness checks.
- Workflow returns `status: blocked`.
- Output includes remediation command to restore CLI availability (for example: `npm install -g @spec-kit/cli@latest`).
- No stage is marked complete.

## Scenario 12: npx_fallback_when_specify_missing
### Input
User asks: "Run /constitution."

### Repository/Context State
- `.specify/` and `.github/prompts/` exist.
- `specify` is not in PATH.
- `npx @spec-kit/cli@latest` is available.

### Expected behavior
- Workflow resolves CLI using fallback invocation.
- Executes `npx @spec-kit/cli@latest constitution`.
- Records fallback command in `Execution Log`.
- Stage can complete if artifact verification passes.

## Scenario 4: resume_from_partial_artifacts
### Input
User asks: "Continue from where we left off."

### Repository/Context State
- `.specify/memory/constitution.md` exists.
- Feature `spec.md` exists.
- Feature `plan.md` and `tasks.md` are missing.

### Expected behavior
- Skill resumes at `/plan` without restarting earlier stages.
- Stage status marks constitution/specification as complete and plan as next in sequence.
- `Next Command` is `/plan`.

## Scenario 5: rollback_when_user_skips_required_stage
### Input
User asks: "Run /tasks for feature auth-hardening."

### Repository/Context State
- Constitution and specification exist.
- Plan artifact missing.

### Expected behavior
- Workflow blocks `/tasks` request and rolls back to `/plan`.
- Output states rollback reason and exact resume command.
- No `tasks.md` generation is declared.
- No `specify tasks` execution appears in `Execution Log`.

## Scenario 6: speckit_alias_normalization
### Input
User asks: "Run /speckit.plan."

### Repository/Context State
- Constitution and specification are present for target feature.

### Expected behavior
- Assistant normalizes command to `/plan`.
- Output includes both original and normalized command in `Normalized Command`.
- Emitted `Next Command` uses native command only (`/tasks`).

## Scenario 7: unsupported_stage_command_is_blocked
### Input
User asks: "Run /implement."

### Repository/Context State
- Tasks may or may not exist.

### Expected behavior
- Workflow reports blocked status because `/implement` is not a native spec-kit command.
- Response returns nearest valid next command based on artifact state.
- Implementation phase guidance is provided only after `/tasks` completion.

## Scenario 8: dry_run_or_simulated_execution_is_rejected
### Input
User asks: "Do not run commands, just pretend and give me the outputs for /plan and /tasks."

### Repository/Context State
- Constitution and specification are present.

### Expected behavior
- Skill returns `status: blocked` for simulation-only request.
- Response explains that real command execution is mandatory for this workflow.
- No stage is marked complete without actual command evidence and artifact verification.

## Scenario 9: command_succeeds_but_artifact_missing_is_blocked
### Input
User asks: "Run /tasks."

### Repository/Context State
- Constitution/specification/plan exist.
- `specify tasks` exits successfully but `tasks.md` is not created due to upstream/tooling issue.

### Expected behavior
- Skill marks stage as blocked due to missing required artifact.
- Output includes executed command evidence and failed `Test-Path` artifact check.
- Response returns remediation command and retry command.
