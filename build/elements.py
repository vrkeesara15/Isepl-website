from icons import icon
from layout import head, header, footer, cta_band, ELEMENTS


def prod_card(i, p):
    title, desc, points = p['title'], p['desc'], p['points']
    if p.get('img'):
        cls = ' ' + p['fit'] if p.get('fit') else ''
        bg = f' style="background:{p["bg"]}"' if p.get('bg') else ''
        media = f'<div class="ph{cls}"{bg}><img src="{p["img"]}" alt="{p.get("alt", title)}" loading="lazy"></div>'
    else:
        media = f'<div class="ph icon">{icon(p["icon"])}</div>'
    pts = ''.join(f'<li>{x}</li>' for x in points)
    return f'<article class="prod rv d{i % 3}" id="{p.get("id", "")}">{media}<div class="bd"><h3>{title}</h3><p>{desc}</p><ul>{pts}</ul></div></article>'


def element_page(d):
    k = d['key']
    el = next(e for e in ELEMENTS if e[0] == k)
    h = head(d['meta_title'], d['meta_desc'], 'el-' + k)
    h += header('solutions')
    sub = ''.join(f'<a href="#{a}">{t}</a>' for a, t in d['subnav'])
    h += f'''<section class="page-hero">
  <img src="{d['hero_img']}" alt="" style="object-position:{d.get('hero_pos', 'center')}">
  <div class="wrap">
    <div class="crumbs rv"><a href="index.html">Home</a> / <a href="index.html#solutions">Solutions</a> / {el[1]}</div>
    <div class="chip-el rv">{icon(k)}</div>
    <div class="eyebrow rv">{el[1]} · {el[2]} · {el[4]}</div>
    <h1 class="rv d1">{d['h1']}</h1>
    <p class="lead rv d2">{d['lead']}</p>
    <div class="btn-row rv d3"><a class="btn btn-primary" href="contact.html?interest={k}">Request a Proposal {icon('arrow')}</a><a class="btn btn-ghost" href="#solutions">View solutions</a></div>
  </div>
</section>
<nav class="subnav" aria-label="On this page"><div class="wrap">{sub}</div></nav>
'''
    h += d['body']
    grid_cls = 'prod-grid two' if d.get('two') else 'prod-grid'
    prods = ''.join(prod_card(i, p) for i, p in enumerate(d['products']))
    h += f'''<section class="section soft" id="solutions"><div class="wrap">
  <div class="section-head rv"><div class="eyebrow">Solutions</div><h2>{d['sol_title']}</h2><p class="lead">{d['sol_lead']}</p></div>
  <div class="{grid_cls}">{prods}</div>
</div></section>
'''
    h += d.get('after', '')
    chips = ''.join(f'<span>{c}</span>' for c in d['apps'])
    h += f'''<section class="section dark" id="applications"><div class="wrap split" style="align-items:start">
  <div class="rv"><div class="eyebrow">Applications &amp; Markets</div><h2>{d['apps_title']}</h2><p class="lead" style="color:#b6c3d6">{d['apps_lead']}</p></div>
  <div class="rv d1"><div class="chips">{chips}</div>
    <div style="margin-top:34px;padding-top:26px;border-top:1px solid rgba(255,255,255,.1)"><div class="eyebrow" style="margin-bottom:12px">Regions served</div><p style="color:#e3eaf3;margin:0">{d['regions']}</p></div>
  </div>
</div></section>
'''
    h += cta_band(d.get('cta_title', f'Let’s discuss your {el[4].lower()} requirements.'),
                  'Tell us about your site and application. We will recommend the right system and take care of design, supply, erection and commissioning.')
    h += footer()
    return h


def steps(items):
    return '<div class="steps">' + ''.join(f'<div class="s rv d{i}"><h3>{t}</h3><p>{p}</p></div>' for i, (t, p) in enumerate(items)) + '</div>'


# ------------------------------------------------------------------ AIR
AIR = dict(
    key='air',
    meta_title='Whole-Home Clean Air | ONEAIR LIVING | ISEPL',
    meta_desc='Positive-pressure, medical-grade filtered fresh air for premium villas, hospitals, hotels and VIP residences. PM2.5 in single digits, CO2 below 1000 ppm.',
    hero_img='assets/img/air-diffuser-room.jpg', hero_pos='center 30%',
    h1='Clean air in every corner, 24/7.',
    lead='ONEAIR LIVING treats the entire indoor airspace as one body of air, not just pockets around a purifier. Medical-grade filtered fresh air, delivered under gentle positive pressure, keeps outdoor pollution out and refreshes the air inside continuously.',
    subnav=[('approach', 'The ONEAIR approach'), ('how', 'How it works'), ('solutions', 'Solutions'), ('applications', 'Applications')],
    body=f'''<section class="section" id="approach"><div class="wrap split">
  <div class="rv">
    <div class="eyebrow">ONEAIR LIVING · Breathe better, live quieter</div>
    <h2>Air treated as ONE, not in pockets.</h2>
    <p class="lead">Conventional purifiers clean the air near the machine, leaving polluted zones elsewhere. Our whole-space system controls fresh air intake, filters it to medical grade and distributes it evenly, so every room gets the same quality of air.</p>
    <ul class="ticks">
      <li>Fresh, filtered air is gently pushed into the home</li>
      <li>Indoor pressure stays slightly higher than outside, so unfiltered air, dust and pollutants cannot leak in</li>
      <li>Indoor pollutants and CO₂ are continuously diluted</li>
      <li>No hotspots, no stagnant zones and no clutter of portable devices</li>
    </ul>
  </div>
  <div class="media rv d1"><img src="assets/img/air-living-room.jpg" alt="Living room with whole-home fresh air" loading="lazy" style="aspect-ratio:4/4.4"></div>
</div></section>

<section class="section tight warm"><div class="wrap">
  <div class="stats">
    <div class="stat rv"><b>&lt;10</b><span>PM2.5 maintained in single digits (µg/m³), well within the WHO guideline of 15</span></div>
    <div class="stat rv d1"><b>&lt;1000</b><span>CO₂ kept below 1000 ppm (the Pettenkofer limit) for alertness and better sleep</span></div>
    <div class="stat rv d2"><b>100%</b><span>Of the indoor volume treated as one, every room and every corner</span></div>
    <div class="stat rv d3"><b>24/7</b><span>Continuous, silent, energy-efficient operation with real-time monitoring</span></div>
  </div>
</div></section>

<section class="section" id="how"><div class="wrap">
  <div class="section-head rv"><div class="eyebrow">How it works</div><h2>Prevention is better than purification.</h2><p class="lead">A compact fresh-air unit outside the living space draws in outdoor air, cleans it and delivers it through discreet ducted or ductless distribution.</p></div>
  {steps([('Draw in & filter', 'Outdoor air passes through multi-stage, medical-grade filtration that captures fine dust, PM2.5, pollen and allergens.'),
          ('Pressurise', 'Filtered air keeps the home at a slight positive pressure, sealing out unfiltered infiltration through gaps, doors and windows.'),
          ('Dilute & monitor', 'Fresh air continuously dilutes CO₂ and VOCs, while sensors track PM2.5 and CO₂ in real time.')])}
  <div class="prod-grid two" style="margin-top:64px">
    <div class="prod rv"><div class="ph"><img src="assets/img/air-unit-wall.jpg" alt="Wall-mounted fresh air unit on a terrace" loading="lazy" style="object-position:center 35%"></div><div class="bd"><h3>Discreet outdoor installation</h3><p>The fresh-air unit mounts on an external wall or terrace, keeping noise and maintenance out of the living space.</p></div></div>
    <div class="prod rv d1"><div class="ph"><img src="assets/img/air-unit-soffit.jpg" alt="Fresh air unit mounted under a balcony" loading="lazy" style="object-position:center 55%"></div><div class="bd"><h3>Fits new and existing homes</h3><p>Designed for apartments and villas, both new builds and older constructions, with ducted or ductless distribution.</p></div></div>
  </div>
</div></section>
''',
    sol_title='Indoor air quality solutions',
    sol_lead='From a single villa to a multi-storey hospital, we design the right combination of fresh air, filtration and monitoring.',
    products=[
        dict(icon='house', title='Whole-home positive-pressure fresh air', desc='The core ONEAIR LIVING system: filtered fresh air for the entire home under gentle positive pressure.',
             points=['Blocks outdoor pollution at the source', 'Even air quality in every room', 'Silent, energy-efficient operation']),
        dict(icon='filter', title='Medical-grade filtration', desc='Multi-stage filtration including HEPA-class media and optional UV-C for anti-pathogen treatment.',
             points=['Captures PM2.5, PM10, pollen and allergens', 'Suitable for clinics and patient areas', 'Easy, scheduled filter service']),
        dict(icon='sensor', title='Real-time IAQ monitoring', desc='CO₂, PM2.5 and VOC sensors make the invisible visible, with live readings and alerts.',
             points=['Live dashboards for homes and facilities', 'Data to verify WHO-aligned targets', 'Automatic fan-speed control']),
        dict(icon='recover', title='Energy-recovery ventilation', desc='Heat and energy recovery that brings in fresh air while retaining indoor cooling.',
             points=['Lower air-conditioning load', 'Balanced ventilation for large homes', 'Ideal for always-closed, air-conditioned spaces']),
        dict(icon='grid', title='Commercial HVAC air purification', desc='In-duct air scrubbing and filtration upgrades for offices, hotels and hospitals.',
             points=['Duct-mounted filtration and UV-C', 'Retrofit to existing HVAC', 'Continuous particulate mapping']),
        dict(icon='shield', title='Clean-air zones for critical spaces', desc='Higher-pressure, higher-filtration zones for bedrooms, nurseries, ICUs and VIP suites.',
             points=['Tailored air-change rates', 'Positive pressure isolation', 'Independent monitoring per zone']),
    ],
    apps_title='Built for spaces where air matters most.',
    apps_lead='We focus on premium projects where occupants expect, and notice, the best indoor air.',
    apps=['Premium villas', 'Luxury apartments', 'Hospitals', 'Clinics & wellness centres', 'Premium hotels', 'Politician & VIP residences', 'Offices & workspaces', 'Gyms & studios', 'Schools & learning spaces', 'Retail & commercial'],
    regions='Hyderabad · Bengaluru · Chennai · Pune · Mumbai',
    cta_title='Breathe better at home. Book an air quality consultation.',
)

# ------------------------------------------------------------------ FIRE
FIRE = dict(
    key='fire',
    meta_title='Fire Suppression & Protection | ISEPL',
    meta_desc='Electrical and IT panel fire suppression, lithium-ion battery fire suppression, clean agent systems, fire curtains and fire doors for industrial and commercial buildings.',
    hero_img='assets/img/fire-curtain-hall.jpg', hero_pos='center',
    h1='Stop fire where it starts. Contain it where it spreads.',
    lead='Engineered fire suppression and passive fire protection for industrial and commercial facilities: from automatic in-panel systems and lithium-ion battery protection to fire curtains and rated fire doors.',
    subnav=[('risks', 'Critical risks'), ('solutions', 'Solutions'), ('standards', 'Standards'), ('applications', 'Applications')],
    body=f'''<section class="section" id="risks"><div class="wrap">
  <div class="section-head rv"><div class="eyebrow">Critical risks</div><h2>Modern facilities face modern fire risks.</h2><p class="lead">Most fires in commercial and industrial buildings start inside equipment: electrical panels, server racks and battery systems. Targeted, automatic suppression stops them early, before they can spread or force a shutdown.</p></div>
  <div class="stats">
    <div class="stat rv">{icon('panel', ' style="width:34px;height:34px;color:var(--fire);margin-bottom:14px"')}<b style="font-size:1.25rem">Electrical &amp; IT panels</b><span>Overheating, arcing and loose connections inside enclosed panels.</span></div>
    <div class="stat rv d1">{icon('battery', ' style="width:34px;height:34px;color:var(--fire);margin-bottom:14px"')}<b style="font-size:1.25rem">Lithium-ion batteries</b><span>Thermal runaway in battery storage, UPS rooms and EV charging.</span></div>
    <div class="stat rv d2">{icon('server', ' style="width:34px;height:34px;color:var(--fire);margin-bottom:14px"')}<b style="font-size:1.25rem">Data &amp; control rooms</b><span>High-value equipment that cannot tolerate water or downtime.</span></div>
    <div class="stat rv d3">{icon('users', ' style="width:34px;height:34px;color:var(--fire);margin-bottom:14px"')}<b style="font-size:1.25rem">Life safety</b><span>Smoke and fire spread through openings, atriums and escape routes.</span></div>
  </div>
</div></section>
''',
    sol_title='Fire suppression & protection solutions',
    sol_lead='Active suppression to stop fire at the source, and passive protection to keep escape routes and compartments safe.',
    products=[
        dict(icon='panel', title='Electrical & IT panel fire suppression', desc='Automatic, self-contained suppression installed inside switchgear, MCC, PLC, server and control panels.',
             points=['Detects and suppresses at the point of origin', 'No external power required', 'Clean agent: no residue, no damage to equipment', 'Direct and indirect discharge options']),
        dict(icon='battery', title='Lithium-ion battery fire suppression', desc='Purpose-designed protection for battery energy storage, UPS battery rooms, EV charging and battery manufacturing.',
             points=['Early detection of off-gassing and heat', 'Suppression and cooling to tackle thermal runaway', 'Rack, cabinet and container level solutions']),
        dict(icon='server', title='Clean agent & inert gas systems', desc='Total flooding systems for data centres, server rooms, control rooms and archives.',
             points=['Safe for occupied spaces', 'No water damage to critical assets', 'Aspirating smoke detection for very early warning', 'Integration with fire alarm and BMS']),
        dict(icon='mist', title='Water mist, sprinkler & hydrant networks', desc='Engineered water-based protection, from high-pressure water mist to sprinkler grids, hydrants and pump rooms.',
             points=['Wet-pipe and pre-action sprinkler systems', 'Hydrant networks and pump rooms', 'Low water use with water mist']),
        dict(img='assets/img/fire-curtain-accordion.jpg', title='Fire & smoke curtains', desc='Automatic curtains that stay hidden until needed, then deploy to compartmentalise openings, atriums and lobbies.',
             points=['Automatic, accordion, egress and fixed types', 'Tested to EN 1634-1 and EN 12101-1', 'Up to 120 minutes integrity and radiation performance', 'Large openings with no visible barrier']),
        dict(img='assets/img/fire-door-glazed.jpg', title='Fire doors & glazed fire partitions', desc='Rated steel, shaft and glazed fire doors for staircases, lift lobbies, shafts and corridors.',
             points=['30 to 120 minute ratings', 'Tested to IS 3614', 'Single and double leaf, glazed options', 'Standard and custom colours'], fit=''),
    ],
    after=f'''<section class="section" id="standards"><div class="wrap split">
  <div class="media rv"><img src="assets/img/fire-door-red.jpg" alt="Rated steel fire exit door" loading="lazy" style="aspect-ratio:4/3.4"></div>
  <div class="rv d1"><div class="eyebrow">Compliance</div><h2>Designed for code. Tested to international standards.</h2>
    <p class="lead">We select and engineer systems that meet the National Building Code and the latest Part F fire and life safety provisions, together with international test standards.</p>
    <ul class="ticks">
      <li>Fire doors with 30 to 120 minute ratings for stairwells, lift lobbies, shafts and basements</li>
      <li>Fire curtains tested for integrity (E), radiation (EW), insulation (EI) and smoke control (Sa)</li>
      <li>Suppression designed in line with NFPA and relevant IS standards</li>
      <li>Documentation that supports first-time inspection clearance</li>
    </ul>
    <div class="chips"><span>NBC</span><span>IS 3614</span><span>EN 1634-1</span><span>EN 12101-1</span><span>NFPA</span></div>
  </div>
</div></section>
''',
    apps_title='Protecting industrial and commercial assets.',
    apps_lead='Our fire solutions focus on industrial and commercial facilities where equipment uptime and life safety are critical.',
    apps=['Manufacturing plants', 'Electrical substations & switch rooms', 'Data centres & server rooms', 'Battery energy storage (BESS)', 'UPS & battery rooms', 'EV charging hubs', 'Warehouses & logistics', 'Malls & commercial complexes', 'Hospitals', 'Hotels', 'High-rise buildings', 'Airports & metro'],
    regions='Telangana · Andhra Pradesh · Karnataka · Tamil Nadu · Kerala · Maharashtra · Gujarat',
    cta_title='Protect your panels, batteries and people.',
)

# ------------------------------------------------------------------ WATER
WATER = dict(
    key='water',
    meta_title='Water Pipelines, Treatment & Heat Pumps | ISEPL',
    meta_desc='Special-application pipeline solutions, pipe repair couplings, thermoplastic valves, water treatment engineering and chemicals, and heat pumps for industrial, commercial and residential projects.',
    hero_img='assets/img/water-texture.jpg', hero_pos='center',
    h1='Water that moves safely, stays clean and heats efficiently.',
    lead='Complete water solutions for industrial, commercial and residential projects: special-application pipelines and valves, fast leak repair, treatment engineering and chemicals, and energy-saving heat pumps.',
    subnav=[('solutions', 'Solutions'), ('repair', 'Repair without welding'), ('applications', 'Applications')],
    body='',
    sol_title='Pipelines, treatment & heating',
    sol_lead='Three capabilities, one team: distribute water and fluids reliably, treat it to the right standard, and heat it efficiently.',
    products=[
        dict(img='assets/img/thermoplastic-valves.jpg', fit='light', title='Thermoplastic valves & piping', desc='Corrosion-proof ball, butterfly, diaphragm and check valves and piping in PVC-U, PVC-C, PP-H and PVDF for chemical and high-purity lines.',
             points=['100% corrosion resistant: no rust or chemical attack', 'Manual, pneumatic and electric actuation', 'Wide temperature range, −40°C to +140°C', 'Lower total cost of ownership than metal']),
        dict(img='assets/img/pipe-couplings.jpg', fit='contain', bg='#212a31', title='Pipe repair & joining couplings', desc='Clamp-on couplings that repair leaks, cracks and corrosion, or join pipes, without welding, threading or flanging.',
             points=['Repair in 15 to 30 minutes', 'No hot work permit, minimal or no shutdown', 'Steel, stainless, ductile and cast iron, HDPE, PVC', 'DN50 to DN300 and larger']),
        dict(icon='valve', title='Special-application distribution', desc='Engineered pipelines for process, chemical, high-purity, chilled and hot water, and fire water networks.',
             points=['Material selection for the medium', 'Flow, pressure and thermal design', 'Instrumentation and flowmeters']),
        dict(icon='treat', title='Water & wastewater treatment', desc='Engineering of treatment plants: filtration, RO/UF, softening, STP and ETP, through to zero liquid discharge.',
             points=['Process design and equipment supply', 'Modular STP and ETP plants', 'Water reuse and recycling']),
        dict(icon='chem', title='Treatment chemicals', desc='Specialty chemicals for boilers, cooling towers, RO membranes and effluent treatment.',
             points=['Antiscalants and membrane cleaners', 'Cooling and boiler water programmes', 'Dosing systems and monitoring']),
        dict(icon='heat', title='Heat pumps', desc='High-efficiency heat pumps for hot water and process heating in homes, hotels, hospitals and industry.',
             points=['Up to 3 to 4 times more efficient than electric heating', 'Lower fuel and operating cost', 'Residential, commercial and industrial capacities']),
    ],
    after=f'''<section class="section" id="repair"><div class="wrap">
  <div class="section-head rv"><div class="eyebrow">Emergency pipe repair</div><h2>Repair leaks in minutes. Avoid downtime for days.</h2><p class="lead">When a pipe leaks, cracks or corrodes, every minute of downtime costs money. Clamp-on repair couplings provide a fast, reliable, permanent repair, often paying for themselves in a single avoided shutdown.</p></div>
  <div class="table-scroll rv"><table class="compare">
    <thead><tr><th></th><th>Traditional repair</th><th>Coupling repair</th></tr></thead>
    <tbody>
      <tr><td>Pipe removal</td><td>Required</td><td>Not required</td></tr>
      <tr><td>Welding</td><td>Required</td><td>No welding</td></tr>
      <tr><td>Hot work permit</td><td>Required</td><td>Not required</td></tr>
      <tr><td>Shutdown</td><td>Long</td><td>Minimal or none</td></tr>
      <tr><td>Safety risk</td><td>High</td><td>Safe</td></tr>
      <tr><td>Time to repair</td><td>Hours to days</td><td>15 to 30 minutes</td></tr>
    </tbody>
  </table></div>
</div></section>
''',
    apps_title='Industrial, commercial and residential water.',
    apps_lead='We work with plant engineers, facility managers, consultants and developers on new projects and on upgrades to running facilities.',
    apps=['Chemical & process industries', 'Pharmaceuticals', 'Food & beverage', 'Power & utilities', 'Water & wastewater plants', 'Infrastructure', 'Hotels & hospitals', 'Commercial buildings', 'Residential communities', 'Villas'],
    regions='Southern states (Telangana, Andhra Pradesh, Karnataka, Tamil Nadu, Kerala) · Western states (Maharashtra, Gujarat)',
)

# ------------------------------------------------------------------ EARTH
EARTH = dict(
    key='earth',
    meta_title='Siphonic Roof Drainage & Rainwater Harvesting | ISEPL',
    meta_desc='Siphonic roof drainage, rainwater harvesting storage integration, surface drainage channels and special drainage products for industries in South and West India.',
    hero_img='assets/img/siphonic-roof.jpg', hero_pos='center',
    h1='Every drop of rain, captured and put to work.',
    lead='Rainwater harvesting and drainage engineered for large roofs and industrial sites: siphonic roof drainage integrated with storage tanks, surface drainage channels and special drainage products.',
    subnav=[('siphonic', 'Siphonic drainage'), ('flow', 'How it works'), ('solutions', 'Solutions'), ('applications', 'Applications')],
    body=f'''<section class="section" id="siphonic"><div class="wrap split">
  <div class="rv">
    <div class="eyebrow">Siphonic roof drainage</div>
    <h2>Smaller pipes. Level runs. No underground pipework.</h2>
    <p class="lead">In a conventional gravity system only about 30% of the pipe carries water. A primed siphonic system runs full bore, so pipes can be much smaller and run level at roof height, all the way to the storage tank or discharge point.</p>
    <ul class="ticks">
      <li>Fewer outlets and downpipes for large roofs</li>
      <li>Horizontal pipework with no gradient: easy coordination with other services</li>
      <li>No underground collection pipes, less excavation</li>
      <li>Anti-block outlets for concrete, metal gutter and membrane roofs, 4 to 90 L/s</li>
    </ul>
  </div>
  <div class="media rv d1"><img src="assets/img/siphonic-outlet.jpg" alt="Anti-block siphonic roof outlet" loading="lazy" style="background:#000;aspect-ratio:4/3.3;object-fit:contain"></div>
</div></section>

<section class="section tight soft" id="flow"><div class="wrap">
  <div class="section-head rv"><div class="eyebrow">How it works</div><h2>Four stages of siphonic flow.</h2><p class="lead">As rainfall intensifies, the system primes itself, moving from gravity flow to full-bore siphonic flow with maximum capacity.</p></div>
  <div class="flow">
    <div class="f rv"><div class="pipe"><i style="height:18%"></i></div><small>0 – 20% · Light rain</small><h4>Gravity flow</h4><p>Water flows along the pipe with air carried above it.</p></div>
    <div class="f rv d1"><div class="pipe"><i style="height:38%"></i></div><small>20 – 40% · Moderate rain</small><h4>Plug flow</h4><p>Air pockets are driven down the pipe by water plugs, keeping it self-cleaning.</p></div>
    <div class="f rv d2"><div class="pipe"><i style="height:68%"></i></div><small>40 – 70% · Heavy rain</small><h4>Bubble flow</h4><p>Water fills the pipe and carries air bubbles in suspension.</p></div>
    <div class="f rv d3"><div class="pipe"><i style="height:100%"></i></div><small>70 – 100% · Design storm</small><h4>Full-bore flow</h4><p>Air is purged and the pipe runs full, delivering far greater capacity.</p></div>
  </div>
  <div class="table-scroll rv" style="margin-top:50px"><table class="compare">
    <thead><tr><th></th><th>Gravity system</th><th>Siphonic system</th></tr></thead>
    <tbody>
      <tr><td>Pipe filled with water</td><td>About 30%</td><td>100% when primed</td></tr>
      <tr><td>Pipe size</td><td>Larger</td><td>Significantly smaller</td></tr>
      <tr><td>Pipe routing</td><td>Needs gradient, clashes with services</td><td>Runs level, easy coordination</td></tr>
      <tr><td>Underground pipework</td><td>Required</td><td>Not required</td></tr>
      <tr><td>Water depth at outlet</td><td>Deeper</td><td>Lower</td></tr>
    </tbody>
  </table></div>
</div></section>
''',
    sol_title='Drainage & harvesting solutions',
    sol_lead='From the roof to the tank to the ground: integrated systems that protect your facility from flooding and turn rainwater into a resource.',
    products=[
        dict(img='assets/img/siphonic-outlet.jpg', fit='contain', bg='#000', title='Siphonic roof drainage', desc='Complete design, supply and installation of siphonic systems for large and complex roofs.',
             points=['Anti-block, finless outlets', 'Trafficable metal cover plates', 'Built-in membrane clamping', 'Hydraulic design calculations']),
        dict(icon='tank', title='Rainwater harvesting & storage integration', desc='Siphonic collection integrated with storage tanks, first-flush and filtration for reuse or recharge.',
             points=['Storage tank sizing and integration', 'First-flush and filtration', 'Groundwater recharge wells and percolation pits']),
        dict(icon='channel', title='Surface drainage channels', desc='Pre-engineered trench and channel drains for roads, yards, loading bays and plant floors.',
             points=['Light to heavy-duty load classes', 'Grated and slot drain options', 'Fast installation, long service life']),
        dict(icon='roof', title='Special drainage products', desc='Engineered stormwater management for industrial sites, including runoff containment and sustainable ground protection.',
             points=['Stormwater and flood management', 'Runoff containment', 'Custom drainage for special areas']),
    ],
    two=True,
    after='''<section class="section" style="padding-bottom:40px"><div class="wrap">
  <div class="section-head rv"><div class="eyebrow">Proven worldwide</div><h2>Trusted on landmark roofs.</h2><p class="lead">Siphonic technology is the preferred choice for the world’s largest roofs: airports, stadiums, data centres, logistics hubs and factories.</p></div>
  <div class="prod-grid">
    <div class="prod rv"><div class="ph"><img src="assets/img/stadium-roof.jpg" alt="Stadium roof" loading="lazy"></div><div class="bd"><h3>Stadiums &amp; airports</h3><p style="margin:0">Huge catchment areas drained with minimal pipework.</p></div></div>
    <div class="prod rv d1"><div class="ph"><img src="assets/img/datacenter.jpg" alt="Data centre building" loading="lazy"></div><div class="bd"><h3>Data centres</h3><p style="margin:0">Level pipe runs that avoid clashes with critical services.</p></div></div>
    <div class="prod rv d2"><div class="ph"><img src="assets/img/office-building.jpg" alt="Commercial office building" loading="lazy"></div><div class="bd"><h3>Commercial &amp; industrial</h3><p style="margin:0">Factories, warehouses, malls and office campuses.</p></div></div>
  </div>
</div></section>
''',
    apps_title='Built for industries and large roofs.',
    apps_lead='Our drainage and harvesting solutions serve industrial and commercial facilities where roof areas are large and rainfall is intense.',
    apps=['Factories & manufacturing', 'Warehouses & logistics parks', 'Data centres', 'Airports & aircraft hangars', 'Stadiums & convention centres', 'Shopping malls', 'Office complexes', 'Industrial yards & loading bays'],
    regions='Southern states (Telangana, Andhra Pradesh, Karnataka, Tamil Nadu, Kerala) · Western states (Maharashtra, Gujarat)',
)


# ------------------------------------------------------------------ SKY (coming soon)
def sky_page():
    h = head('Solar Solutions, Coming Soon | ISEPL', 'ISEPL Space / Sky: solar products for special applications, launching soon.', 'el-sky')
    h += header('solutions')
    h += f'''<section class="page-hero soon-hero" style="background:linear-gradient(160deg,#1c1240 0%,#3b2577 50%,#7b4bc4 100%)">
  <div class="art art-sky" style="position:absolute;inset:0;z-index:-2;opacity:.9"></div>
  <div class="wrap">
    <div class="crumbs rv"><a href="index.html">Home</a> / <a href="index.html#solutions">Solutions</a> / Space / Sky</div>
    <div class="chip-el rv">{icon('sky')}</div>
    <div class="eyebrow rv">Space / Sky · Akasha · Coming soon</div>
    <h1 class="rv d1">Harnessing the sky. Launching soon.</h1>
    <p class="lead rv d2">We are finalising a range of solar products for special applications, engineered with the same design, supply, erection and commissioning approach as our other four elements.</p>
    <form class="notify rv d3" data-notify><input type="text" required placeholder="Your email or phone number" aria-label="Your email or phone number"><button class="btn btn-primary" type="submit">Notify me {icon('arrow')}</button></form>
  </div>
</section>
<section class="section"><div class="wrap">
  <div class="section-head center rv"><div class="eyebrow">What to expect</div><h2>Solar, engineered for special applications.</h2><p class="lead">Our upcoming portfolio will complement our air, fire, water and earth solutions, so buildings run cleaner and more self-sufficiently.</p></div>
  <div class="prod-grid">
    <article class="prod rv"><div class="ph icon">{icon('solar')}</div><div class="bd"><h3>Special-application solar</h3><p style="margin:0">Solar solutions selected for specific site and process needs, beyond standard rooftop installations.</p></div></article>
    <article class="prod rv d1"><div class="ph icon">{icon('heat')}</div><div class="bd"><h3>Integrated with our systems</h3><p style="margin:0">Designed to work alongside heat pumps, ventilation and water systems for combined energy savings.</p></div></article>
    <article class="prod rv d2"><div class="ph icon">{icon('tools')}</div><div class="bd"><h3>Turnkey delivery</h3><p style="margin:0">One partner for design, supply, erection and commissioning.</p></div></article>
  </div>
</div></section>
'''
    h += cta_band('Interested in solar for your project?', 'Tell us about your requirement today. We will get in touch as soon as our solar range is ready.')
    h += footer()
    return h
