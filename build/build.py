"""Generates the static ISEPL website into ../site. Run: python3 build/build.py"""
import os
from icons import icon
from layout import head, header, footer, ELEMENTS, PHONE, PHONE_TEL, EMAIL, SALES, ADDRESS, ADDRESS_HTML, WA_LINK
import home
import elements as E

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'site')


def contact():
    h = head('Contact ISEPL | Enquiries & Consultations', 'Contact Integra Sustainable Enterprises, Bachupally, Hyderabad. Call +91 99621 69456 or email salesinfo.isepl@gmail.com.')
    h += header('contact')
    pills = ''.join(
        f'<label class="c-{k}"><input type="checkbox" name="interest" value="{k}"><span><i></i>{n}</span></label>'
        for k, n, *_ in ELEMENTS)
    q = ADDRESS.replace(' ', '+').replace(',', '%2C')
    h += f'''<section class="page-hero" style="background:linear-gradient(160deg,#0b1c36,#13294b)">
  <div class="wrap" style="padding-bottom:90px">
    <div class="crumbs rv"><a href="index.html">Home</a> / Contact</div>
    <div class="eyebrow rv" style="color:#7fd48a">Contact us</div>
    <h1 class="rv d1">Let’s talk about your project.</h1>
    <p class="lead rv d2">Whether it is a single villa or a multi-site industrial project, our engineers will help you choose the right solution. Send an enquiry, call or WhatsApp us.</p>
  </div>
</section>
<section class="section"><div class="wrap contact-grid">
  <div class="rv">
    <div class="info-card">
      <h3>Integra Sustainable Enterprises Pvt. Ltd.</h3>
      <div class="info-item"><span class="ic">{icon('pin')}</span><div><small>Office</small><p>{ADDRESS_HTML}</p></div></div>
      <div class="info-item"><span class="ic">{icon('phone')}</span><div><small>Phone &amp; WhatsApp</small><a href="tel:{PHONE_TEL}">{PHONE}</a></div></div>
      <div class="info-item"><span class="ic">{icon('mail')}</span><div><small>Sales enquiries</small><a href="mailto:{SALES}">{SALES}</a></div></div>
      <div class="info-item"><span class="ic">{icon('mail')}</span><div><small>General</small><a href="mailto:{EMAIL}">{EMAIL}</a></div></div>
      <a class="btn btn-primary" style="--accent:#25d366;margin-top:18px;position:relative;z-index:1" href="{WA_LINK}" target="_blank" rel="noopener">Chat on WhatsApp {icon('arrow')}</a>
    </div>
    <div class="map"><iframe title="ISEPL office location" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="https://www.google.com/maps?q={q}&output=embed"></iframe></div>
  </div>
  <form class="form rv d1" data-enquiry novalidate>
    <h3>Send an enquiry</h3>
    <p style="color:var(--muted);margin-bottom:26px">Tell us a little about your requirement and we will get back within one working day.</p>
    <div class="grid">
      <div><label for="f-name">Full name *</label><input id="f-name" name="name" required autocomplete="name"></div>
      <div><label for="f-company">Company / Project</label><input id="f-company" name="company" autocomplete="organization"></div>
      <div><label for="f-phone">Phone *</label><input id="f-phone" name="phone" type="tel" required autocomplete="tel"></div>
      <div><label for="f-email">Email</label><input id="f-email" name="email" type="email" autocomplete="email"></div>
      <div class="full"><label for="f-city">City / Site location</label><input id="f-city" name="city" placeholder="e.g. Hyderabad, Bengaluru, Pune"></div>
      <div class="full"><label>I’m interested in</label><div class="pills">{pills}</div></div>
      <div class="full"><label for="f-msg">Your requirement</label><textarea id="f-msg" name="message" placeholder="Building type, size, application, timeline..."></textarea></div>
      <div class="full"><button class="btn btn-primary" type="submit" style="--accent:var(--navy);width:100%;justify-content:center">Send Enquiry {icon('arrow')}</button></div>
    </div>
    <p class="note">Submitting opens your email app with the details filled in, addressed to {SALES}.</p>
    <div class="ok">Thank you! Your email app should now be open. Just press send, and we will be in touch shortly.</div>
  </form>
</div></section>
'''
    h += footer()
    return h


PAGES = {
    'index.html': home.page,
    'air.html': lambda: E.element_page(E.AIR),
    'fire.html': lambda: E.element_page(E.FIRE),
    'water.html': lambda: E.element_page(E.WATER),
    'earth.html': lambda: E.element_page(E.EARTH),
    'sky.html': E.sky_page,
    'contact.html': contact,
}

if __name__ == '__main__':
    for name, fn in PAGES.items():
        with open(os.path.join(OUT, name), 'w', encoding='utf-8') as f:
            f.write(fn())
        print('wrote', name)
    # 404
    with open(os.path.join(OUT, '404.html'), 'w', encoding='utf-8') as f:
        f.write(head('Page not found | ISEPL', 'Page not found') + header() +
                '<section class="section center"><div class="wrap"><h1>Page not found</h1><p class="lead">The page you are looking for has moved.</p>'
                '<a class="btn btn-primary" href="index.html">Back to home</a></div></section>' + footer())
