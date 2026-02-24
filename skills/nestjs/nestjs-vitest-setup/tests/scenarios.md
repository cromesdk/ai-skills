# Scenario Tests

## Easy: Fresh Vitest setup in an existing NestJS app

- Given a NestJS backend with `src/main.ts`, `src/app.module.ts`, `package.json`, and `tsconfig.json`
- When the assistant applies this skill
- Then it installs Vitest dependencies, creates or updates `vitest.config.ts` and `test/vitest.setup.ts`, and updates scripts for `test`, `test:e2e`, and `test:cov`
- And it verifies unit, e2e, and coverage commands before reporting success

## Hard: Migrate mixed Jest + Vitest project to a consistent Vitest baseline

- Given a NestJS project with partial Vitest setup, lingering `jest.config.ts`, and tests using both `jest.*` and `vi.*`
- When the assistant is asked to standardize tests on Vitest
- Then it converts Jest APIs to Vitest equivalents, removes or documents intentional retention of Jest-only config, and normalizes scripts
- And it preserves existing business assertions while making the minimum required migration edits

## Hard: Repair failing e2e tests caused by open handles

- Given e2e tests that initialize `INestApplication` but do not close it
- When the assistant applies this skill to fix hanging test runs
- Then it updates e2e teardown to call `await app.close()` in `afterAll`
- And it verifies `test:e2e` completes without hanging workers

## Edge: Missing required Nest root files

- Given the selected path is missing one or more required files (`package.json`, `tsconfig.json`, `src/main.ts`, `src/app.module.ts`)
- When the workflow starts
- Then the assistant stops before editing, reports exact missing path(s), and asks for the correct project root
- And it does not claim install, migration, or verification success

## Edge: Package manager mismatch or lockfile ambiguity

- Given commands are run with a package manager that does not match the lockfile in the repository
- When dependency installation or script execution fails
- Then the assistant reports the mismatch, switches to lockfile-consistent commands, and retries deterministically
- And it includes the exact corrected command(s) in its report

## Edge: Coverage command passes but no coverage artifacts are produced

- Given `test:cov` exits successfully but `coverage/` is missing due to misconfiguration
- When verification gates are executed
- Then the assistant treats this as a failed gate and reports the configuration gap
- And it does not mark the migration complete until artifacts are generated
