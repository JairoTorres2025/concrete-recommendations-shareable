#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")" && pwd)"

if ! command -v gh >/dev/null 2>&1; then
  echo "GitHub CLI (gh) is not installed. Please install with: brew install gh" >&2
  exit 1
fi

if ! gh auth status >/dev/null 2>&1; then
  echo "You are not authenticated with GitHub CLI. Run: gh auth login" >&2
  exit 1
fi

cd "$ROOT_DIR"

# Initialize repo if needed
if [ ! -d .git ]; then
  git init
  git add .
  git commit -m "Initial publish"
  DEFAULT_BRANCH="main"
  git branch -M "$DEFAULT_BRANCH"
  # Create remote repo and push
  gh repo create concrete-recommendations-shareable --public --source=. --remote=origin --push
else
  git add .
  git commit -m "Update site" || true
  git push -u origin HEAD
fi

# Enable and deploy Pages from the main branch
if gh help pages >/dev/null 2>&1; then
  gh pages enable --source=main --branch=main || true
  # Newer gh supports deploy from a folder; here root is fine
  gh pages deploy --branch=main --force --directory . || true
else
  echo "'gh pages' subcommand not available. Configure Pages in repo Settings -> Pages (source: main)." >&2
fi

echo "If Pages is enabled, your site will be available shortly at:"
echo "  https://$(gh api user --jq .login).github.io/concrete-recommendations-shareable/"
