# FFmpeg Presets and Quality Policy

## 1. Output Formats

Supported output formats:

1. `mp4`
2. `webm`
3. `mp3`

Base behavior:

1. `mp4` and `webm` map both video and audio streams.
2. `mp3` maps audio stream only.

## 2. Quality Presets

Public quality enum:

1. `auto`
2. `best`
3. `worst`
4. `low`
5. `medium`
6. `high`

Internal normalization:

1. `auto -> medium`
2. `best -> high`
3. `worst -> low`

## 3. CRF / QScale Mapping

### MP4 (`libx264`)

1. `high`: `-crf 20`
2. `medium`: `-crf 23`
3. `low`: `-crf 28`

### WEBM (`libvpx-vp9`)

1. `high`: `-crf 28`
2. `medium`: `-crf 33`
3. `low`: `-crf 38`

### MP3 (`libmp3lame`)

1. `high`: `-q:a 0`
2. `medium`: `-q:a 2`
3. `low`: `-q:a 5`

## 4. Thumbnail / Preview Embedding

When `embedPreviewImage=true`:

1. yt-dlp downloads and converts thumbnail to JPG.
2. ffmpeg embeds cover art for:
   - MP4: attached picture stream
   - MP3: ID3 cover art metadata
3. WEBM remains standard transcode without embedded cover art stream.

## 5. MP4 Baseline

MP4 transcode should include:

1. `-c:v libx264`
2. `-c:a aac`
3. `-movflags +faststart`
4. explicit stream mapping (`-map 0:v:0`, `-map 0:a:0`)

