# Skill Evaluation Scenarios

## Scenario 1: fresh_setup_success
### Input
User asks: "Introduce spec-kit into this repo and get me started."

### Repository/Context State
- Valid git repository.
- `.specify` and `.github/prompts` do not exist.
- `gh`, `uv`, and `python` are installed.
- `gh auth status` passes.

### Expected behavior
- Preflight passes.
- Skill selects fresh setup path.
- Runs official install and init commands.
- Uses explicit `--ai <assistant>` and `--here` during init.
- Verifies `specify --version`, `specify check`, `.specify`, and `.github/prompts`.
- Returns `/constitution` as next-step command.

## Scenario 2: existing_setup_safe_reconcile
### Input
User asks: "Update our existing spec-kit setup to latest and verify it."

### Repository/Context State
- Valid git repository.
- `.specify` and `.github/prompts` already exist and look healthy.
- `specify` command is installed.

### Expected behavior
- Preflight passes.
- Skill selects safe reconcile path.
- Runs official upgrade command first.
- Does not force destructive re-init.
- Reports that no repair is needed (or only minimal non-destructive actions).
- Verifies readiness with `specify check`.

## Scenario 3: partial_install_repair
### Input
User asks: "Fix our broken spec-kit setup."

### Repository/Context State
- Valid git repository.
- `.specify` exists.
- `.github/prompts` is missing or incomplete.
- Tooling prerequisites are available.

### Expected behavior
- Preflight passes.
- Skill classifies as `existing_partial_or_broken`.
- Performs targeted non-destructive repair via official init flow using explicit `--ai`.
- Verifies assets after repair.
- Returns readiness for `/specify` and downstream workflow commands.

## Scenario 4: missing_gh_or_uv_preflight_fail
### Input
User asks: "Set up spec-kit here."

### Repository/Context State
- Valid git repository.
- `gh` or `uv` is missing from PATH.

### Expected behavior
- Preflight fails with explicit missing-tool evidence.
- No setup/install/init actions run.
- Output includes concrete unblock command/path.
- Output remains deterministic and fail-fast.

## Scenario 5: non_git_directory_preflight_fail
### Input
User asks: "Initialize spec-kit in this folder."

### Repository/Context State
- Current folder is not a git repository.

### Expected behavior
- Preflight fails on git-repository check.
- No setup/install/init actions run.
- Output includes unblock action (`git init` or switch directory).

## Scenario 6: workflow_commands_available_after_setup
### Input
User asks: "Finish setup and tell me exactly what command flow to run next."

### Repository/Context State
- Setup or reconcile path completed successfully.
- Prompt files and `.specify` are present.

### Expected behavior
- Skill confirms readiness for slash-command workflow.
- Recommends ordered progression: `/constitution`, `/specify`, `/plan`, `/tasks`.
- Includes verification rationale for why each command is now safe to use.

## Scenario 7: gh_installed_but_not_authenticated
### Input
User asks: "Set up spec-kit in this repo."

### Repository/Context State
- Valid git repository.
- `gh`, `uv`, and `python` are installed.
- `gh auth status` fails.

### Expected behavior
- Preflight fails on GitHub CLI authentication.
- No setup/install/init actions run.
- Output includes unblock action: `gh auth login`.

## Scenario 8: unsupported_or_missing_assistant_value
### Input
User asks: "Initialize spec-kit here." (no assistant specified)

### Repository/Context State
- Valid git repository with prerequisites available.
- Fresh setup.

### Expected behavior
- Skill resolves assistant deterministically (`codex` default) and does not ask unnecessary follow-up questions.
- Uses explicit init flags: `specify init --ai <resolved-assistant> --here`.
- In PowerShell context, includes `--script ps`.

## Scenario 9: prompts_directory_exists_but_incomplete
### Input
User asks: "Repair the spec-kit prompts only."

### Repository/Context State
- Valid git repository.
- `.specify` exists.
- `.github/prompts` exists but required slash-command prompt files are missing.

### Expected behavior
- Skill classifies as `existing_partial_or_broken`.
- Executes targeted re-init with explicit `--ai` and `--here`.
- Re-verifies prompt files and `specify check` before declaring readiness.
