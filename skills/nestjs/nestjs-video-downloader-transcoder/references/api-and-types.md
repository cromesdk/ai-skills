# API and Types

## 1. HTTP Endpoint

Route:

1. `POST /video-downloader-transcoder/transcode`

Controller:

1. `VideoDownloaderTranscoderController`

Service entrypoint:

1. `downloadAndTranscode(dto: TranscodeVideoDto)`

## 2. Request DTO

`TranscodeVideoDto`:

1. `sourceUrl: string` (required, `http(s)`)
2. `format?: VideoOutputFormat` (default `mp4`)
3. `quality?: VideoQualityPreset` (default `medium`)
4. `outputName?: string`
5. `userAgent?: string`
6. `referer?: string`
7. `embedPreviewImage?: boolean`

## 3. Enums

### `VideoOutputFormat`

1. `mp4`
2. `webm`
3. `mp3`

### `VideoQualityPreset`

1. `auto`
2. `best`
3. `worst`
4. `low`
5. `medium`
6. `high`

Alias mapping in service:

1. `auto -> medium`
2. `best -> high`
3. `worst -> low`

## 4. Response DTO

`TranscodeVideoResponseDto`:

1. `jobId: string`
2. `outputPath: string`
3. `format: VideoOutputFormat`
4. `quality: VideoQualityPreset`
5. `downloadedBytes: number`
6. `outputBytes: number`

## 5. API Error Contract

1. `400 Bad Request` for invalid URL or yt-dlp failures.
2. `500 Internal Server Error` for unexpected transcoding pipeline failures.

