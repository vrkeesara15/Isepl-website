# ISEPL website

Static marketing website for Integra Sustainable Enterprises Pvt. Ltd. (ISEPL), organised around the five elements: Air, Fire, Water, Earth and Space/Sky.

## Structure

- `site/` – the published website (HTML, CSS, JS, images). This is what gets served.
- `build/` – small Python generator that writes the HTML pages in `site/` (shared header, footer and page content live here).
- `Dockerfile`, `Caddyfile`, `railway.json` – deployment on Railway (Caddy static file server on `$PORT`).

## Edit content

Change text in `build/home.py` (home page), `build/elements.py` (Air, Fire, Water, Earth, Sky pages), `build/build.py` (contact page) or `build/layout.py` (contact details, header, footer), then run:

```
python3 build/build.py
```

## Preview locally

```
cd site && python3 -m http.server 8000
```

Open http://localhost:8000

## Deploy to Railway

1. Push this folder to a GitHub repository.
2. In Railway: New Project → Deploy from GitHub repo → pick the repository. Railway detects `railway.json` and builds the Dockerfile.
3. Settings → Networking → Generate Domain to get a public `*.up.railway.app` link (a custom domain can be added later).

Or with the Railway CLI from this folder: `railway login`, `railway init`, `railway up`, then `railway domain`.

## Enquiry form

The site is static, so the enquiry form opens the visitor's email app with the details pre-filled to salesinfo.isepl@gmail.com (cc isepl.india@gmail.com). A form backend can be added later.
