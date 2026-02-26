# Implementation Spec

## Integration Target

Implement within the existing repository structure by default.
Do not create a separate root package (for example `file-downloader/package.json`) unless explicitly requested.

Recommended placement (adjust to project conventions):

1. `src/libs/file-downloader/...` for NestJS monolith/lib patterns
2. `src/modules/file-downloader/...` when the project uses module-first organization
3. Existing shared utility/service folders when the project already has established downloader abstractions

## Export Rules

Existing project exports must include:

1. `FileDownloadService`
2. All relevant types (`DownloadRequest`, `DownloadResult`, and related helper types)
3. Optional Nest export `FileDownloaderModule` if Nest wrapper exists

## Request Contract

Required fields:

1. `urlName: string`
2. `targetName: string`
3. `referer: string`
4. `userAgent: string`

Optional fields:

1. `cookies?: string | Record<string, string> | Array<{ name: string; value: string }>`
2. `timeoutMs?: number` default `30000`
3. `followRedirects?: boolean` default `true`
4. `maxRedirects?: number` default `5`
5. `overwrite?: boolean` default `false`
6. `createDirs?: boolean` default `true`
7. `allowOutsideCwd?: boolean` optional safety override

## Result Contract

Always return one object with:

1. `state: "queued" | "downloading" | "success" | "failed"`
2. `ok: boolean`
3. `targetPath: string`
4. `startedAt: string` ISO
5. `finishedAt: string | null` ISO
6. `durationMs: number | null`
7. `httpStatus: number | null`
8. `finalUrl: string`
9. `headersSent: Record<string, string>`
10. `headersReceived: Record<string, string> | null`
11. `bytesWritten: number`
12. `contentLength: number | null`
13. `contentType: string | null`
14. `checksumSha256: string | null` success only
15. `error: null | { code: string; message: string; details?: unknown }`

## Functional Requirements

1. Use `undici` (preferred) or `axios` with streaming.
2. Support custom `Referer`, `User-Agent`, `Cookie`.
3. Support timeout and redirect behavior.
4. Stream to disk without loading full file in memory.
5. Compute SHA-256 checksum only on successful completion.
6. Resolve relative target paths against `process.cwd()`.
7. If `createDirs=true`, create parent directories recursively.
8. If target exists and `overwrite=false`, fail with `E_TARGET_EXISTS`.

## Validation Rules

Before download:

1. Validate `urlName` is a valid HTTP/HTTPS URL.
2. Validate `targetName`, `referer`, and `userAgent` are non-empty.
3. If invalid, return failed result with `E_INVALID_INPUT`.

## Security Rules

1. Deny `file:` and non-HTTP(S) protocols (`E_UNSUPPORTED_PROTOCOL`).
2. Deny path traversal outside `process.cwd()` by default (`E_PATH_TRAVERSAL`).
3. Never execute downloaded content.

## Cookies

1. If string, pass as-is to `Cookie` header.
2. If record, convert to `name=value; ...`.
3. If array, convert to `name=value; ...`.

## Observability

No default logging. Allow one of:

1. `logger?: { debug/info/warn/error }`
2. `onEvent?: (event) => void` with event names:
   - `start`
   - `redirect`
   - `progress`
   - `finish`
   - `error`

## NestJS Layer

If Nest wrapper is included:

1. Export `FileDownloaderModule`
2. Provide and export `FileDownloadService`
3. Optionally support `forRoot(options?)` for defaults

## Packaging Rule

1. Reuse existing `package.json` and `tsconfig` in the current workspace.
2. Add dependencies only to the existing package where code is integrated.
3. Generate new standalone npm-style package structure only when explicitly requested.
