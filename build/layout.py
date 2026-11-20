from icons import icon, WA
import math

PHONE = '+91 99621 69456'
PHONE_TEL = '+919962169456'
EMAIL = 'isepl.india@gmail.com'
SALES = 'salesinfo.isepl@gmail.com'
ADDRESS = 'Flat No. 103, 2nd Floor, SRS Prime Meadows, Road No. 6, Krantinagar Colony, Bachupally, Hyderabad, Telangana 500090'
ADDRESS_HTML = 'Flat No. 103, 2nd Floor, SRS Prime Meadows,<br>Road No. 6, Krantinagar Colony, Bachupally,<br>Hyderabad, Telangana 500090'
WA_LINK = 'https://wa.me/919962169456?text=' + 'Hello%20ISEPL%2C%20I%27d%20like%20to%20know%20more%20about%20your%20solutions.'

ELEMENTS = [
    # key, name, sanskrit, page, title, short
    ('air', 'Air', 'Vayu', 'air.html', 'Indoor Air Quality',
     'Whole-home filtered fresh air that keeps PM2.5 in single digits and CO₂ below 1000 ppm.'),
    ('fire', 'Fire', 'Agni', 'fire.html', 'Fire Protection',
     'Panel and lithium-ion battery suppression, fire curtains, fire doors and engineered systems.'),
    ('water', 'Water', 'Jala', 'water.html', 'Water & Thermal',
     'Special-application pipelines, treatment engineering and chemicals, and heat pumps.'),
    ('earth', 'Earth', 'Prithvi', 'earth.html', 'Drainage & Harvesting',
     'Siphonic roof drainage, rainwater storage integration and surface drainage channels.'),
    ('sky', 'Space / Sky', 'Akasha', 'sky.html', 'Solar Solutions',
     'Solar products for special applications. Launching soon.'),
]


def head(title, desc, body_class=''):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#13294b">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:image" content="assets/img/logo.png">
<link rel="icon" type="image/png" href="assets/img/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Sora:wght@500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/styles.css">
</head>
<body class="{body_class}">
'''


def header(active=''):
    mega = ''
    for k, name, skt, page, title, short in ELEMENTS:
        soon = '<span class="soon">Soon</span>' if k == 'sky' else ''
        mega += (f'<a href="{page}" class="c-{k}"><span class="ic bg-c">{icon(k)}</span>'
                 f'<span><strong>{name} · {title}{soon}</strong><small>{short}</small></span></a>')
    def act(x):
        return ' class="active"' if active == x else ''
    return f'''<div class="topbar"><div class="wrap">
  <span class="tb-hide">Design · Supply · Erection · Commissioning</span>
  <div class="tb-links">
    <span>{icon('phone')}<a href="tel:{PHONE_TEL}">{PHONE}</a></span>
    <span>{icon('mail')}<a href="mailto:{SALES}">{SALES}</a></span>
  </div>
</div></div>
<header class="site-header"><div class="wrap">
  <a class="brand" href="index.html" aria-label="ISEPL home"><img src="assets/img/logo.png" alt="ISEPL, Integra Sustainable Enterprises Private Limited" width="640" height="218"></a>
  <nav class="nav" aria-label="Main">
    <a href="index.html"{act('home')}>Home</a>
    <div class="dd"><button type="button" aria-expanded="false">Solutions {icon('chev')}</button>
      <div class="mega">{mega}</div></div>
    <a href="index.html#applications"{act('apps')}>Applications</a>
    <a href="index.html#about"{act('about')}>About</a>
    <a href="contact.html"{act('contact')}>Contact</a>
    <a class="btn btn-primary" href="contact.html">Get a Consultation {icon('arrow')}</a>
  </nav>
  <button class="burger" type="button" aria-label="Open menu" aria-expanded="false">{icon('menu')}</button>
</div></header>
'''


def cta_band(title='Planning a project? Let’s engineer it together.',
             text='Share your site details and requirements. Our engineers will recommend the right solution and handle design, supply, erection and commissioning end to end.'):
    return f'''<section class="section tight"><div class="wrap">
  <div class="cta-band rv">
    <div><h2>{title}</h2><p>{text}</p></div>
    <div class="btn-row">
      <a class="btn btn-primary" href="contact.html" style="--accent:var(--brand-green)">Send an Enquiry {icon('arrow')}</a>
      <a class="btn btn-ghost" href="tel:{PHONE_TEL}">{icon('phone')} Call Us</a>
    </div>
  </div>
</div></section>
'''


def footer():
    els = ''.join(f'<li><a class="el-link c-{k}" href="{p}"><i></i>{n} · {t}</a></li>' for k, n, s, p, t, _ in ELEMENTS)
    return f'''<footer class="site-footer"><div class="wrap">
  <div class="foot-grid">
    <div>
      <a class="foot-logo" href="index.html"><img src="assets/img/logo.png" alt="ISEPL" width="640" height="218"></a>
      <p>Integra Sustainable Enterprises Private Limited designs, supplies, erects and commissions the engineered systems inside buildings and industries: clean air, fire safety, water, drainage and energy.</p>
    </div>
    <div><h4>Solutions</h4><ul>{els}</ul></div>
    <div><h4>Company</h4><ul>
      <li><a href="index.html#about">About ISEPL</a></li>
      <li><a href="index.html#how">How We Work</a></li>
      <li><a href="index.html#applications">Applications</a></li>
      <li><a href="index.html#regions">Regions Served</a></li>
      <li><a href="contact.html">Contact</a></li>
    </ul></div>
    <div><h4>Get in touch</h4><ul>
      <li>{ADDRESS_HTML}</li>
      <li><a href="tel:{PHONE_TEL}">{PHONE}</a></li>
      <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
      <li><a href="mailto:{SALES}">{SALES}</a></li>
    </ul></div>
  </div>
  <div class="foot-bottom">
    <span>© <span id="yr">2026</span> Integra Sustainable Enterprises Pvt. Ltd. All rights reserved.</span>
    <span>Engineering the Five Elements for a Sustainable Future</span>
  </div>
</div></footer>
<a class="wa-float" href="{WA_LINK}" target="_blank" rel="noopener" aria-label="Chat on WhatsApp">{WA}</a>
<script src="assets/js/main.js"></script>
</body>
</html>
'''


COLORS = {'air': '#1ba3b8', 'fire': '#f07d1a', 'water': '#2c7be5', 'earth': '#3fa34d', 'sky': '#7b4bc4'}


def wheel():
    """Interactive five-element wheel, echoing the ISEPL logo."""
    cx = cy = 250
    r1, r2 = 132, 245
    order = [('fire', -90), ('water', -18), ('earth', 54), ('sky', 126), ('air', 198)]
    info = {e[0]: e for e in ELEMENTS}
    gap = 1.6
    segs = ''
    for k, a0 in order:
        a1 = a0 + 72
        s, e = math.radians(a0 + gap), math.radians(a1 - gap)
        # inner gap smaller in angle terms
        si, ei = math.radians(a0 + gap * r2 / r1), math.radians(a1 - gap * r2 / r1)
        p = (f'M{cx + r2 * math.cos(s):.1f},{cy + r2 * math.sin(s):.1f} '
             f'A{r2},{r2} 0 0 1 {cx + r2 * math.cos(e):.1f},{cy + r2 * math.sin(e):.1f} '
             f'L{cx + r1 * math.cos(ei):.1f},{cy + r1 * math.sin(ei):.1f} '
             f'A{r1},{r1} 0 0 0 {cx + r1 * math.cos(si):.1f},{cy + r1 * math.sin(si):.1f} Z')
        mid = math.radians(a0 + 36)
        ix, iy = cx + 178 * math.cos(mid), cy + 178 * math.sin(mid)
        _, name, skt, page, title, short = info[k]
        label = 'SKY' if k == 'sky' else name.upper()
        segs += (f'<a href="{page}" class="seg" tabindex="0" data-name="{name} · {skt}" data-title="{title}" '
                 f'data-desc="{short}" data-color="{COLORS[k]}" aria-label="{name}: {title}">'
                 f'<path d="{p}" fill="{COLORS[k]}"/>'
                 f'<g transform="translate({ix - 17:.1f},{iy - 26:.1f}) scale(1.42)" color="#fff">{icon(k)}</g>'
                 f'<text class="lbl" x="{ix:.1f}" y="{iy + 30:.1f}" text-anchor="middle">{label}</text></a>')
    # nested svgs need explicit size
    segs = segs.replace('<svg viewBox="0 0 24 24"', '<svg width="24" height="24" viewBox="0 0 24 24"')
    return f'''<div class="wheel rv d2">
  <div class="orbit"></div>
  <svg class="ring" viewBox="0 0 500 500" role="img" aria-label="The five elements">{segs}</svg>
  <div class="core"><div><small>Five Elements</small><strong>One Integrated Partner</strong><span>Hover an element to explore</span></div></div>
</div>'''
