# Skill Evaluation Scenarios

## Scenario 1: public_controller_e2e_addition
### Input
User asks: "Add e2e tests for my health and status endpoints."

### Repository/Context State
- NestJS project with existing e2e setup.
- Public endpoints exist and do not require auth.

### Expected behavior
- Reuses existing e2e runner and script.
- Adds/updates `test/<feature>.e2e-spec.ts` without introducing a second runner.
- Mirrors production bootstrap behavior from `src/main.ts`.
- Asserts success and validation-failure paths where applicable.
- Runs repository e2e command and reports result.

## Scenario 2: jwt_enabled_full_matrix
### Input
User asks: "Create e2e tests for auth and protected routes with JWT."

### Repository/Context State
- JWT auth is configured (`JwtModule` or `JWT_SECRET` usage and guarded routes).
- Login endpoint exists.

### Expected behavior
- Detects JWT/auth configuration before generating tests.
- Adds full matrix: valid login, invalid login, no token, valid token, invalid/expired token.
- Uses Bearer token from login response key used by the project.
- Verifies via repository e2e command and reports pass/fail.

## Scenario 3: keep_existing_jest_runner
### Input
User asks: "Fix our API e2e tests."

### Repository/Context State
- Project uses Jest for e2e tests.
- Existing Jest e2e script is already in `package.json`.

### Expected behavior
- Keeps Jest-based e2e flow; does not add Vitest or extra runner config.
- Repairs tests in-place and keeps naming conventions consistent.
- Runs existing e2e command and reports deterministic outcomes.

## Scenario 4: bootstrap_parity_required
### Input
User asks: "My e2e tests pass locally but fail on validation behavior, fix them."

### Repository/Context State
- `src/main.ts` configures global pipes/interceptors.
- Existing tests do not mirror those bootstrap settings.

### Expected behavior
- Aligns test bootstrap with production bootstrap behavior from `src/main.ts`.
- Updates assertions to match true runtime status codes and response shape.
- Verifies with e2e command after parity fix.

## Scenario 5: no_auth_detected_public_only
### Input
User asks: "Generate e2e tests for users read endpoints."

### Repository/Context State
- No JWT config, no auth guards, and no login endpoint.

### Expected behavior
- Does not invent auth/login tests.
- Generates public endpoint coverage with success and negative validation paths.
- Reports auth detection result explicitly.

## Scenario 6: verification_blocked_by_missing_env
### Input
User asks: "Add full auth e2e coverage and run tests."

### Repository/Context State
- JWT auth exists, but required env values for e2e are missing.

### Expected behavior
- Implements required test files and keeps runner reuse intact.
- Attempts verification and surfaces exact blocker (missing env key).
- Returns concrete next command/action to unblock verification.

## Scenario 7: unstable_external_dependency_guard
### Input
User asks: "Add e2e tests for endpoints that call third-party APIs."

### Repository/Context State
- Endpoints touch external APIs.
- Repository has no stable mock/stub strategy.

### Expected behavior
- Avoids fragile real-network assertions by default.
- Uses existing repository mocking/stubbing pattern when available.
- Documents any residual verification gap if external dependency stability cannot be guaranteed.
