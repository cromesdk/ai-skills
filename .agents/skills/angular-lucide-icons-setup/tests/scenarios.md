# Scenario Tests: angular-lucide-icons-setup

Use these scenarios to validate trigger quality, deterministic setup, non-destructive edits, and architecture-aware Lucide integration.

## Easy

### Scenario 1: Fresh Angular 20 standalone app
**Input prompt**
`Add lucide-angular to this Angular 20 app and render House and Menu icons.`

**Expected behavior**
- Installs `lucide-angular` with the detected package manager.
- Detects standalone mode or honors explicit standalone input.
- Adds `LucideAngularModule` import in target standalone component.
- Adds icon object bindings and renders at least one `<lucide-icon [img]="..."></lucide-icon>`.
- Verifies build succeeds.

### Scenario 2: NgModule app with explicit icon list
**Input prompt**
`Configure Lucide icons in this NgModule Angular app using House, User, and File.`

**Expected behavior**
- Uses `LucideAngularModule.pick({ House, User, File })` in module imports.
- Uses name-based template rendering for selected icons.
- Avoids importing unused icons.

## Hard

### Scenario 3: Existing complex imports in app module/component
**Input prompt**
`Set up lucide-angular, but do not break existing imports or formatting.`

**Expected behavior**
- Merges into existing imports without removing unrelated entries.
- Preserves formatting/style conventions as much as possible.
- Does not rewrite files wholesale.

### Scenario 4: Re-run idempotency
**Input prompt**
`Run the Lucide setup again and verify no duplicate changes are introduced.`

**Expected behavior**
- No duplicate import lines.
- No duplicate icon registration entries.
- No duplicate template icon snippets unless explicitly requested.

### Scenario 5: Monorepo with multiple lock files
**Input prompt**
`Install Lucide in this Angular 20 workspace that uses pnpm.`

**Expected behavior**
- Selects `pnpm` from lock-file detection.
- Runs package-manager-consistent install command.
- Avoids mixing package managers.

## Edge Cases

### Scenario 6: Unsupported Angular version
**Input prompt**
`Set up lucide-angular here.` (run in Angular <20 workspace)

**Expected behavior**
- Fails fast with explicit version mismatch reason.
- Does not apply partial edits.

### Scenario 7: Non-Angular directory
**Input prompt**
`Add Lucide icons in this folder.` (run where `angular.json` is missing)

**Expected behavior**
- Reports missing Angular workspace files clearly.
- Exits without file changes.

### Scenario 8: User requests all icons
**Input prompt**
`Import all Lucide icons globally so I can use any icon.`

**Expected behavior**
- Warns about bundle-size impact before applying.
- Proceeds only if request is explicit after warning.
- Documents the tradeoff in the output.
