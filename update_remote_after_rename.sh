#!/usr/bin/env bash
set -euo pipefail

# Usage: ./update_remote_after_rename.sh wolfcarports
# If no arg provided, defaults to 'wolfcarports'.

NEW_USER="${1:-wolfcarports}"
REPO_NAME="concrete-recommendations-shareable"
ROOT_DIR="$(cd "$(dirname "$0")" && pwd)"

cd "$ROOT_DIR"

echo "Updating remote to: https://github.com/${NEW_USER}/${REPO_NAME}.git"

git remote set-url origin "https://github.com/${NEW_USER}/${REPO_NAME}.git"
git remote -v

echo "Pushing main to new remote..."
git push -u origin main

echo "Re-assert Pages source (if needed)"
if command -v gh >/dev/null 2>&1; then
  gh api -X POST "repos/${NEW_USER}/${REPO_NAME}/pages" -f "source[branch]=main" -f "source[path]=/" || true
  echo "New Pages URL should be: https://${NEW_USER}.github.io/${REPO_NAME}/"
fi

