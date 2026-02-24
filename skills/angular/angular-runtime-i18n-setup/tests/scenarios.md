# angular-runtime-i18n-setup scenario tests

## Easy: Standalone Angular 20 app, first-time runtime i18n setup

### Input
User asks: "Set up runtime language switching with English and German in this Angular 20 app."

### Expected behavior
- Validates Angular 20 workspace and identifies standalone app configuration.
- Installs (or validates) `@ngx-translate/core` and `@ngx-translate/http-loader`.
- Creates `public/i18n/en.json` and `public/i18n/de.json` with stable keys.
- Configures `provideTranslateService(...)` and `provideTranslateHttpLoader(...)` in `app.config.ts`.
- Adds language service and root init path.
- Ensures `TranslatePipe` is imported where used.
- Runs `npm run build` and reports verification outcomes.

## Hard: NgModule-based Angular 20 app with partial runtime i18n wiring

### Input
User asks: "Our language toggle exists but strings stay untranslated. Repair runtime i18n without migrating to standalone."

### Expected behavior
- Detects NgModule project shape and keeps module-based structure.
- Repairs provider/module wiring so runtime loader and `TranslatePipe` resolve correctly.
- Preserves existing app structure and avoids unnecessary migration.
- Verifies translation file fetch path and runtime switching behavior.
- Reports exact file-level fixes and any manual checks still required.

## Hard: Multi-project workspace with ambiguous target app

### Input
User asks: "Add runtime i18n to this repo." Workspace has multiple Angular application projects and no clear default app target.

### Expected behavior
- Detects multi-project ambiguity.
- Stops and requests explicit target project.
- Makes no edits until the target is provided.

## Edge case: Non-Angular 20 workspace

### Input
User asks for runtime i18n setup but `@angular/core` major version is not `20`.

### Expected behavior
- Stops before dependency install or file edits.
- Reports the version mismatch clearly.
- Requests upgrade or explicit override direction.

## Edge case: SSR or non-browser runtime

### Input
User asks for setup in an app with SSR/hydration enabled.

### Expected behavior
- Adds or preserves guards for browser-only APIs (`localStorage`, `document`).
- Avoids crashing server render paths.
- Marks browser-only runtime checks as manual if environment cannot execute them.

## Edge case: CI environment without runtime browser verification

### Input
User asks for full setup in CI where only build/test commands can run.

### Expected behavior
- Completes deterministic setup and build verification.
- Reports runtime switch/persistence checks as pending manual verification.
- Returns concise manual verification steps for local/browser validation.

