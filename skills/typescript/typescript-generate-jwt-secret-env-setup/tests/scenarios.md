# Scenario Tests

## Easy: Add JWT_SECRET when src references it and .env key is missing

- Given a Node.js or NestJS repository with `src/` containing `JWT_SECRET` usage
- And `.env` exists but has no active `JWT_SECRET=` line
- When the assistant applies this skill
- Then it generates a cryptographically secure secret and appends one active `JWT_SECRET=<generated>` entry
- And it preserves unrelated `.env` lines and comments
- And it reports `updated` without printing the secret value

## Hard: Replace placeholder in first eligible duplicate key only

- Given `.env` contains multiple active `JWT_SECRET=` lines
- And the first active key is `JWT_SECRET="change-me-in-production"` while a later key has a real value
- When the assistant applies this skill with default behavior
- Then it updates only the first eligible placeholder key
- And it leaves later keys unchanged unless the task explicitly requests duplicate cleanup
- And it preserves existing formatting and key order

## Edge: Do not modify .env when no src usage exists

- Given a repository where `.env` has `JWT_SECRET=change-me-in-production`
- And there are no `JWT_SECRET` references under `src/`
- When the assistant runs this skill
- Then it makes no `.env` changes and returns `skipped-no-reference`
- And it explains the precondition failure briefly
- And it does not generate or print any secret value
