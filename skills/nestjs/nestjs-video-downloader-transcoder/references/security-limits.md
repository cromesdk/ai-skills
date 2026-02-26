# Security and Limits

## 1. Request Validation

Enforce at DTO level:

1. `sourceUrl` must be valid `http(s)` URL.
2. `format` must be in `VideoOutputFormat`.
3. `quality` must be in `VideoQualityPreset`.
4. optional fields are length-limited and typed.

## 2. Size and Resource Controls

Current limit control:

1. `VIDEO_TRANSCODER_MAX_DOWNLOAD_BYTES` (env)

Expected behavior:

1. yt-dlp download is constrained by max filesize.
2. over-limit downloads fail with safe API error.
3. partial files are cleaned during failure handling.

## 3. Process Execution Safety

1. Use argument arrays only for subprocesses.
2. Never construct shell command strings from user input.
3. Binary paths come from trusted env/package resolution:
   - `ffmpeg-static` or env override
   - `youtube-dl-exec` or env override

## 4. Filesystem Safety

1. Workdir resolves from env or `tmp/videos`.
2. Output name is sanitized to alphanumeric/`-`/`_`.
3. Temporary files are cleaned with job-specific prefix.

## 5. Network-related Env Controls

The following are env-driven and should remain server-only:

1. `VIDEO_TRANSCODER_YTDLP_PROXY`
2. `VIDEO_TRANSCODER_YTDLP_NO_CHECK_CERTS`
3. `VIDEO_TRANSCODER_YTDLP_FORCE_IPV4`

Request-level headers allowed:

1. `userAgent`
2. `referer`

## 6. Error Hygiene

1. Return `400` for extractor/download failures.
2. Return `500` for unexpected transcode pipeline failures.
3. Keep deep diagnostics in server logs; API error messages should stay concise.

