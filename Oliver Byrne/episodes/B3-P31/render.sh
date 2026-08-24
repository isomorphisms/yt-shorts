#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd -- "$SCRIPT_DIR/../../.." && pwd)"

exec docker run --rm \
  --user "$(id -u):$(id -g)" \
  -v "$REPO_ROOT:/manim" \
  -w "/manim/Oliver Byrne/episodes/B3-P31" \
  manimcommunity/manim:v0.19.1 \
  manim render \
    --renderer=cairo \
    --disable_caching \
    --resolution=1080,1920 \
    --fps=30 \
    --format=mp4 \
    --media_dir=media \
    --output_file=byrne-iii-31.mp4 \
    scene.py ByrneIII31
