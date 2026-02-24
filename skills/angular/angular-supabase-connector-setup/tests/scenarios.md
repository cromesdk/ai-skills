# angular-supabase-connector-setup scenario tests

## Easy: Single app Angular 20 workspace, first-time Supabase setup

### Input
User asks: "Set up Supabase in this Angular 20 app with an injectable connector service."

### Expected behavior
- Detects Angular workspace and confirms `@angular/core` major version `20`.
- Installs `@supabase/supabase-js` if missing.
- Ensures `supabaseUrl` and `supabaseAnonKey` exist in dev/prod environment files.
- Creates tokens, providers, and connector service in `src/app/core/supabase`.
- Wires `provideSupabaseConnector()` in `app.config.ts`.
- Runs `npm run build` and reports result.

## Hard: Multi-project workspace without projectName

### Input
User asks: "Configure Supabase connector in this repo." Workspace has multiple Angular app projects and no explicit target.

### Expected behavior
- Detects multiple app projects.
- Requests explicit `projectName` before editing files.
- Does not mutate an arbitrary project.
- After target is provided, performs deterministic setup only in that project.

## Hard: Existing API layer must be bridged without tight coupling

### Input
User asks: "Use our existing ApiService with the Supabase connector, but keep things decoupled."

### Expected behavior
- Creates or updates adapter implementation that conforms to `SupabaseApiAdapter`.
- Registers `{ provide: SUPABASE_API_ADAPTER, useExisting: ExistingApiAdapter }`.
- Keeps Supabase connector free of direct concrete `ApiService` references.
- Verifies adapter-free path remains valid when bridge is not configured.

## Edge case: Not Angular 20

### Input
User asks to set up connector, but workspace Angular major version is not `20`.

### Expected behavior
- Stops before dependency install or file edits.
- Reports version mismatch clearly.
- Returns remediation path (upgrade to Angular 20 or request override).

## Edge case: Missing/unsupported environment file layout

### Input
User asks for setup, but selected project does not expose expected environment files for dev/prod config.

### Expected behavior
- Stops before generating Supabase provider wiring that imports unresolved environment paths.
- Reports exact missing files and expected keys.
- Provides concrete next actions to align environment layout, then retry setup.
