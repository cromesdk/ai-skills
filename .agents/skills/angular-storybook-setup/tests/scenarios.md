# Scenario Tests: angular-storybook-setup

Use these scenarios to validate trigger quality, deterministic setup/repair behavior, non-destructive config merges, and verification gates.

## Easy

### Scenario 1: Fresh Angular 20 app with Tailwind already configured
**Input prompt**
`Add Storybook with themes, designs, and a11y to this Angular 20 Tailwind app.`

**Expected behavior**
- Runs Storybook init for Angular.
- Installs `@storybook/addon-themes`, `@storybook/addon-designs`, and `@storybook/addon-a11y`.
- Merges addons into `.storybook/main.ts` without removing unrelated entries.
- Imports detected global stylesheet in `.storybook/preview.ts`.
- Runs Storybook startup verification.

### Scenario 2: Existing Storybook missing one addon
**Input prompt**
`Fix my Storybook setup so design and a11y panels work.`

**Expected behavior**
- Detects existing Storybook config and repairs only missing addon entries.
- Keeps existing framework and story globs intact unless invalid.
- Ensures addon entries are unique (no duplicates).

## Hard

### Scenario 3: Monorepo with Angular 20 app and non-default global styles path
**Input prompt**
`Set up Storybook for apps/admin and make Tailwind styles show in stories.`

**Expected behavior**
- Uses the target workspace/project context under the provided root.
- Detects style path from `angular.json` (not hardcoded `src/styles.css`).
- Imports the resolved style path into `.storybook/preview.ts`.
- Verifies startup from the correct working directory.

### Scenario 4: Re-run idempotency
**Input prompt**
`Run the Storybook setup again and verify no duplicate config lines are created.`

**Expected behavior**
- No duplicate addon entries.
- No duplicate style import in `.storybook/preview.ts`.
- Existing decorators/parameters remain present.

### Scenario 5: Optional Chromatic CLI requested
**Input prompt**
`Add Storybook and also install Chromatic CLI.`

**Expected behavior**
- Installs required Storybook addons.
- Installs `chromatic` only because user explicitly requested it.
- Verifies CLI availability (for example via `npm run chromatic -- --help` or equivalent command).

## Edge Cases

### Scenario 6: Unsupported Angular major version
**Input prompt**
`Install Storybook with these addons.` (run in Angular 19 workspace)

**Expected behavior**
- Fails fast with explicit Angular version mismatch.
- Makes no partial edits.

### Scenario 7: Missing Angular workspace files
**Input prompt**
`Set up Storybook here.` (run where `angular.json` is missing)

**Expected behavior**
- Reports missing workspace prerequisites clearly.
- Exits before dependency installs or config writes.

### Scenario 8: Tailwind not configured
**Input prompt**
`Add Storybook and make Tailwind classes work.` (workspace has no Tailwind setup)

**Expected behavior**
- Detects missing Tailwind prerequisites.
- Instructs use of `$angular-tailwind-setup` before continuing, or stops with an explicit prerequisite error.
- Avoids claiming full success until Tailwind prerequisite is satisfied.

