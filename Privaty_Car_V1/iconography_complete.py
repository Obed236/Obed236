from pathlib import Path

MARKER = "/* === Privaty Car complete iconography 2026-09-13 === */"

ICONS = {
    "phone": '<svg class="pc-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M6 3l3 4-2 2c2 4 4 6 8 8l2-2 4 3-2 3c-1 1-3 1-5 0C8 18 4 14 3 9c-1-2-1-4 0-5z"/></svg>',
    "mail": '<svg class="pc-icon" viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="1"/><path d="M3 7l9 7 9-7"/></svg>',
    "clock": '<svg class="pc-icon" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>',
    "quote": '<svg class="pc-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M5 7h6v6H7c0 2 1 3 3 4M14 7h6v6h-4c0 2 1 3 3 4"/></svg>',
    "shield": '<svg class="pc-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3l7 3v5c0 5-3 8-7 10-4-2-7-5-7-10V6z"/><path d="M9 12l2 2 4-4"/></svg>',
    "user": '<svg class="pc-icon" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="8" r="3"/><path d="M5 21v-2a7 7 0 0114 0v2"/></svg>',
    "doc": '<svg class="pc-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M6 3h8l4 4v14H6zM14 3v5h5M9 12h6M9 16h6"/></svg>',
    "pin": '<svg class="pc-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 21s7-6 7-12a7 7 0 10-14 0c0 6 7 12 7 12z"/><circle cx="12" cy="9" r="2"/></svg>',
    "plane": '<svg class="pc-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M2 16l7-4 13-6-6 13-4 3-1-5-5-1z"/></svg>',
    "briefcase": '<svg class="pc-icon" viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="7" width="18" height="12"/><path d="M8 7V5h8v2M3 12h18"/></svg>',
    "wheel": '<svg class="pc-icon" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="8"/><circle cx="12" cy="12" r="2"/><path d="M12 4v6M4 12h6M14 12h6M12 14v6"/></svg>',
    "car": '<svg class="pc-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M4 15l2-6h12l2 6v4h-2v-2H6v2H4zM7 9l2-3h6l2 3M7 14h.01M17 14h.01"/></svg>',
    "check": '<svg class="pc-icon" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M8 12l3 3 5-6"/></svg>',
    "info": '<svg class="pc-icon" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 11v6M12 7h.01"/></svg>',
    "route": '<svg class="pc-icon" viewBox="0 0 24 24" aria-hidden="true"><circle cx="5" cy="6" r="2"/><circle cx="19" cy="18" r="2"/><path d="M7 6h4a3 3 0 010 6H9a3 3 0 000 6h8"/></svg>',
    "wa": '<svg class="pc-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M20 11.5a8 8 0 01-12 7L4 20l1.5-4A8 8 0 1120 11.5z"/><path d="M9 8c.5 3 2 4.5 5 6l2-1"/></svg>',
}

CSS = r'''
/* === Privaty Car complete iconography 2026-09-13 === */
.pc-icon{width:1.15em;height:1.15em;display:inline-block;fill:none;stroke:currentColor;stroke-width:1.65;stroke-linecap:round;stroke-linejoin:round;vertical-align:-.16em;flex:0 0 auto}
.pc-icon-box{width:58px;height:58px;border:1px solid #000;display:grid;place-items:center;color:#765822;margin-bottom:20px}.pc-icon-box .pc-icon{width:26px;height:26px}
.pc-info-list{display:grid;gap:0;border-top:1px solid #ddd;margin:22px 0}.pc-info-row{display:flex;gap:13px;align-items:flex-start;padding:15px 0;border-bottom:1px solid #ddd}.pc-info-row>.pc-icon{color:#765822;width:20px;height:20px;margin-top:3px}.pc-info-row strong{display:block;font-weight:500}.pc-info-row p{margin:2px 0 0;color:#555;font-size:.9rem}
.icon-contact a,.icon-contact>div{display:flex!important;grid-template-columns:none!important;gap:13px;align-items:flex-start}.icon-contact .pc-icon{color:#765822;width:20px;height:20px;margin-top:3px}.icon-contact span{display:grid}
.contact-visual{margin-top:28px;border:1px solid #000;min-height:230px;overflow:hidden}.contact-visual img{width:100%;height:100%;object-fit:cover;filter:saturate(.8) contrast(1.03)}
.post-icon{display:grid;place-items:center;width:44px;height:44px;border:1px solid #000;color:#765822;margin-bottom:18px}.post-icon .pc-icon{width:20px;height:20px}
.status-icon .pc-icon{width:34px;height:34px}.status-icon.status-404{font-size:0}.whatsapp .pc-icon{width:22px;height:22px}
.article-cta .pc-icon-box{margin-bottom:18px}.legal-copy h2{display:flex;align-items:center;gap:10px}.legal-copy h2 .pc-icon{color:#765822;width:20px;height:20px}
'''


def patch(path, old, new):
    if not path.exists():
        return
    text = path.read_text(encoding="utf-8")
    if old in text:
        path.write_text(text.replace(old, new), encoding="utf-8")


def apply():
    root = Path(__file__).resolve().parent
    css_path = root / "static/css/style.css"
    if css_path.exists():
        css = css_path.read_text(encoding="utf-8")
        if MARKER in css:
            css = css.split(MARKER)[0].rstrip() + "\n"
        css_path.write_text(css + "\n" + CSS.strip() + "\n", encoding="utf-8")

    # Contact: iconography for every contact method + brand photograph.
    p = root / "templates/contact.html"
    old = '<div><h2>Coordonnées</h2><div class="contact-list"><a href="tel:{{ site.contact_phone|replace(\' \', \'\') }}"><small>Téléphone</small>{{ site.contact_phone }}</a><a href="mailto:{{ site.contact_email }}"><small>Email</small>{{ site.contact_email }}</a><div><small>Horaires</small>{{ site.contact_hours }}</div></div></div>'
    new = '<div><h2>Coordonnées</h2><div class="contact-list icon-contact"><a href="tel:{{ site.contact_phone|replace(\' \', \'\') }}">' + ICONS["phone"] + '<span><small>Téléphone</small>{{ site.contact_phone }}</span></a><a href="mailto:{{ site.contact_email }}">' + ICONS["mail"] + '<span><small>Email</small>{{ site.contact_email }}</span></a><div>' + ICONS["clock"] + '<span><small>Horaires</small>{{ site.contact_hours }}</span></div></div><div class="contact-visual"><img src="{{ url_for(\'static\', filename=\'img/service-premium.jpg\') }}" alt="Chauffeur Privaty Car accueillant un client"></div></div>'
    patch(p, old, new)

    # Testimonials: trust iconography.
    p = root / "templates/testimonials.html"
    old = '<div><span class="eyebrow">TRANSPARENCE</span><h2>Les premiers témoignages vérifiés seront ajoutés ici.</h2></div><div><p>Les avis d’entreprises clientes et de chauffeurs partenaires seront publiés après autorisation, avec leur contexte réel.</p>'
    new = '<div><span class="pc-icon-box">' + ICONS["quote"] + '</span><span class="eyebrow">TRANSPARENCE</span><h2>Les premiers témoignages vérifiés seront ajoutés ici.</h2></div><div><div class="pc-info-list"><div class="pc-info-row">' + ICONS["shield"] + '<span><strong>Avis authentiques</strong><p>Uniquement des retours vérifiés et validés.</p></span></div><div class="pc-info-row">' + ICONS["user"] + '<span><strong>Retours réels</strong><p>Entreprises clientes et chauffeurs partenaires.</p></span></div><div class="pc-info-row">' + ICONS["doc"] + '<span><strong>Contexte transparent</strong><p>Publication après autorisation.</p></span></div></div><p>Les avis d’entreprises clientes et de chauffeurs partenaires seront publiés après autorisation, avec leur contexte réel.</p>'
    patch(p, old, new)

    # Blog and article CTA.
    p = root / "templates/blog.html"
    patch(p, '<article class="post-card"><span class="post-cat">{{ post.category }}</span>', '<article class="post-card"><span class="post-icon">' + ICONS["doc"] + '</span><span class="post-cat">{{ post.category }}</span>')
    p = root / "templates/post.html"
    patch(p, '<div class="article-cta"><h2>Besoin d’un chauffeur privé pour votre entreprise ?</h2>', '<div class="article-cta"><span class="pc-icon-box">' + ICONS["car"] + '</span><h2>Besoin d’un chauffeur privé pour votre entreprise ?</h2>')

    # Local city pages.
    p = root / "templates/city.html"
    old = '<div><span class="eyebrow">SERVICE LOCAL</span><h2>Un service professionnel adapté à vos déplacements.</h2></div><div><p>'
    new = '<div><span class="pc-icon-box">' + ICONS["pin"] + '</span><span class="eyebrow">SERVICE LOCAL</span><h2>Un service professionnel adapté à vos déplacements.</h2></div><div><div class="pc-info-list"><div class="pc-info-row">' + ICONS["plane"] + '<span>Transferts gare et aéroport</span></div><div class="pc-info-row">' + ICONS["briefcase"] + '<span>Rendez-vous d’affaires</span></div><div class="pc-info-row">' + ICONS["wheel"] + '<span>Mise à disposition</span></div></div><p>'
    patch(p, old, new)

    # Status pages.
    p = root / "templates/payment_success.html"
    patch(p, '<span class="status-icon">✓</span>', '<span class="status-icon">' + ICONS["check"] + '</span>')
    patch(p, '<span class="status-icon">i</span>', '<span class="status-icon">' + ICONS["info"] + '</span>')
    p = root / "templates/404.html"
    patch(p, '<span class="status-icon">404</span>', '<span class="status-icon status-404">' + ICONS["route"] + '</span>')

    # Legal/privacy headings receive restrained document/security iconography.
    p = root / "templates/privacy.html"
    if p.exists():
        text = p.read_text(encoding="utf-8")
        if 'data-pc-privacy-icons' not in text:
            text = text.replace('<section class="section">', '<span data-pc-privacy-icons hidden></span><section class="section">', 1)
            text = text.replace('<h2>Données collectées</h2>', '<h2>' + ICONS["doc"] + ' Données collectées</h2>')
            text = text.replace('<h2>Finalités</h2>', '<h2>' + ICONS["shield"] + ' Finalités</h2>')
            text = text.replace('<h2>Mesure d’audience</h2>', '<h2>' + ICONS["info"] + ' Mesure d’audience</h2>')
            text = text.replace('<h2>Durée et droits</h2>', '<h2>' + ICONS["user"] + ' Durée et droits</h2>')
            p.write_text(text, encoding="utf-8")
    p = root / "templates/legal.html"
    if p.exists():
        text = p.read_text(encoding="utf-8")
        if 'data-pc-legal-icons' not in text:
            text = text.replace('<section class="section">', '<span data-pc-legal-icons hidden></span><section class="section">', 1)
            text = text.replace('<h2>Éditeur du site</h2>', '<h2>' + ICONS["doc"] + ' Éditeur du site</h2>')
            text = text.replace('<h2>Hébergement</h2>', '<h2>' + ICONS["shield"] + ' Hébergement</h2>')
            p.write_text(text, encoding="utf-8")

    # Replace the textual WA badge if an earlier patch has not already done so.
    p = root / "templates/base.html"
    if p.exists():
        text = p.read_text(encoding="utf-8")
        text = text.replace('aria-label="Contacter Privaty Car sur WhatsApp">WA</a>', 'aria-label="Contacter Privaty Car sur WhatsApp">' + ICONS["wa"] + '</a>')
        # Cache-bust the completed iconography stylesheet.
        token = "{{ url_for('static', filename='css/style.css') }}"
        import re
        text = re.sub(re.escape(token) + r'(?:\?v=[^\"\']+)?', token + '?v=20260913-iconography-complete', text)
        p.write_text(text, encoding="utf-8")
