# Scenario Tests

## Easy: Standard post-change verification

- Given a NestJS repository where `package.json` defines `build`, `lint`, and `test:cov`
- When the assistant runs this skill after backend changes
- Then it executes only those present scripts in pipeline order
- And it reports per-step status with a final all-pass result

## Hard: Mid-pipeline failure and full-loop retry

- Given `docs`, `clean`, `build`, `format`, `lint`, and `test:cov` all exist
- And `lint` fails on the first pass
- When the assistant applies this skill
- Then it fixes the lint root cause and reruns from `docs` (not from `lint`)
- And it confirms one uninterrupted full pass at the end

## Edge: No matching maintenance scripts

- Given `package.json` has scripts but none of `docs`, `clean`, `build`, `format`, `lint`, `test:cov`
- When this skill is executed
- Then the assistant stops without speculative commands
- And it reports that no pipeline scripts matched the maintenance contract

## Edge: Coverage threshold regression

- Given `test:cov` fails due to low branch coverage
- When the assistant executes this skill
- Then it prioritizes adding/updating tests for uncovered code
- And it does not default to lowering thresholds or excluding project source files

## Edge: Repository uses pnpm or yarn

- Given the repo uses `pnpm` or `yarn` instead of `npm`
- When the assistant runs maintenance verification
- Then it uses the repository package manager command format
- And it preserves the required script order and retry semantics