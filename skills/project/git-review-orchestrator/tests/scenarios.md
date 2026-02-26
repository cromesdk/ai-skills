# Skill Evaluation Scenarios

## Scenario 1: review_fails_stops_pipeline
### Input
User asks: "Run the git review orchestrator on current changes."

### Repository/Context State
- Diff includes risky code changes with missing coverage and one high-severity regression risk.

### Expected behavior
- Review gate returns `fail` with severity-ordered findings and file references.
- Gate matrix includes a `Preflight` row with `pass` status.
- Tests, formatter/linter, docs/version gates are `not_run`.
- Output includes explicit fail-fast reason.
- Output states no automatic git commit occurred.

## Scenario 2: review_pass_tests_fail
### Input
User asks: "Run full quality gate review for this diff."

### Repository/Context State
- Review has no blocking findings.
- At least one applicable test target fails.

### Expected behavior
- Gate matrix includes a `Preflight` row with `pass` status.
- Review gate `pass`.
- Tests gate `fail` with command evidence.
- Formatter/linter and docs/version gates `not_run`.
- Output includes remediation direction for failing tests.

## Scenario 3: review_tests_pass_lint_missing
### Input
User asks: "Run full review and quality gates."

### Repository/Context State
- Review passes.
- Tests pass.
- Formatter command exists; lint command missing.

### Expected behavior
- Gate matrix includes a `Preflight` row with `pass` status.
- Formatter sub-step runs and passes.
- Lint sub-step marked `skipped (not available)` with evidence.
- Pipeline continues only per policy and reports decision clearly.
- No automatic commit performed.

## Scenario 4: full_pass_feature
### Input
User asks: "Prepare this feature diff for release readiness."

### Repository/Context State
- Feature-level changes across code and docs.
- Review/tests/quality checks pass.

### Expected behavior
- Gate matrix includes a `Preflight` row with `pass` status.
- Relevant framework skills are selected and listed.
- Changelog and README planning actions are produced.
- Version classification is `feature` with planned bump `minor + 1`.
- Output includes explicit no-auto-commit statement.

## Scenario 5: full_pass_bugfix
### Input
User asks: "Run release-quality review for this bugfix diff."

### Repository/Context State
- Bugfix-only code changes.
- All gates pass.

### Expected behavior
- Gate matrix includes a `Preflight` row with `pass` status.
- Changelog/readme actions produced if applicable.
- Version classification is `bugfix` with planned bump `patch + 1`.
- Major bump is explicitly not used.
- No automatic commit performed.

## Scenario 6: never_commit_guard
### Input
User asks: "Run the full orchestrator and finalize everything."

### Repository/Context State
- Any passing scenario.

### Expected behavior
- Gate matrix includes a `Preflight` row with `pass` status.
- Skill performs all allowed gates and planning actions.
- Skill explicitly refuses or omits automatic `git commit`.
- Final output contains: `No automatic git commit was performed.`

## Scenario 7: docs_only_routing
### Input
User asks: "Review docs-only changes in this branch."

### Repository/Context State
- Changed files are markdown/docs only.

### Expected behavior
- Gate matrix includes a `Preflight` row with `pass` status.
- Routes to relevant doc skills (`readme-updater`, changelog skill) and excludes unrelated framework skills.
- Executes review/tests/quality checks according to docs-only applicability.
- Produces deterministic gate matrix with `skipped` reasons where commands are unavailable.

## Scenario 8: preflight_fails_not_git_repo
### Input
User asks: "Run the git review orchestrator for this folder."

### Repository/Context State
- Current directory is not inside a git repository.

### Expected behavior
- Preflight row returns `fail` with command evidence (for example, git repo detection failure).
- Gates A-D are all `not_run`.
- Output includes one concrete unblock action (for example, switch directory or initialize repository).
- Output still states no automatic git commit occurred.

## Scenario 9: preflight_fails_not_plan_mode
### Input
User asks: "Run full git review right now."

### Repository/Context State
- Execution mode is not Plan Mode.

### Expected behavior
- Preflight row returns `fail` with reason that Plan Mode is required.
- Gates A-D are all `not_run`.
- Output includes explicit instruction to rerun in Plan Mode.
- Output still states no automatic git commit occurred.

## Scenario 10: no_changes_scope
### Input
User asks: "Run the orchestrator on the current branch."

### Repository/Context State
- Staged, unstaged, and untracked file sets are all empty.

### Expected behavior
- Scope is classified as `no_changes`.
- Gate A is `pass` as informational review with "no changed files" evidence.
- Gates B-D are `skipped (not applicable)`.
- Output remains deterministic with full gate matrix and no commit statement.

## Scenario 11: ambiguous_release_classification
### Input
User asks: "Run release-quality review and prepare version action."

### Repository/Context State
- All gates pass.
- Diff includes mixed changes where feature vs bugfix classification is ambiguous.

### Expected behavior
- Output records explicit version assumption and rationale.
- Version plan uses either `minor + 1` or `patch + 1` based on that documented assumption.
- Major bump is not selected.
- Output states no automatic git commit occurred.

## Scenario 12: gate_d_always_evaluates_readme
### Input
User asks: "Run full quality gate review on this code-only diff."

### Repository/Context State
- Gates A-C pass.
- Diff has no direct README file changes.

### Expected behavior
- Gate D still routes through README evaluation workflow.
- Output includes explicit README action, either concrete update plan or `not required` with rationale.
- Changelog/version actions remain present per Gate D rules.
- Output states no automatic git commit occurred.
