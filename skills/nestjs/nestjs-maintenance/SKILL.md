---
name: nestjs-maintenance
description: After NestJS project changes, run the verification pipeline (docs, clean, build, format, lint, test:cov) only for scripts present in package.json, in that order; repeat until all pass. Use when the NestJS backend was modified, before committing, or when the user asks to verify or run checks.
---

# NestJS Maintenance Verification

## When to use

- The NestJS project (or backend) was changed and verification is needed
- The user asks to verify, run checks, or pre-commit validation
- Before committing or finishing a change set
- Verification includes ensuring JSDoc is current for changed code so the `docs` step (TypeDoc) stays accurate

## Ordered script list

Run only scripts that exist in `package.json`, in this order:

1. **docs** (e.g. typedoc)
2. **clean** (e.g. rimraf dist coverage .cache)
3. **build** (e.g. nest build)
4. **format** (e.g. prettier)
5. **lint** (e.g. eslint)
6. **test:cov** (coverage tests)

## Workflow

1. **Read** `package.json` and get the `scripts` object.
2. **Before running scripts:** If the change set touched source (especially public API or new exports), use the **typescript-jsdoc-develop** skill (`.agents/skills/typescript-jsdoc-develop/SKILL.md`) to add or update JSDoc for affected files so that the `docs` step reflects the codebase.
3. **For each** of the six script names above, **if** it exists in `scripts`, run from the project root:
   ```bash
   npm run <name>
   ```
   Run them strictly in the order listed. Do not skip any script that is present.
4. **If any run fails:** fix the cause (code, config, or dependencies), then **re-run the full sequence** from step 3. Repeat until every run in the sequence passes.
5. Do not skip a script that exists; run all that are present in the defined order.

## When test:cov fails (coverage thresholds)

If `test:cov` fails because coverage is below thresholds:

1. **Prefer adding or updating tests** for uncovered code. Use the coverage report (terminal table or `coverage/index.html`) to find low-coverage files and uncovered line numbers; add or extend `*.spec.ts` / `*.test.ts` to exercise that code and branches.
2. **Do not**, as the default fix, exclude project source from coverage (e.g. `src/libs/**`) or lower thresholds. Exclude only generated/vendor/tooling (e.g. Prisma generated client, `main.ts`, `*.module.ts`, setup files).
3. If you must temporarily lower thresholds (e.g. while tests are being added), add a short comment in `vitest.config.ts` that they should be raised again as tests are added, and treat it as technical debt.
4. For the full "reach coverage" workflow (include/exclude, reading the report, writing tests), use the **nestjs-vitest-coverage** skill (`.agents/skills/nestjs-vitest-coverage/SKILL.md`).

## Summary

- Only run scripts that are defined in `package.json`.
- Order: docs -> clean -> build -> format -> lint -> test:cov.
- Before running scripts: if source was changed (especially public API), update JSDoc using the **typescript-jsdoc-develop** skill so `docs` stays accurate.
- On failure: fix, then run the full sequence again until all pass.
- If test:cov fails on coverage: add or update tests for uncovered code; do not exclude project code or lower thresholds by default.
