from pathlib import Path
import re

MARKER = "/* === Privaty Car hero logo transparent 2026-09-13 === */"
CSS = r"""
/* === Privaty Car hero logo transparent 2026-09-13 === */
.hero-signature{
  background:transparent !important;
  border:0 !important;
  padding:0 !important;
  box-shadow:none !important;
  width:min(76%,380px) !important;
  filter:drop-shadow(0 6px 18px rgba(0,0,0,.55)) !important;
}
@media(max-width:680px){
  .hero-signature{width:74% !important;}
}
"""


def apply():
    root = Path(__file__).resolve().parent

    css_path = root / "static" / "css" / "style.css"
    if css_path.exists():
        css = css_path.read_text(encoding="utf-8")
        # A fresh Render build starts from the archived stylesheet. Keep this idempotent
        # in case the hook runs more than once in the same process.
        if MARKER in css:
            css = css.split(MARKER)[0].rstrip() + "\n"
        css_path.write_text(css + "\n" + CSS.strip() + "\n", encoding="utf-8")

    home = root / "templates" / "home.html"
    if home.exists():
        html = home.read_text(encoding="utf-8")
        html = html.replace(
            "img/privaty-logo-dark.png",
            "img/privaty-logo-transparent.png"
        )
        home.write_text(html, encoding="utf-8")

    # Force browsers to fetch the corrected CSS. The header itself is intentionally
    # left exactly as defined by the original Privaty Car theme.
    base = root / "templates" / "base.html"
    if base.exists():
        html = base.read_text(encoding="utf-8")
        token = "{{ url_for('static', filename='css/style.css') }}"
        html = re.sub(
            re.escape(token) + r"(?:\?v=[^\"']+)?",
            token + "?v=20260913-herologo",
            html,
        )
        base.write_text(html, encoding="utf-8")
