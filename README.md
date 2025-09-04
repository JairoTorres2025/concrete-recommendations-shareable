# Wolf Carports — Training Hub (Shareable)

This system builds a self-contained, responsive site to share training materials for Wolf Reps. It currently includes the Concrete Recommendations package and provides two sections for additional content:

- Sentinels Training (materials you place in materials/sentinels)
- Onboarding (materials you place in materials/onboarding)

Branding includes the Wolf Carports logo. All text, diagrams, and images are preserved by embedding PDFs directly into the HTML pages as data URIs.

Requirements
- macOS
- Python 3 (python3)

Quick start (one-line command)

```bash
cd ~/Desktop/concrete-recommendations-shareable && ./build.sh && open index.html
```

Structure
- index.html — Training Hub homepage. Includes the Concrete Recommendations (main + appendix) with a combined Download button.
- sentinels.html — Auto-generated from PDFs in materials/sentinels.
- onboarding.html — Auto-generated from PDFs in materials/onboarding.
- materials/
  - sentinels/ — Drop any .pdf files here (e.g., Call_Scripts.pdf, Objections.pdf).
  - onboarding/ — Drop any .pdf files here (e.g., Handbook.pdf, First_Week_Checklist.pdf).
- download/concrete-recommendations-shareable.pdf — Combined PDF (main + appendix).
- build.sh — Rebuild helper (idempotent). Installs lightweight Python dependency and calls build.py.
- build.py — Generates all self-contained HTML pages and the combined PDF.
- publish.sh — Helper to publish via GitHub Pages.

Add materials and rebuild
```bash
# Example: add a Sentinels PDF and an Onboarding PDF, then rebuild and open
cp "/path/to/YourSentinelsDoc.pdf" ~/Desktop/concrete-recommendations-shareable/materials/sentinels/
cp "/path/to/YourOnboardingDoc.pdf" ~/Desktop/concrete-recommendations-shareable/materials/onboarding/
cd ~/Desktop/concrete-recommendations-shareable && ./build.sh && open index.html
```

Public URL (GitHub Pages)
- Initial publish or re-publish:
  ```bash
  cd ~/Desktop/concrete-recommendations-shareable && bash publish.sh
  ```
- Your Pages URL looks like: https://YOUR_GITHUB_USERNAME.github.io/concrete-recommendations-shareable/

After renaming your GitHub account (e.g., to wolfcarports)
- Update the Git remote and push:
  ```bash
  cd ~/Desktop/concrete-recommendations-shareable && \
  git remote set-url origin https://github.com/wolfcarports/concrete-recommendations-shareable.git && \
  git push -u origin main
  ```
- The site URL will become: https://wolfcarports.github.io/concrete-recommendations-shareable/

Optional: Custom domain (recommended)
- Point a DNS CNAME (e.g., training.wolfcarports.com) to YOUR_GITHUB_USERNAME.github.io
- Add a CNAME file to the repo with that hostname and push:
  ```bash
  cd ~/Desktop/concrete-recommendations-shareable && \
  printf "training.wolfcarports.com" > CNAME && git add CNAME && git commit -m "Add custom domain" && git push
  ```
- Then enable HTTPS in the repo’s Pages settings.

Notes
- Per your rule to delete previous versions, build.sh overwrites regenerated artifacts.
- The HTML pages are self-contained and can be shared individually if desired.
- Use underscore or readable names for PDFs; page titles are derived from filenames.

