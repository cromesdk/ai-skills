# angular-pwa-setup scenario tests

## Easy: Single app Angular 20 workspace, first-time PWA setup

### Input
User asks: "Add PWA support to this Angular 20 app and verify it works."

### Expected behavior
- Detects a single application project and selects it without clarification.
- Runs `ng add @angular/pwa --project <projectName> --skip-confirmation`.
- Verifies `ngsw-config.json`, `manifest.webmanifest`, icons, and `index.html` manifest/theme-color wiring.
- Builds the app with `ng build <projectName>`.
- Reports where `ngsw.json` and `ngsw-worker.js` were found.
- Provides manual runtime verification checks for installability and offline behavior.

## Hard: Multi-project workspace with missing project selection

### Input
User asks: "Set up PWA in this repo." Workspace has multiple application projects and no default app target is obvious.

### Expected behavior
- Detects multiple application projects.
- Requests explicit `projectName` before running `ng add`.
- Does not apply changes to an arbitrary project.
- After user selects a target, proceeds with deterministic command and validations.

## Hard: Existing PWA wiring is partially broken

### Input
User asks: "Our service worker is not activating in production. Please fix PWA setup."

### Expected behavior
- Confirms existing `@angular/pwa` dependency and scaffolding state.
- Verifies registration wiring exists in `app.config.ts` or module setup.
- Ensures `enabled` logic is production-safe by default (`!isDevMode()` unless explicitly requested otherwise).
- Rebuilds and validates service-worker output artifacts.
- Reports exact file-level fixes and remaining manual checks.

## Edge case: Non-Angular 20 workspace

### Input
User asks: "Enable PWA" but `@angular/core` major version is not `20`.

### Expected behavior
- Stops before running `ng add @angular/pwa`.
- Reports version mismatch clearly and requests upgrade path or explicit override direction.
- Makes no PWA-related file edits.

## Edge case: Runtime verification cannot run in environment

### Input
User asks for full setup in a CI/non-interactive environment where browser runtime checks cannot be performed.

### Expected behavior
- Completes deterministic setup and build-time validation.
- Marks runtime install/offline verification as pending manual verification.
- Returns explicit manual validation steps for Chrome DevTools Application tab and offline testing.
