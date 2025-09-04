#!/usr/bin/env bash
set -euo pipefail

# Rebuilds the shareable HTML and combined PDF in a clean workspace.
# Requirements:
# - macOS with Python 3 available as `python3`
# - Internet not required
# - No heavyweight brew deps needed

ROOT_DIR="$(cd "$(dirname "$0")" && pwd)"
DOWNLOAD_DIR="$ROOT_DIR/download"

# 1) Clean previous generated artifacts (preserve scripts and README)
rm -f "$ROOT_DIR/index.html" "$DOWNLOAD_DIR/concrete-recommendations-shareable.pdf"

# 2) Ensure Python deps (lightweight)
python3 -m pip install --user --quiet pypdf

# 3) Run builder
python3 "$ROOT_DIR/build.py"

# 4) Success message
printf "\nBuilt index.html and download/concrete-recommendations-shareable.pdf\nLocation: %s\n" "$ROOT_DIR"

