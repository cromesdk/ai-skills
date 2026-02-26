# Scenarios: video-downloader-transcoder

## Easy: Implement module in an existing NestJS app

**Given**
- A NestJS backend already exists with `src/main.ts` and a root module.
- `src/libs/video-downloader-transcoder` files are missing or partially stubbed.

**When**
- The agent applies `$video-downloader-transcoder`.

**Then**
- The module, controller, service, and DTO files are created or repaired in `src/libs/video-downloader-transcoder`.
- `VideoDownloaderTranscoderModule` is imported by the root app module.
- The route remains `POST /video-downloader-transcoder/transcode`.

## Hard: Repair unsafe process execution and preserve API contract

**Given**
- Existing service code spawns `yt-dlp` or `ffmpeg` through shell-interpolated strings.
- The endpoint already serves consumers that depend on existing DTO fields.

**When**
- The agent runs `$video-downloader-transcoder` for remediation.

**Then**
- Process execution is converted to argument-array invocation without raw shell interpolation.
- DTO request/response contracts remain backward-compatible unless explicit API changes were requested.
- Stage logs still cover accept/download/transcode/cleanup/error boundaries.

## Edge: Preconditions fail for non-Nest project

**Given**
- The target directory has no `@nestjs/core` dependency and no `src/main.ts`.

**When**
- The agent is asked to run `$video-downloader-transcoder`.

**Then**
- The agent stops before implementation edits.
- The agent reports that this skill requires an existing NestJS app path and requests the correct path.

## Edge: Missing optional env overrides

**Given**
- No `VIDEO_TRANSCODER_*` environment variables are defined.

**When**
- The agent applies the skill to maintain behavior.

**Then**
- Safe defaults are retained (including local workdir and default yt-dlp/ffmpeg behavior).
- The implementation does not fail only because optional proxy/TLS/IP override envs are absent.
