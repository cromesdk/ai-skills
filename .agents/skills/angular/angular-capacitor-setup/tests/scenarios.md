# angular-capacitor-setup scenario tests

## Easy: Single Angular 20 app, first-time Capacitor setup for Android

### Input
User asks: "Add Capacitor to this Angular 20 app and set up Android."

### Expected behavior
- Detects a single application project and selects it automatically.
- Installs `@capacitor/core` and `@capacitor/cli` only if missing.
- Initializes Capacitor config when absent.
- Resolves `webDir` from Angular build configuration (not hardcoded).
- Runs `ng build <projectName>` before `npx cap sync`.
- Adds Android platform when not already present.
- Reports selected project, configured `webDir`, and executed commands.

## Hard: Multi-project workspace with no target project specified

### Input
User asks: "Set up Capacitor in this repo." Workspace has multiple application projects.

### Expected behavior
- Detects multiple app projects.
- Requests explicit `projectName` before changing files or running `cap` commands.
- Does not apply setup to an arbitrary project.
- After selection, continues with deterministic build-and-sync flow.

## Hard: Existing Capacitor setup has incorrect `webDir`

### Input
User asks: "Capacitor sync fails because it cannot find web assets. Please fix it."

### Expected behavior
- Finds existing Capacitor config and preserves unrelated keys.
- Recomputes `webDir` from current Angular project `outputPath`.
- Builds the selected app and re-runs `npx cap sync`.
- Reports exact fix location and whether sync succeeds.

## Edge case: Requested iOS setup on Windows

### Input
User asks: "Add Android and iOS platforms from my Windows machine."

### Expected behavior
- Adds requested platforms when possible.
- Clearly states iOS open/build requires macOS with Xcode.
- Continues Android verification and marks iOS runtime/open verification as pending manual validation on macOS.

## Edge case: Non-Angular 20 workspace

### Input
User asks for Capacitor setup but `@angular/core` major version is not `20`.

### Expected behavior
- Stops before running install/init/add/sync commands.
- Reports version mismatch clearly.
- Makes no Capacitor-related file edits.
