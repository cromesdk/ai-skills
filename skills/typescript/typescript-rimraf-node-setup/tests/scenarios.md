# Skill Evaluation Scenarios

## Scenario 1: Add clean script in npm project (easy)
### Input
User asks: "Add a cross-platform clean script for `dist` and `coverage`."

### Repository/Context State
- `package.json` exists.
- Package manager is npm.
- No current `clean` script.

### Expected behavior
- Adds `rimraf` as a dev dependency if missing.
- Adds `"clean": "rimraf dist coverage"` to scripts.
- Uses direct `rimraf` command (no `npx` in script).
- Preserves unrelated scripts unchanged.
- Verifies `npm run clean` path.

## Scenario 2: Replace mixed Unix and Windows delete commands (hard)
### Input
User asks: "Our scripts break on Windows. Standardize cleanup."

### Repository/Context State
- `package.json` scripts contain `rm -rf dist` and `rmdir /s /q coverage`.
- Package manager is pnpm.
- Existing script names are used by CI.

### Expected behavior
- Replaces shell-specific commands with equivalent `rimraf` commands.
- Keeps original script names stable.
- Uses package-manager-appropriate install command if `rimraf` missing.
- Does not alter non-cleanup scripts.
- Verifies no shell-specific delete command remains in scripts.

## Scenario 3: Build tool already cleans outputs (edge)
### Input
User asks: "Set up rimraf cleanup."

### Repository/Context State
- Build tool config already performs deterministic cleanup.
- No user request for dedicated standalone `clean` script.

### Expected behavior
- Calls out existing cleanup behavior.
- Avoids adding redundant scripts by default.
- Adds `rimraf` only if a new standalone cleanup step is explicitly requested.
- Documents decision and keeps repository unchanged when no change is needed.

## Scenario 4: Monorepo package with yarn and prebuild hook (hard)
### Input
User asks: "In this package, make prebuild clean `dist` and `.turbo`."

### Repository/Context State
- Working directory is a package subfolder with its own `package.json`.
- Package manager is yarn.
- Existing `prebuild` script has shell-specific deletion.

### Expected behavior
- Updates `prebuild` to use `rimraf dist .turbo`.
- Installs `rimraf` with yarn when missing.
- Keeps command local to the package where `package.json` was edited.
- Confirms build flow still works with the updated prebuild step.

## Scenario 5: Globs and tsbuildinfo cleanup (edge)
### Input
User asks: "Clean generated tsbuildinfo files and cache outputs."

### Repository/Context State
- Cleanup targets include `*.tsbuildinfo` and `.cache`.
- Existing script does not quote glob patterns.

### Expected behavior
- Uses `rimraf` for both folder and glob targets.
- Quotes glob patterns when needed for shell portability.
- Keeps target list explicit and scoped to requested outputs.
- Verifies resulting script is valid JSON and executable.

## Scenario 6: Missing package.json path (edge)
### Input
User asks: "Add rimraf clean scripts here."

### Repository/Context State
- Current working directory does not contain `package.json`.
- User did not provide an alternative project path.

### Expected behavior
- Stops without creating new files.
- Reports the exact blocker (`package.json` missing in current path).
- Requests the correct project root path before proceeding.

## Scenario 7: Existing rimraf already correct (easy)
### Input
User asks: "Standardize cleanup scripts."

### Repository/Context State
- `package.json` already has `"clean": "rimraf dist coverage"` and `"prebuild": "rimraf dist"`.
- No shell-specific delete commands remain.
- `rimraf` already exists in `devDependencies`.

### Expected behavior
- Performs an audit and returns a no-op result with reason.
- Avoids dependency reinstall or script churn.
- Confirms current scripts satisfy cross-platform requirements.

## Scenario 8: Lockfile-based package manager detection (hard)
### Input
User asks: "Fix cleanup scripts in this package."

### Repository/Context State
- `package.json` exists.
- `pnpm-lock.yaml` exists (no `yarn.lock` or `package-lock.json`).
- `rimraf` is missing.

### Expected behavior
- Detects pnpm from lockfile and uses `pnpm add -D rimraf`.
- Updates only requested cleanup scripts.
- Preserves unrelated `package.json` sections unchanged.
