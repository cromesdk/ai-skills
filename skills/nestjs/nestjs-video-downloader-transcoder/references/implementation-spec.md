# Implementation Spec

## 1. Module Layout

Maintain the existing library layout:

1. `src/libs/video-downloader-transcoder/video-downloader-transcoder.module.ts`
2. `src/libs/video-downloader-transcoder/controllers/video-downloader-transcoder.controller.ts`
3. `src/libs/video-downloader-transcoder/services/video-downloader-transcoder.service.ts`
4. `src/libs/video-downloader-transcoder/dtos/transcode-video.dto.ts`
5. `src/libs/video-downloader-transcoder/dtos/transcode-video-response.dto.ts`

Register `VideoDownloaderTranscoderModule` in `src/app.module.ts`.

## 2. Runtime Flow

`POST /video-downloader-transcoder/transcode` calls `downloadAndTranscode(dto)` and runs:

1. Resolve workdir and derive file paths.
2. Download source media with `yt-dlp` (`youtube-dl-exec`).
3. Optionally download source preview image when requested.
4. Select the correct media file (prefer merged output).
5. Transcode with ffmpeg (`ffmpeg-static`).
6. Return output metadata payload.
7. Always cleanup temp files in `finally`.

This workflow is synchronous request/response, not a background queue.

## 3. Binary Resolution Rules

### ffmpeg

Resolution order:

1. `VIDEO_TRANSCODER_FFMPEG_BIN` (env override)
2. `ffmpeg-static` path
3. `ffmpeg` fallback

### yt-dlp

Resolution order:

1. `VIDEO_TRANSCODER_YTDLP_BIN` (env override via `createYoutubeDl(path)`)
2. bundled `youtube-dl-exec` binary

## 4. Logging Requirements

`VideoDownloaderTranscoderService` should log:

1. Job accepted
2. Workdir resolved
3. yt-dlp start
4. yt-dlp completion/failure
5. ffmpeg start
6. ffmpeg completion/failure
7. temp cleanup details

All logs must include `jobId` where available.

## 5. Preview Image Embedding

When `embedPreviewImage=true`:

1. Enable yt-dlp thumbnail download and conversion to JPG.
2. Detect the downloaded thumbnail path.
3. Embed image where supported:
   - MP4: attached picture stream
   - MP3: ID3 cover art
4. WEBM continues normal transcode without embedded cover stream.

## 6. Error Handling

1. yt-dlp errors should return `BadRequestException`.
2. Unexpected pipeline errors should return `InternalServerErrorException`.
3. Always remove partial output and temp input files on failure.

