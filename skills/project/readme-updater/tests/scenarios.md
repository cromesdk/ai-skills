# Skill Evaluation Scenarios

## Scenario 1: Root README rewrite with strong repository evidence (easy)
### Input
User asks: "Please rewrite our README to enterprise quality."

Repository contains:
- `README.md` with minimal setup notes only.
- `package.json` scripts for `dev`, `build`, `test`, and `lint`.
- `.github/workflows/ci.yml` with test and lint jobs.
- `docker-compose.yml` with service ports.

### Expected behavior
- Targets root `README.md`.
- Produces all baseline sections in the required order.
- Uses commands that exist in `package.json`.
- Adds environment/ports tables where applicable.
- Includes unresolved items as `TBD (owner needed)` only when evidence is missing.
- Returns:
  - Updated `README.md`
  - Compact gap report
  - Verification summary (commands, paths, links)

## Scenario 2: Multiple README files and explicit non-root target (hard)
### Input
User asks: "Update `apps/admin/README.md`, not the root README."

Repository contains:
- Root `README.md`
- `apps/admin/README.md`
- Separate toolchains for root and `apps/admin`.

### Expected behavior
- Honors explicit target `apps/admin/README.md`.
- Uses only evidence relevant to `apps/admin` context where possible.
- Does not overwrite root README.
- Notes scope constraints when shared root infra details are required.
- Returns updated target README plus gap report and verification summary.

## Scenario 3: README missing and sparse operational evidence (edge)
### Input
User asks: "Create a production-ready README."

Repository contains:
- No `README.md`.
- Minimal files: source code and partial `package.json`.
- No CI, no deployment docs, no ownership metadata.

### Expected behavior
- Creates root `README.md` using required baseline structure.
- Marks non-evidenced operational/governance content as `Not applicable` or `TBD (owner needed)` with short rationale.
- Avoids fabricated deployment, compliance, or escalation claims.
- Returns new README plus a gap report that clearly calls out missing ownership and release data.

## Scenario 4: Existing README has unverifiable claims (edge)
### Input
User asks: "Harden this README and keep it accurate."

Current README claims:
- SOC 2 certification
- Pager rotation team and escalation contacts
- Automated canary deploys

Repository evidence does not support these claims.

### Expected behavior
- Removes or converts unverifiable claims to explicit `TBD (owner needed)` items.
- Preserves verified claims with source-backed wording.
- Includes verification summary stating that unverifiable claims were corrected.

## Scenario 5: Broken command references and stale paths (hard)
### Input
User asks: "Standardize README so onboarding commands actually work."

Current README references:
- `npm run start:prod` (script not present)
- `./ops/runbook.md` (path missing)

### Expected behavior
- Replaces invalid commands with actual script commands from repo tooling.
- Removes or corrects stale file references.
- Verification summary explicitly reports command/path validation results.

## Scenario 6: Explicit target path missing with update-only intent (edge)
### Input
User asks: "Update `docs/README.md` to enterprise standards."

Repository contains:
- Root `README.md`
- No `docs/README.md`
- No prior request to create new docs path

### Expected behavior
- Detects that `docs/README.md` does not exist.
- Asks one precise clarification question before creating a new README in `docs/`.
- Does not silently overwrite root `README.md` as a fallback.
- Proceeds deterministically once scope is clarified.
