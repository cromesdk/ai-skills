# Scenario Tests

## Easy: Add downloader to plain TypeScript app

**User request**
`Use $typescript-file-downloader-module to add a downloader service to this Node TypeScript app.`

**Expected behavior**
1. Detect existing plain TypeScript structure and integrate in-repo (no new standalone package).
2. Implement `DownloadRequest`/`DownloadResult` with deterministic result shape.
3. Enforce required `referer` and `userAgent` request fields.
4. Stream download to disk, not full-memory buffering.
5. Return failed states with standardized error codes instead of throwing.
6. Provide success/failure `DownloadResult` JSON samples.

## Hard: Repair broken NestJS downloader behavior

**User request**
`Fix our NestJS file downloader. It throws on 404 and allows ../ path traversal. Keep existing module layout.`

**Expected behavior**
1. Preserve current NestJS module boundaries and wire `FileDownloadService` via existing module/provider patterns.
2. Replace throw-based expected failures with `state: "failed"` and mapped `error.code`.
3. Add path traversal protection against escaping `process.cwd()` unless explicit override is enabled.
4. Reject unsupported protocols, including `file:`.
5. Add or update tests for 404, traversal, and expected result-shape stability.

## Edge Case: Cookie normalization and timeout mapping

**User request**
`Update downloader to accept cookie objects and arrays, and return E_TIMEOUT when remote host stalls.`

**Expected behavior**
1. Normalize cookie record/array inputs to a valid `Cookie` header string.
2. Preserve required `Referer` and `User-Agent` header behavior.
3. Map timeout failures to `E_TIMEOUT` with non-throwing failed result objects.
4. Keep checksum populated only for successful downloads.
5. Confirm tests cover timeout plus cookie normalization behavior.

## Edge Case: Existing target and overwrite semantics

**User request**
`Do not overwrite existing files unless overwrite=true, and document what changed.`

**Expected behavior**
1. Fail with `E_TARGET_EXISTS` when target exists and overwrite is not enabled.
2. Replace file only when `overwrite=true`.
3. Avoid unrelated refactors or folder moves.
4. Report changed files and why each change was needed.
