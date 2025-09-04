# Concrete Recommendations — Shareable Package

This folder contains a self-contained, responsive HTML for sharing and viewing the following documents together:

- Concrete recommendations and leg types (2).pdf
- Some concrete aspects.pdf (appendix)

Branding includes the Wolf Carports logo. All text, diagrams, and images are preserved via embedded PDFs in the HTML.

Requirements
- macOS
- Python 3 (python3)

Quick start (one-line command)

```bash
cd ~/Desktop/concrete-recommendations-shareable && ./build.sh && open index.html
```

Files
- index.html — Single-file, self-contained HTML (embeds both PDFs and the logo as base64). Includes a Download PDF button for a combined PDF.
- download/concrete-recommendations-shareable.pdf — Combined PDF (main + appendix).
- build.sh — Rebuild helper (idempotent). Installs lightweight Python dependency and calls build.py.
- build.py — Merges PDFs and renders the self-contained HTML with styling.

Rebuild
- Re-run the one-liner above or:
  ```bash
  cd ~/Desktop/concrete-recommendations-shareable
  ./build.sh
  ```

Public URL (GitHub Pages)
- If you want a public URL, run the publish script below once you’re logged in with GitHub CLI (gh). If gh is not installed or authenticated, install and login first:
  ```bash
  brew install gh && gh auth login
  ```
- Then publish (one-liner):
  ```bash
  cd ~/Desktop/concrete-recommendations-shareable && bash publish.sh
  ```

Notes
- Per your rule to delete previous versions, build.sh overwrites regenerated artifacts.
- The HTML is self-contained and can be sent as a single file.

