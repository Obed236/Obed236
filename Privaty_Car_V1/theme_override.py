from pathlib import Path

MARKER = "/* === Privaty Car light header 2026-09-13 === */"
CSS = r"""
/* === Privaty Car light header 2026-09-13 === */
.site-header{
  background:#F7F4EE !important;
  color:#111111 !important;
  border-bottom:1px solid rgba(209,174,114,.72) !important;
  backdrop-filter:blur(14px) !important;
}
.site-header .brand,
.site-header .main-nav,
.site-header .main-nav > a:not(.btn){
  color:#111111 !important;
}
.site-header .main-nav > a:not(.btn):hover{color:#765822 !important;}
.site-header .menu-btn{
  color:#111111 !important;
  border-color:#BCA77F !important;
  background:transparent !important;
}
.site-header .btn{color:#111111 !important;}
.site-header .brand-logo{
  filter:grayscale(1) invert(1) !important;
}
@media (max-width:980px){
  .site-header .main-nav{
    background:#F7F4EE !important;
    color:#111111 !important;
    border-top:1px solid rgba(209,174,114,.55) !important;
    box-shadow:0 16px 28px rgba(0,0,0,.08);
  }
}
"""


def apply():
    root = Path(__file__).resolve().parent
    css_path = root / "static" / "css" / "style.css"
    if css_path.exists():
        css = css_path.read_text(encoding="utf-8")
        if MARKER in css:
            css = css.split(MARKER)[0].rstrip() + "\n"
        css_path.write_text(css + "\n" + CSS.strip() + "\n", encoding="utf-8")

    base = root / "templates" / "base.html"
    if base.exists():
        html = base.read_text(encoding="utf-8")
        old = "{{ url_for('static', filename='css/style.css') }}"
        new = "{{ url_for('static', filename='css/style.css') }}?v=20260913-lightheader"
        if new not in html:
            html = html.replace(old, new)
        base.write_text(html, encoding="utf-8")
