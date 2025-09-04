#!/usr/bin/env python3
import base64
import os
from pathlib import Path
from pypdf import PdfReader, PdfWriter

# Paths
home = str(Path.home())
ROOT = Path.home() / "Desktop" / "concrete-recommendations-shareable"
DOWNLOADS = Path.home() / "Downloads"
OUTPUT_PDF = ROOT / "download" / "concrete-recommendations-shareable.pdf"
INDEX_HTML = ROOT / "index.html"

# Source PDF files
MAIN_PDF = DOWNLOADS / "Concrete recommendations and leg types (2).pdf"
APPENDIX_PDF = DOWNLOADS / "Some concrete aspects.pdf"
# Logo (found in Downloads)
LOGO_PNG = DOWNLOADS / "Wolf-Carports.png"

# Validations
for p in [MAIN_PDF, APPENDIX_PDF, LOGO_PNG]:
    if not p.exists():
        raise FileNotFoundError(f"Required file not found: {p}")

# 1) Merge PDFs into a single combined PDF
writer = PdfWriter()
for src in [MAIN_PDF, APPENDIX_PDF]:
    reader = PdfReader(str(src))
    for page in reader.pages:
        writer.add_page(page)

OUTPUT_PDF.parent.mkdir(parents=True, exist_ok=True)
with OUTPUT_PDF.open("wb") as f_out:
    writer.write(f_out)

# 2) Base64 encode assets
with LOGO_PNG.open("rb") as f:
    logo_b64 = base64.b64encode(f.read()).decode("ascii")
with MAIN_PDF.open("rb") as f:
    main_pdf_b64 = base64.b64encode(f.read()).decode("ascii")
with APPENDIX_PDF.open("rb") as f:
    appendix_pdf_b64 = base64.b64encode(f.read()).decode("ascii")
with OUTPUT_PDF.open("rb") as f:
    combined_pdf_b64 = base64.b64encode(f.read()).decode("ascii")

# 3) HTML template (self-contained)
html = f"""
<!DOCTYPE html>
<html lang=\"en\">
<head>
  <meta charset=\"utf-8\" />
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
  <title>Concrete Recommendations and Leg Types — Shareable</title>
  <style>
    :root {{
      --brand: #0f3d63;
      --accent: #ff8a00;
      --bg: #f7f9fc;
      --text: #1b1f23;
      --muted: #6b7280;
      --surface: #ffffff;
      --radius: 12px;
      --shadow: 0 6px 24px rgba(0,0,0,0.08);
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", sans-serif;
      color: var(--text);
      background: var(--bg);
      line-height: 1.55;
    }}
    header {{
      background: linear-gradient(180deg, rgba(15,61,99,0.95), rgba(15,61,99,0.88)), var(--brand);
      color: white;
      padding: 24px 20px;
      position: sticky; top: 0; z-index: 1000;
      box-shadow: var(--shadow);
    }}
    .container {{
      max-width: 1180px;
      margin: 0 auto;
      padding: 0 16px;
    }}
    .brand {{ display: flex; align-items: center; gap: 16px; }}
    .brand img {{ height: 44px; width: auto; border-radius: 6px; background: #fff; padding: 4px; }}
    .brand h1 {{ font-size: 20px; margin: 0; font-weight: 650; letter-spacing: .2px; }}

    .card {{
      background: var(--surface);
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      padding: 20px;
      margin: 18px 0;
    }}
    .actions {{ display: flex; gap: 12px; flex-wrap: wrap; }}
    .btn {{
      appearance: none; border: none; cursor: pointer;
      padding: 12px 16px; border-radius: 10px; font-weight: 600;
      background: var(--brand); color: #fff; text-decoration: none;
      box-shadow: 0 2px 10px rgba(15,61,99,.25);
    }}
    .btn.secondary {{ background: #1f2937; }}
    .meta {{ color: var(--muted); font-size: 13px; }}
    .toc a {{ color: var(--brand); text-decoration: none; }}

    .viewer {{ width: 100%; height: 85vh; border: none; border-radius: 10px; background: #111; }}
    .section-title {{ font-size: 18px; margin: 0 0 10px; color: #0f3d63; }}

    @media (max-width: 720px) {{
      .viewer {{ height: 70vh; }}
    }}

    @media print {{
      header, .actions, .toc {{ display: none !important; }}
      .card {{ box-shadow: none; border: 1px solid #ddd; }}
      .viewer {{ height: 95vh; }}
    }}
  </style>
</head>
<body>
  <header>
    <div class=\"container brand\">
      <img alt=\"Wolf Carports\" src=\"data:image/png;base64,{logo_b64}\" />
      <h1>Concrete Recommendations and Leg Types — Shareable</h1>
    </div>
  </header>

  <main class=\"container\" style=\"padding: 18px 0 32px\"> 
    <section class=\"card actions\">
      <a class=\"btn\" id=\"downloadBtn\" href=\"data:application/pdf;base64,{combined_pdf_b64}\" download=\"concrete-recommendations-shareable.pdf\">Download PDF</a>
      <a class=\"btn secondary\" href=\"#appendix\">Skip to Appendix</a>
      <div class=\"meta\">Includes all text, diagrams and images from both source PDFs.</div>
    </section>

    <section class=\"card toc\">
      <strong>Table of Contents</strong>
      <ol style=\"margin: 8px 0 0 20px;\">
        <li><a href=\"#main\">Main Document: Concrete recommendations and leg types (2)</a></li>
        <li><a href=\"#appendix\">Appendix: Some concrete aspects</a></li>
      </ol>
    </section>

    <section id=\"main\" class=\"card\">
      <h2 class=\"section-title\">Main Document</h2>
      <object class=\"viewer\" type=\"application/pdf\" data=\"data:application/pdf;base64,{main_pdf_b64}\">
        <p>Your browser cannot display embedded PDFs. <a href=\"data:application/pdf;base64,{main_pdf_b64}\" download=\"Concrete-recommendations-and-leg-types.pdf\">Download instead</a>.</p>
      </object>
    </section>

    <section id=\"appendix\" class=\"card\">
      <h2 class=\"section-title\">Appendix — Some concrete aspects</h2>
      <object class=\"viewer\" type=\"application/pdf\" data=\"data:application/pdf;base64,{appendix_pdf_b64}\">
        <p>Your browser cannot display embedded PDFs. <a href=\"data:application/pdf;base64,{appendix_pdf_b64}\" download=\"Some-concrete-aspects.pdf\">Download instead</a>.</p>
      </object>
    </section>
  </main>
</body>
</html>
"""

INDEX_HTML.write_text(html, encoding="utf-8")
print(f"Wrote {INDEX_HTML}")
print(f"Wrote {OUTPUT_PDF}")

