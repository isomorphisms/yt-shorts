# yt-shorts

Source files and reproducible renders for short-form videos.

Each short lives in its own directory with its sources, narration, and render script.

## Publishing

YouTube upload automation is documented in [`docs/youtube-upload.md`](docs/youtube-upload.md). The uploader runs under Grease. Push and pull-request CI only smoke-tests the uploader; an actual upload requires a manual workflow run with `publish=true`.
