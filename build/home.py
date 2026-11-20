from icons import icon
from layout import head, header, footer, cta_band, wheel, ELEMENTS, PHONE_TEL


def page():
    h = head('ISEPL | Engineering the Five Elements for a Sustainable Future',
             'Integra Sustainable Enterprises (ISEPL), Hyderabad: design, supply, erection and commissioning of indoor air quality, fire suppression, water, drainage and solar solutions.')
    h += header('home')

    h += f'''<section class="hero"><div class="wrap">
  <div>
    <div class="eyebrow rv">Integra Sustainable Enterprises</div>
    <h1 class="rv d1">Engineering the <span class="grad">five elements</span> for a sustainable future.</h1>
    <p class="lead rv d2">We design, supply, install and commission the systems that keep buildings and industries breathing clean, staying fire-safe, moving water efficiently and draining responsibly. One accountable partner from concept to commissioning.</p>
    <div class="btn-row rv d3">
      <a class="btn btn-primary" href="#solutions">Explore Solutions {icon('arrow')}</a>
      <a class="btn btn-ghost" href="contact.html">Talk to an Engineer</a>
    </div>
    <div class="hero-badges rv d4">
      <span>Premium residences</span><span>Hospitals &amp; hotels</span><span>Industrial &amp; commercial</span><span>South &amp; West India</span>
    </div>
  </div>
  {wheel()}
</div></section>

<section class="scope" id="how"><div class="wrap">
  <div class="step rv"><span class="num">01</span><div><h4>Design</h4><p>Site study, engineering calculations and system selection for your application.</p></div></div>
  <div class="step rv d1"><span class="num">02</span><div><h4>Supply</h4><p>Proven, certified products sourced and delivered to site on schedule.</p></div></div>
  <div class="step rv d2"><span class="num">03</span><div><h4>Erection</h4><p>Installation by trained teams to code, with clean handovers between trades.</p></div></div>
  <div class="step rv d3"><span class="num">04</span><div><h4>Commissioning</h4><p>Testing, performance verification, documentation and after-sales support.</p></div></div>
</div></section>
'''

    # Element cards
    imgs = {
        'air': ('assets/img/air-diffuser-room.jpg', 'Calm living room with a discreet fresh-air diffuser'),
        'fire': ('assets/img/fire-curtain-hall.jpg', 'Automatic fire curtain deployed across a large opening'),
        'water': ('assets/img/water-texture.jpg', 'Clear moving water'),
        'earth': ('assets/img/siphonic-roof.jpg', 'Siphonic roof drainage layout'),
    }
    cards = ''
    for i, (k, name, skt, pg, title, short) in enumerate(ELEMENTS):
        if k == 'sky':
            media = '<div class="art art-sky"></div>'
            soon = '<span class="soonpill">Coming soon</span>'
        else:
            src, alt = imgs[k]
            media = f'<img src="{src}" alt="{alt}" loading="lazy">'
            soon = ''
        cards += f'''<a class="el-card c-{k} rv d{i % 3}" href="{pg}">{media}{soon}
  <div class="body"><span class="tag">{icon(k)} {name} · {skt}</span><h3>{title}</h3><p>{short}</p><span class="go">{'Learn more' if k == 'sky' else 'Explore solutions'} {icon('arrow')}</span></div></a>
'''
    h += f'''<section class="section" id="solutions"><div class="wrap">
  <div class="section-head center rv"><div class="eyebrow">Our Solutions</div><h2>Five elements. One integrated partner.</h2>
  <p class="lead">Every building depends on hidden systems working together. We bring air, fire, water, earth and energy under one roof, so there is one team accountable for performance.</p></div>
  <div class="el-grid">{cards}</div>
</div></section>
'''

    # ONEAIR feature
    h += f'''<section class="section warm"><div class="wrap feature">
  <div class="media rv">
    <img src="assets/img/air-living-room.jpg" alt="Elegant living room with clean, fresh indoor air" loading="lazy">
    <div class="float"><div class="live">Typical indoor readings</div>
      <div class="row"><span>PM2.5</span><b>6 µg/m³</b></div>
      <div class="row"><span>CO₂</span><b>640 ppm</b></div>
      <div class="row"><span>Pressure</span><b>Positive</b></div>
    </div>
  </div>
  <div class="rv d1">
    <div class="eyebrow" style="--accent:var(--air)">Featured · Air</div>
    <h2><span class="brandline">ONEAIR LIVING</span><br>Breathe better. Live quieter.</h2>
    <p class="lead">ONEAIR LIVING treats the entire indoor airspace as one body of air, not just pockets around a purifier. A positive-pressure, medical-grade filtered fresh air system for the whole house blocks outdoor pollution and continuously refreshes the air inside.</p>
    <div class="metrics">
      <div class="metric"><b>&lt;10</b><span>PM2.5 in single digits (µg/m³)</span></div>
      <div class="metric"><b>&lt;1000</b><span>CO₂ ppm, below the Pettenkofer limit</span></div>
      <div class="metric"><b>24/7</b><span>Clean air in every corner, every room</span></div>
    </div>
    <p class="quote">Why positive pressure? Because prevention is better than purification.</p>
    <a class="btn btn-primary" style="--accent:var(--air)" href="air.html">Discover whole-home clean air {icon('arrow')}</a>
  </div>
</div></section>
'''

    # Applications tabs
    apps = {
        'Residential': [
            ('air', 'Premium villas & residences', 'Whole-home filtered fresh air with silent, energy-efficient operation.'),
            ('air', 'VIP & political residences', 'Discreet, monitored air quality for high-security homes and offices.'),
            ('water', 'Heat pumps for hot water', 'Efficient, safe hot water for homes and residential communities.'),
            ('fire', 'Fire doors for apartments', 'Rated doors for stair, lift and shaft enclosures as per code.'),
        ],
        'Healthcare & Hospitality': [
            ('air', 'Hospitals & clinics', 'Medical-grade filtration and positive pressure for patient areas.'),
            ('air', 'Premium hotels', 'Fresh, odour-free air in guest rooms, lobbies and restaurants.'),
            ('water', 'Hotel & hospital hot water', 'Heat pumps that cut fuel bills for laundry, kitchens and rooms.'),
            ('fire', 'Corridor & compartment protection', 'Fire curtains and doors for guest corridors and hospital compartments.'),
        ],
        'Commercial': [
            ('fire', 'Electrical & IT panels', 'Automatic in-panel suppression for switchgear, server and control panels.'),
            ('fire', 'Data centres & server rooms', 'Clean-agent systems that protect equipment without water damage.'),
            ('fire', 'Fire & smoke curtains', 'Invisible compartmentation for atriums, malls and open-plan spaces.'),
            ('air', 'Offices & workspaces', 'Better air for focus, health and productivity.'),
        ],
        'Industrial': [
            ('fire', 'Lithium-ion battery systems', 'Suppression for battery energy storage, UPS rooms and EV charging.'),
            ('water', 'Process & chemical pipelines', 'Corrosion-free thermoplastic valves and piping for aggressive media.'),
            ('water', 'Emergency pipe repair', 'Repair leaks in minutes with couplings: no welding, no shutdown.'),
            ('earth', 'Factory & warehouse roofs', 'Siphonic roof drainage that handles heavy monsoon rain with smaller pipes.'),
            ('earth', 'Yards & loading bays', 'Heavy-duty surface drainage channels and special drainage products.'),
            ('water', 'Water & wastewater treatment', 'RO/UF, softening, STP/ETP and treatment chemicals.'),
        ],
    }
    tabs = ''
    panels = ''
    for i, (name, items) in enumerate(apps.items()):
        pid = 'p' + str(i)
        tabs += f'<button class="tab" role="tab" aria-selected="{"true" if i == 0 else "false"}" aria-controls="{pid}">{name}</button>'
        cards = ''
        for k, t, d in items:
            el = next(e for e in ELEMENTS if e[0] == k)
            cards += f'<a class="app c-{k}" href="{el[3]}"><span class="dot"><i></i>{el[1]}</span><h4>{t}</h4><p>{d}</p></a>'
        panels += f'<div class="panel{" on" if i == 0 else ""}" id="{pid}" role="tabpanel">{cards}</div>'
    h += f'''<section class="section soft" id="applications"><div class="wrap" data-tabs>
  <div class="section-head center rv"><div class="eyebrow">Applications</div><h2>Find the right solution for your building.</h2>
  <p class="lead">Choose your sector to see how we help projects like yours.</p></div>
  <div class="tabs rv" role="tablist">{tabs}</div>
  <div class="rv d1">{panels}</div>
</div></section>
'''

    # About / why
    h += f'''<section class="section dark" id="about"><div class="wrap">
  <div class="section-head rv"><div class="eyebrow" style="color:#7fd48a">Why ISEPL</div><h2>We treat buildings like living systems.</h2>
  <p class="lead" style="color:#b6c3d6">Integra Sustainable Enterprises is an engineering solutions company based in Hyderabad. We design and install the systems that keep air clean, water safe, fires at bay and spaces comfortable, making sure every pipe, filter, sprinkler and duct works together.</p></div>
  <div class="why">
    <div class="card rv">{icon('users')}<h3>One team for everything</h3><p>No juggling separate air, plumbing and fire contractors. Cleaner handoffs, fewer delays and better use of space.</p></div>
    <div class="card rv d1">{icon('chart')}<h3>Lower running costs</h3><p>Energy-recovery heat pumps, efficient ventilation and water reuse that bring utility bills down year after year.</p></div>
    <div class="card rv d2">{icon('cert')}<h3>Code-compliant by design</h3><p>Engineered to NBC, BIS, ASHRAE, NFPA and EN requirements for first-time inspection clearance.</p></div>
    <div class="card rv d3">{icon('tools')}<h3>Turnkey delivery</h3><p>Design, supply, erection and commissioning, with support that continues after handover.</p></div>
  </div>
</div></section>
'''

    # Regions
    reg = [
        ('air', 'Air', 'Hyderabad, Bengaluru, Chennai, Pune and Mumbai: premium villas, hospitals, premium hotels, VIP residences.'),
        ('fire', 'Fire', 'Southern states, Maharashtra and Gujarat: industrial and commercial facilities.'),
        ('water', 'Water', 'Southern and western states: industrial, commercial and residential projects.'),
        ('earth', 'Earth', 'Southern and western states: industries, warehouses and large-roof facilities.'),
    ]
    rows = ''.join(f'<div class="region c-{k} rv d{i}"><b><i></i>{n}</b><span>{t}</span></div>' for i, (k, n, t) in enumerate(reg))
    h += f'''<section class="section" id="regions"><div class="wrap regions">
  <div class="rv"><div class="eyebrow">Where We Work</div><h2>Headquartered in Hyderabad. Delivering across South &amp; West India.</h2>
  <p class="lead">Our project teams support clients across Telangana, Andhra Pradesh, Karnataka, Tamil Nadu, Kerala, Maharashtra and Gujarat.</p>
  <a class="btn btn-outline" href="contact.html" style="margin-top:12px">Discuss your location {icon('arrow')}</a></div>
  <div class="region-list">{rows}</div>
</div></section>
'''
    h += cta_band()
    h += footer()
    return h
