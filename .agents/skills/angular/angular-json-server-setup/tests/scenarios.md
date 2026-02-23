# Scenario Tests: angular-json-server-setup

Use these scenarios to validate trigger quality, deterministic execution, idempotent edits, and version-aware troubleshooting behavior.

## Easy

### Scenario 1: Fresh Angular 20 workspace, standard `/api`
**Input prompt**
`Set up json-server for this Angular 20 app with a /api proxy and a start:mock command.`

**Expected behavior**
- Installs `json-server` (+ `concurrently` by default) as dev dependencies.
- Creates `mocks/db.json` with valid JSON.
- Creates/updates `src/proxy.conf.json` with `/api` rewrite to `http://localhost:3000`.
- Sets `proxyConfig` in the active Angular serve target.
- Adds/updates `mock:api` and `start:mock` scripts without removing unrelated scripts.
- Creates/updates `mocks/README.md` with run and reset instructions.

### Scenario 2: Custom API port and prefix
**Input prompt**
`Configure json-server on port 3100 and use /backend as the proxy prefix.`

**Expected behavior**
- Uses `3100` in `mock:api` and proxy target.
- Uses `/backend` as proxy key and in `pathRewrite`.
- Verifies Angular calls use relative `/backend/...` paths.

## Hard

### Scenario 3: Existing scripts and complex package.json
**Input prompt**
`Add json-server, but keep all existing npm scripts and do not break current tooling commands.`

**Expected behavior**
- Merges only required script keys.
- Does not reorder/remove unrelated scripts.
- Leaves non-skill config fields untouched.

### Scenario 4: Multi-project workspace
**Input prompt**
`This repo has multiple Angular projects; wire json-server for the app served during development.`

**Expected behavior**
- Updates only the active app serve target (`architect` or `targets` path).
- Avoids touching unrelated projects.
- Documents which project/target was changed.

### Scenario 5: Re-run idempotency
**Input prompt**
`Run the json-server setup again and verify it remains stable.`

**Expected behavior**
- Second run produces no destructive or duplicate changes.
- Existing `mocks/db.json` data is preserved.
- `proxyConfig` and scripts remain valid and singular.

## Edge Cases

### Scenario 6: Not an Angular 20 workspace
**Input prompt**
`Set up json-server here.` (run in non-Angular repo or Angular <20)

**Expected behavior**
- Fails fast with clear reason (`angular.json` missing or unsupported Angular major version).
- Does not apply partial file edits.

### Scenario 7: json-server CLI mismatch
**Input prompt**
`My setup fails with "Unknown option" on json-server; fix it.`

**Expected behavior**
- Treats issue as version/CLI mismatch first.
- Removes dependency on incompatible flags.
- Offers/uses module wrapper approach for advanced behavior when needed.

### Scenario 8: Hardcoded localhost in Angular services
**Input prompt**
`Proxy is configured but app still calls localhost directly.`

**Expected behavior**
- Detects hardcoded `http://localhost:<port>` API calls.
- Refactors usage to relative proxy base (`/api` or configured prefix).
- Verifies proxy path is used end-to-end.
