# Acceptance Test Plan

Use `vitest` or `jest` and `nock` (or a local test server).

## Required Cases

1. Valid download writes target file and returns `state: "success"` with `ok: true`.
2. HTTP 404 returns `state: "failed"` with `E_HTTP_ERROR` and no leftover target file.
3. Existing target with `overwrite: false` returns `E_TARGET_EXISTS`.
4. Invalid URL input returns `E_INVALID_INPUT`.
5. Cookie object/array is normalized to a valid `Cookie` header.
6. Timeout scenario returns `E_TIMEOUT`.

## Additional Recommended Cases

1. Redirects are followed when enabled and blocked at redirect limit.
2. Path traversal attempt (`../`) returns `E_PATH_TRAVERSAL`.
3. `overwrite: true` replaces existing file.
4. `createDirs: true` creates nested directories.
5. `checksumSha256` is set only on success.
