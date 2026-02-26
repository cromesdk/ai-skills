---
name: video-downloader-transcoder
description: Implement and maintain the existing NestJS `VideoDownloaderTranscoderModule` that downloads source media with `yt-dlp`, transcodes with `ffmpeg-static`, and exposes `POST /video-downloader-transcoder/transcode` with DTO validation, quality presets, optional preview embedding, and structured logging.
---

# NestJS Video Downloader + Transcoder

## Overview

This skill targets the existing implementation under:

1. `src/libs/video-downloader-transcoder/video-downloader-transcoder.module.ts`
2. `src/libs/video-downloader-transcoder/controllers/video-downloader-transcoder.controller.ts`
3. `src/libs/video-downloader-transcoder/services/video-downloader-transcoder.service.ts`
4. `src/libs/video-downloader-transcoder/dtos/transcode-video.dto.ts`
5. `src/libs/video-downloader-transcoder/dtos/transcode-video-response.dto.ts`

It is a synchronous request pipeline (download + transcode inside one request), not an async queue/job-store architecture.

## Hard Constraints

1. Require an existing NestJS application. Do not scaffold a new app in this skill.
2. Do not rely on global `ffmpeg`; use `ffmpeg-static` path by default.
3. Use `youtube-dl-exec` for `yt-dlp` execution; support optional custom binary via env.
4. Spawn subprocesses with argument arrays; never interpolate untrusted input into shell strings.
5. Keep the public API transport and route stable unless the user explicitly asks to change it.
6. Keep descriptions/examples generic and avoid site-specific references.

## Preconditions

Verify these before coding:

1. `package.json` includes `@nestjs/core`.
2. App bootstrap file exists at `src/main.ts`.
3. A root module exists (`src/app.module.ts` or equivalent wired in `main.ts`).

If any precondition fails, stop and ask for an existing Nest app path.

## Package Baseline

Install runtime dependencies:

```bash
npm i youtube-dl-exec ffmpeg-static
```

Dependency roles:

1. `youtube-dl-exec`: manages and invokes `yt-dlp`.
2. `ffmpeg-static`: provides absolute `ffmpeg` executable path.

## Required Deliverables

Primary files to maintain:

1. `src/libs/video-downloader-transcoder/video-downloader-transcoder.module.ts`
2. `src/libs/video-downloader-transcoder/controllers/video-downloader-transcoder.controller.ts`
3. `src/libs/video-downloader-transcoder/services/video-downloader-transcoder.service.ts`
4. `src/libs/video-downloader-transcoder/dtos/transcode-video.dto.ts`
5. `src/libs/video-downloader-transcoder/dtos/transcode-video-response.dto.ts`

Ensure `VideoDownloaderTranscoderModule` is imported in `src/app.module.ts`.

## Required Service Contract

`VideoDownloaderTranscoderService` must expose:

1. `downloadAndTranscode(dto: TranscodeVideoDto): Promise<TranscodeVideoResponseDto>`

`TranscodeVideoDto` must support:

1. `sourceUrl` (required)
2. `format` enum: `mp4 | webm | mp3`
3. `quality` enum: `auto | best | worst | low | medium | high`
4. `outputName` optional
5. `userAgent` optional
6. `referer` optional
7. `embedPreviewImage` optional

`TranscodeVideoResponseDto` returns:

1. `jobId`
2. `outputPath`
3. `format`
4. `quality`
5. `downloadedBytes`
6. `outputBytes`

## Required Implementation Behavior

1. Resolve workdir from env `VIDEO_TRANSCODER_WORKDIR` or default `tmp/videos`.
2. Download with `yt-dlp` using `bestvideo*+bestaudio/best`.
3. Transcode with ffmpeg using mapped quality preset.
4. Support optional preview-image embedding when `embedPreviewImage=true`.
5. Log each stage (`accepted`, `download start/end`, `ffmpeg start/end`, `cleanup`, `error`).
6. Clean temporary files in `finally`.

## Security and Abuse Controls

1. Validate URL and enums through DTO decorators.
2. Enforce max download bytes via `VIDEO_TRANSCODER_MAX_DOWNLOAD_BYTES`.
3. Sanitize `outputName`.
4. Never pass raw shell strings to process execution.
5. Keep proxy/TLS overrides env-driven:
   - `VIDEO_TRANSCODER_YTDLP_PROXY`
   - `VIDEO_TRANSCODER_YTDLP_NO_CHECK_CERTS`
   - `VIDEO_TRANSCODER_YTDLP_FORCE_IPV4`

Use request-level optional headers:

1. `userAgent`
2. `referer`

## References

1. [references/implementation-spec.md](references/implementation-spec.md)
2. [references/api-and-types.md](references/api-and-types.md)
3. [references/ffmpeg-presets.md](references/ffmpeg-presets.md)
4. [references/security-limits.md](references/security-limits.md)
5. [references/test-plan.md](references/test-plan.md)
