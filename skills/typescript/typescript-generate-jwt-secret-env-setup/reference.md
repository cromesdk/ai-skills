# Reference: JWT_SECRET detection and .env parsing

## Precondition

Require at least one `JWT_SECRET` reference under `src/` before modifying `.env`.

Recommended search:

- `rg -n --glob "src/**" "JWT_SECRET"`

If no matches are found in `src/`, do not generate or modify `JWT_SECRET`.

## Parsing .env

Interpret only active (non-comment) lines that begin with `JWT_SECRET=`.

Rules:

- Key format: `JWT_SECRET=value`
- Value is everything after the first `=`
- Ignore leading/trailing whitespace around key and value for comparison
- For comparison, strip one matching pair of surrounding single or double quotes

Treat as empty when the normalized value is:

- empty string (`JWT_SECRET=`, `JWT_SECRET=""`, `JWT_SECRET=''`)

Treat as placeholder when the normalized value is exactly:

- `change-me-in-production`

Treat as valid and do not overwrite for any other non-empty value.

## Update behavior

- If no active `JWT_SECRET` key exists, add one new line.
- If one active key exists and it is empty/placeholder, replace only that value.
- If multiple active keys exist, update only the first active key that is empty/placeholder.
- Never edit commented lines like `# JWT_SECRET=...`.
- Preserve file order, comments, and unrelated formatting.

## Edge cases

| .env line | Decision |
|---|---|
| `JWT_SECRET=change-me-in-production` | Generate and replace |
| `JWT_SECRET="change-me-in-production"` | Generate and replace |
| `JWT_SECRET='change-me-in-production'` | Generate and replace |
| `JWT_SECRET=` | Generate and replace |
| `JWT_SECRET=""` | Generate and replace |
| `JWT_SECRET=''` | Generate and replace |
| `# JWT_SECRET=change-me-in-production` | Ignore comment |
| `JWT_SECRET=my-real-secret-xyz` | Keep existing value |

When uncertain, prefer safety: do not replace non-placeholder values.
