---
name: winston-logging-on-change
description: Adds concise Winston logging when code is changed in a project that uses Winston (LoggerService). Use when modifying services, controllers, or app code in a NestJS backend that has Winston or LoggerModule installed. Never logs passwords, tokens, or other confidential data.
---

# Winston Logging On Change

Apply concise, high-signal Winston logs when modifying NestJS app logic in a project that already uses a shared `LoggerService`.

## Execute Workflow

1. Confirm logger wiring exists before adding logs.
2. Identify changed application code (services, controllers, guards, interceptors, strategies, handlers).
3. Add logs only around meaningful outcomes, decisions, and failures introduced or affected by the change.
4. Keep all logs free of secrets and sensitive payloads.
5. Verify the final diff for noise, duplication, and unsafe fields.

If the project does not have Winston wiring, do not invent a logger pattern in this skill. Use the Winston setup skill first when the user asks for installation.

## Use Logger Correctly

Inject the project logger into the class constructor, same as other Nest injectables.

Use class context consistently:

- Prefer a stable class-name context such as `AuthService` or `UsersController`.
- Keep context consistent across methods in the same class.

Use levels intentionally:

- `log` or `info`: successful operations and key state transitions
- `warn`: handled but unexpected paths or degraded behavior
- `error`: failures and thrown exceptions
- `debug` or `verbose`: temporary or high-detail diagnostics only

Expected `LoggerService` API shape:

- `log(message, context?, meta?)` or `info(message, context?, meta?)`
- `warn(message, context?, meta?)`
- `error(message, trace?, context?, meta?)`
- `debug(message, context?, meta?)` or `verbose(message, context?, meta?)`
- Lifecycle cleanup when relevant: `onModuleDestroy()` should detach Winston process handlers (`exceptions.unhandle()`, `rejections.unhandle()`) and close the logger (`logger.close()`)

When calling `error`, pass a trace or stack string when it improves diagnosis.

## Log Scope Rules

Log only meaningful events:

- command/query success or failure
- auth/authorization outcomes
- external dependency failures or retries
- branch outcomes that change user-visible behavior

Avoid log noise:

- do not log every method entry/exit
- do not log trivial passthrough helpers
- do not duplicate framework-level logs

Prefer one outcome log per operation, plus one error log on failure.

## Sensitive Data Rules

Never log:

- passwords, password hashes, secrets, API keys
- JWTs, refresh tokens, session tokens, cookies
- full request or response bodies
- raw PII unless explicitly required and redacted

Prefer safe metadata:

- IDs (`userId`, `accountId`, `resourceId`)
- counts and booleans
- status codes and operation names

Keep `meta` small, stable, and diagnostic.

## Edit Checklist

- [ ] Inject `LoggerService` where new logging is needed
- [ ] Use consistent class context
- [ ] Add only high-signal logs tied to changed behavior
- [ ] Include actionable `error` logs with trace when useful
- [ ] Exclude secrets, tokens, raw PII, and full payload bodies
