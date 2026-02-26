# nestjs-typedoc-setup scenarios

Use these scenarios to validate deterministic, non-destructive behavior.

## Scenario 1: Easy - Fresh NestJS app without TypeDoc

### Input context
- A NestJS backend has `package.json`, `src/main.ts`, and `tsconfig.json`.
- No existing TypeDoc config (`typedoc.json`, `typedoc.config.*`, `package.json#typedoc` absent).
- No docs scripts in `package.json`.
- `.gitignore` does not contain docs output entries.

### Required actions
1. Detect package manager from lockfile.
2. Install `typedoc` and `typedoc-material-theme` with package-manager-aware command.
3. Create `typedoc.json` with:
   - `entryPoints: ["src"]`
   - `out: "docs/api"`
   - plugin `typedoc-material-theme`
   - required excludes
4. Add `docs:api` and `docs:api:watch` scripts.
5. Add `docs/api/` ignore rule idempotently.
6. Run docs build and verify output.

### Expected file-level outcomes
- New `typedoc.json` exists with required baseline fields.
- `package.json` includes docs scripts.
- `.gitignore` includes docs output ignore entry exactly once.

### Expected verification outcomes
- Docs command succeeds.
- `docs/api/index.html` exists.
- Excluded test/build/generated files are not documented.

### Failure message quality expectations
- If install fails, report command + package manager used.
- If docs generation fails, provide at least one concrete remediation from: Node version, tsconfig path, plugin mismatch.

## Scenario 2: Hard - Monorepo package with existing conflicting TypeDoc config

### Input context
- Workspace is a monorepo; user targets a specific Nest package root.
- Existing `typedoc.json` uses custom output and custom excludes.
- `package.json` already contains a custom docs script name and one stale script value.

### Required actions
1. Operate only in target package root (do not change unrelated packages).
2. Patch existing TypeDoc config minimally:
   - Preserve unrelated keys.
   - Preserve valid user choices for `out` and `entryPoints`.
   - Append required excludes only if missing.
   - Add `typedoc-material-theme` plugin only if absent.
3. Ensure standard scripts exist without removing existing custom scripts.
4. Verify docs generation from package root.

### Expected file-level outcomes
- Existing config remains mostly intact; only additive or targeted fixes applied.
- Required excludes present after merge.
- Existing custom scripts preserved; `docs:api` and `docs:api:watch` available.

### Expected verification outcomes
- Docs command executes from package root and outputs to configured path.
- No regressions to previously configured docs behavior.

### Failure message quality expectations
- If wrong working directory is detected, failure message must explicitly instruct rerun from package root containing `src/main.ts`.
- If config conflict is unresolved automatically, identify exact key conflict and chosen non-destructive fallback.

## Scenario 3: Edge - Missing marker, Prisma-generated files, and lockfile mismatch

### Input context
- `package.json` exists, but `src/main.ts` is missing.
- Prisma is present with generated output under `prisma/generated`.
- A lockfile exists for one package manager while user requests another.

### Required actions
1. Stop destructive edits until required markers are confirmed.
2. Report missing `src/main.ts` as a preflight blocker with one concrete next action.
3. If proceeding after user clarification, ensure Prisma generated exclude is present.
4. Use detected lockfile package manager unless user explicitly overrides.

### Expected file-level outcomes
- No partial config/script edits before blocker is resolved.
- After resolution, config includes `"**/prisma/generated/**"` exclude.

### Expected verification outcomes
- Verification runs only after preflight passes.
- Package-manager selection is deterministic and explicitly stated.

### Failure message quality expectations
- Blocker messages must include missing file path and resolution hint.
- Package-manager mismatch messages must state detected lockfile, chosen command, and override condition.
