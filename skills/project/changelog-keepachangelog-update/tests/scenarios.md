# Skill Evaluation Scenarios

## Scenario 1: Update existing root changelog from local changes (easy)
### Input
User asks: "Update CHANGELOG.md based on what changed."

Repository contains:
- Root `CHANGELOG.md` with `[Unreleased]`
- Modified source files and tests

### Expected behavior
- Reads git evidence (`status`, `diff`).
- Adds concise entries under appropriate `[Unreleased]` categories.
- Keeps prior released versions unchanged.

## Scenario 2: Explicit changelog path in monorepo (hard)
### Input
User asks: "Update `apps/web/CHANGELOG.md` only."

Repository contains:
- Root and app-level changelogs

### Expected behavior
- Updates only `apps/web/CHANGELOG.md`.
- Avoids edits to root changelog.
- Uses evidence relevant to that scope.

## Scenario 3: Missing changelog file (edge)
### Input
User asks: "Update changelog for this repo."

Repository contains:
- No `CHANGELOG.md`

### Expected behavior
- Asks one precise clarification question before creating a new file.
- Does not write to unrelated markdown docs.

## Scenario 4: Unverifiable claimed changes (edge)
### Input
User asks: "Add that we improved security hardening."

Repository contains:
- No security-relevant code or config changes

### Expected behavior
- Refuses to fabricate claim.
- Adds `TBD (owner needed)` only if user still wants placeholder tracking.