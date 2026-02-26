# Skill Evaluation Scenarios

## Scenario 1: review_fails_stops_pipeline
### Input
User asks: "Run the git review orchestrator on current changes."

### Repository/Context State
- Diff includes risky code changes with missing coverage and one high-severity regression risk.

### Expected behavior
- Review gate returns `fail` with severity-ordered findings and file references.
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
- Skill performs all allowed gates and planning actions.
- Skill explicitly refuses or omits automatic `git commit`.
- Final output contains: `No automatic git commit was performed.`

## Scenario 7: docs_only_routing
### Input
User asks: "Review docs-only changes in this branch."

### Repository/Context State
- Changed files are markdown/docs only.

### Expected behavior
- Routes to relevant doc skills (`readme-updater`, changelog skill) and excludes unrelated framework skills.
- Executes review/tests/quality checks according to docs-only applicability.
- Produces deterministic gate matrix with `skipped` reasons where commands are unavailable.
