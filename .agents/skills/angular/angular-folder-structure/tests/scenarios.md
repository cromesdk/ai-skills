# Scenarios: angular-folder-structure

## Easy: Greenfield structure for a new app

### Input
User asks to create a scalable Angular 20 folder structure for features `auth` and `dashboard`.

### Expected behavior
- Chooses `greenfield` mode.
- Proposes or creates `core/`, `shared/`, `features/auth`, `features/dashboard`, and `shell/`.
- Places feature routes in `features/<feature>/routes.ts`.
- States lazy-loading expectation for feature routes.
- Provides a final tree snapshot.

## Hard: Refactor mixed legacy structure

### Input
User has `components/`, `services/`, `pages/`, and partial `features/` folders with duplicated models and cross-feature imports.

### Expected behavior
- Chooses `refactor` mode.
- Produces explicit source->target migration map before edits.
- Relocates feature logic into `features/*/data-access` and keeps shared-only items in `shared/`.
- Identifies and resolves forbidden dependency directions.
- Reports deferred/risky moves (for example, breaking API surface) if they cannot be completed safely in one pass.

## Edge: Audit-only request with ambiguous ownership

### Input
User asks for architecture review only and does not want file moves. Several services are used by multiple features, and ownership is unclear.

### Expected behavior
- Chooses `audit-only` mode.
- Asks at most one focused clarification if required.
- Does not move files.
- Returns a violation report grouped by boundary type:
  - shared contains business logic
  - core contains feature-specific code
  - feature-to-feature coupling
- Provides prioritized remediation steps and a verification checklist.

## Edge: Tiny app exemption for lazy loading

### Input
User has a very small Angular app and requests simple routing without lazy loading.

### Expected behavior
- Allows explicit exemption from lazy-loading with a clear note.
- Keeps route ownership boundaries and folder conventions intact.
- Documents the exemption in migration/audit output.

