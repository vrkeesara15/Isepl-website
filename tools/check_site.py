"""CI check: every local link, image, script and stylesheet referenced by the site exists."""
import os, re, sys
from html.parser import HTMLParser

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'site')

class Refs(HTMLParser):
    def __init__(self):
        super().__init__(); self.refs = []; self.ids = set()
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if 'id' in a: self.ids.add(a['id'])
        for k in ('href', 'src'):
            if a.get(k): self.refs.append(a[k])

errors = []
pages = {}
for f in sorted(os.listdir(ROOT)):
    if f.endswith('.html'):
        p = Refs(); p.feed(open(os.path.join(ROOT, f), encoding='utf-8').read()); pages[f] = p
for f, p in pages.items():
    for r in p.refs:
        if re.match(r'^(https?:|mailto:|tel:|data:)', r): continue
        path, _, frag = r.partition('#'); path = path.split('?')[0]
        target = path or f
        if path and not os.path.exists(os.path.join(ROOT, path)):
            errors.append(f'{f}: missing file {r}')
        elif frag and target in pages and frag not in pages[target].ids:
            errors.append(f'{f}: missing anchor {r}')
for css in ['assets/css/styles.css']:
    for u in re.findall(r'url\(["\']?([^"\')]+)', open(os.path.join(ROOT, css)).read()):
        if not u.startswith('data:') and not os.path.exists(os.path.join(ROOT, 'assets/css', u)):
            errors.append(f'{css}: missing {u}')
print(f'Checked {len(pages)} pages')
if errors:
    print('\n'.join(errors)); sys.exit(1)
print('All references OK')
