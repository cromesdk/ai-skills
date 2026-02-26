# Error Codes

Use these exact `error.code` values in failed results:

1. `E_INVALID_INPUT` for DTO/request validation failures.
2. `E_UNSUPPORTED_PROTOCOL` for non-HTTP(S) URLs, including `file:`.
3. `E_TIMEOUT` for timeout conditions.
4. `E_HTTP_ERROR` for non-2xx HTTP responses.
5. `E_REDIRECT_LIMIT` when redirect count exceeds configured limit.
6. `E_TARGET_EXISTS` when target file already exists and overwrite is disabled.
7. `E_FS_PERMISSION` for filesystem permission failures.
8. `E_PATH_TRAVERSAL` when relative path escapes allowed root.
9. `E_NETWORK` for transport-level network errors.
10. `E_UNKNOWN` for uncategorized failures.

## Mapping Guidance

1. Prefer explicit code mapping over generic fallback.
2. Preserve original error data in `error.details` when useful and safe.
3. Keep `error.message` concise and user-actionable.
