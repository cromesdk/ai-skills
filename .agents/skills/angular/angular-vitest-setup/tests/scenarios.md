# angular-vitest-setup scenarios

## Easy

### Scenario: Migrate a fresh Angular 20 app from Karma/Jasmine to Vitest

User prompt:
"Set up Vitest in my Angular 20 app."

Expected behavior:
- Detect workspace root and single target project.
- Install `vitest` and `jsdom` as dev dependencies.
- Update test builder to `@angular/build:unit-test`.
- Remove Karma/Jasmine packages.
- Run build and non-watch test command.
- Report changed files and verification outcomes.

## Hard

### Scenario: Multi-project workspace where only one app should be migrated

User prompt:
"Configure Vitest only for the `admin-app` project in this Angular workspace."

Expected behavior:
- Identify the named project and update only that project's test target.
- Avoid changing test targets for unrelated projects.
- Remove packages only if they are unused by remaining projects, or clearly report shared dependency constraints.
- Run verification scoped to the intended project where possible.

### Scenario: Multi-project workspace with no project specified

User prompt:
"Migrate this workspace to Vitest."

Context:
- `angular.json` contains multiple apps/libraries with test targets.

Expected behavior:
- Stop and request project disambiguation before edits.
- Do not apply partial updates to an arbitrary project.
- Resume only after target project is explicit.

## Edge Cases

### Scenario: Workspace uses `targets` key and already has partial Vitest setup

User prompt:
"Fix my broken Vitest setup."

Context:
- `angular.json` uses `projects.<name>.targets.test`.
- `vitest` is already installed.
- Karma packages still exist.

Expected behavior:
- Update the correct `targets.test.builder` field.
- Preserve valid existing test options.
- Remove stale Karma/Jasmine packages.
- Detect and report unresolved Jasmine API usage in spec files.

### Scenario: Missing workspace prerequisites

User prompt:
"Add Vitest here."

Context:
- No `angular.json` in current directory.

Expected behavior:
- Fail fast with a clear message that workspace preflight failed.
- State the exact missing file.
- Do not run install or uninstall commands.

### Scenario: Project exists but has no `test` target

User prompt:
"Switch this Angular project to Vitest."

Context:
- Project exists in `angular.json`.
- No `architect.test` or `targets.test` entry.

Expected behavior:
- Stop and report missing `test` target path.
- Avoid creating speculative test config automatically.
- Provide the precise path that must be added before migration can continue.

### Scenario: Incompatible Angular tooling version

User prompt:
"Migrate tests to Vitest."

Context:
- Workspace Angular tooling does not support `@angular/build:unit-test`.

Expected behavior:
- Detect version/tooling incompatibility before config mutation.
- Stop with an explicit compatibility error.
- Suggest upgrading Angular tooling or using a version-appropriate migration path.