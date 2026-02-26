# Scenario Tests

## Easy: Add logs for new successful and failure paths

- Given a NestJS service change introduces a new external API call and fallback path
- When the assistant applies this skill
- Then it adds one success log and one failure log at meaningful outcome points using existing `LoggerService` conventions
- And it avoids method entry/exit log noise and confirms no sensitive payload fields are logged

## Hard: Repair noisy logging in mixed runtime units

- Given changed controller and service files already include excessive per-method debug logs
- When the assistant is asked to standardize logging quality
- Then it removes or consolidates low-value logs and keeps only high-signal logs around outcomes, branch decisions, and failures
- And it preserves behavior while keeping context naming consistent per class

## Edge: Logger wiring missing

- Given the target NestJS project has no shared Winston logger integration
- When this skill is triggered for logging changes
- Then the assistant stops before code edits and reports that this skill requires pre-existing logger wiring
- And it recommends running the Winston setup workflow before retrying

## Edge: Sensitive data present in candidate metadata

- Given a changed auth flow includes `password`, `accessToken`, and full request body variables
- When the assistant adds logging
- Then it excludes those fields and logs only safe metadata such as `userId`, operation name, and status/outcome
- And it explicitly states that secrets, tokens, and raw bodies were not logged

## Edge: Non-standard logger method signatures

- Given a project logger wrapper exposes `info/warn/error` with custom argument order
- When logging is added to changed files
- Then the assistant adapts to local logger signatures instead of forcing canonical method calls
- And it keeps edits minimal without rewriting the logger abstraction