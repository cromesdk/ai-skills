# Test Plan

## 1. Unit Tests

### Controller

1. `transcode` forwards DTO to service.
2. controller returns service response shape including `quality`.

### Service orchestration

1. resolves workdir.
2. runs yt-dlp phase.
3. runs ffmpeg transcode phase.
4. returns `TranscodeVideoResponseDto` fields.
5. cleans temporary files in `finally`.

### DTO validation

1. reject invalid `sourceUrl`.
2. reject unknown `format`.
3. reject unknown `quality`.
4. accept optional `userAgent`, `referer`, `embedPreviewImage`.

## 2. Integration Tests

1. submit a valid media-page URL and assert successful response.
2. assert output file exists and has non-zero size.
3. validate resulting codecs for MP4:
   - video: H.264
   - audio: AAC
4. for MP3 format, assert audio stream exists.

## 3. Error-path Tests

1. unsupported or blocked URL returns `400`.
2. force ffmpeg failure and assert `500`.
3. assert partial temp/output files are removed after failure.

## 4. Logging Assertions

Where test harness captures logger calls, assert stage logs are emitted:

1. job accepted
2. yt-dlp start/end
3. ffmpeg start/end
4. cleanup log

## 5. Acceptance Criteria

1. endpoint remains `POST /video-downloader-transcoder/transcode`.
2. no global ffmpeg install required by default.
3. quality enum supports `auto|best|worst|low|medium|high`.
4. format enum supports `mp4|webm|mp3`.
5. response includes both `format` and `quality`.

