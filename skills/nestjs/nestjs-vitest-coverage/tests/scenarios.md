# Scenario Tests

## Easy: Normalize provider alignment and pass coverage gate

- Given a NestJS project uses Vitest and coverage is enabled but provider package versions are misaligned
- When the assistant applies `$nestjs-vitest-coverage`
- Then it aligns `vitest` with the selected coverage provider major version
- And it updates config/scripts so `test:cov` passes with enforced thresholds

## Hard: Raise coverage without hiding maintained source code

- Given `test:cov` fails because service and guard branches are uncovered
- When the assistant remediates coverage
- Then it adds or improves tests for success, failure, and edge paths in maintained source code
- And it avoids broad exclusions for controllers/services/handlers just to force a pass

## Edge: Dual provider packages installed with mismatched config

- Given both `@vitest/coverage-v8` and `@vitest/coverage-istanbul` are installed unintentionally
- And config declares only one provider
- When this skill runs
- Then it keeps the configured provider package and removes the unused provider package
- And it verifies the provider in config matches installed dependencies

## Edge: Existing thresholds are stricter than defaults

- Given the project already enforces stricter thresholds than this skill baseline
- When coverage config is standardized
- Then the assistant preserves stricter threshold values
- And it does not lower thresholds unless the user explicitly requests a relaxation

## Edge: CI mismatch with local coverage command

- Given local `test:cov` uses a different command shape than CI workflow
- When the assistant applies this skill
- Then it aligns script behavior so local and CI coverage execute equivalent checks
- And it reports any remaining CI-only blockers that require repository workflow changes
