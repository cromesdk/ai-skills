# JSDoc Reference

Use this file for tag syntax and edge cases while applying the workflow in `SKILL.md`.

## Core tags

| Tag | Use |
| --- | --- |
| `@param` | Document each input parameter and what it means. |
| `@returns` | Describe the return value (or resolved value for async). |
| `@throws` | Document expected thrown errors and the condition. |
| `@example` | Provide one short, realistic usage example. |
| `@typedef` | Define JSDoc-only object/function types (mostly in `.js`). |
| `@property` | Document fields for `@typedef` object types. |

## Parameter patterns

Simple parameter:

```js
@param userId - User identifier
```

Optional/default parameter:

```js
@param [limit=25] - Max number of items
```

Destructured object parameter:

```js
@param options - Query options
@param options.limit - Max number of items
@param options.cursor - Pagination cursor
```

Rest parameter:

```js
@param values - Values to combine
```

## Return and async guidance

- Use `@returns` consistently (avoid mixing with `@return`).
- For async functions, describe the resolved value, not just `Promise`.
- Omit `@returns` only when a function intentionally returns nothing.

## Throws guidance

- Add `@throws` when code can throw under normal use (validation, network failure, parse errors).
- Name an error type when known; otherwise describe the condition clearly.

## TypeScript and TSX guidance

- Keep type authority in the TypeScript signature.
- Add JSDoc type annotations only when they clarify behavior better than the signature.
- For overloads, document the implementation declaration.
- Use `@template` when generic parameter meaning is not obvious.

## React guidance

- Document component purpose and user-visible behavior.
- Document major props behavior if not obvious from prop names.
- Prefer referencing a props interface over duplicating every prop detail.

## Useful optional tags

- `@deprecated` for migration notes.
- `@see` for related symbols or docs.
- `@remarks` for non-obvious implementation context.
- `@internal` when docs tooling should hide the symbol.

## Quick review checklist

- Summary sentence is specific and behavior-focused.
- Parameter names exactly match the current signature.
- Optional/default behavior is documented correctly.
- Return/throw descriptions match real behavior.
- No runtime code changes were made while editing docs.
