# ISEPL website

Static marketing website for Integra Sustainable Enterprises Pvt. Ltd. (ISEPL), organised around the five elements: Air, Fire, Water, Earth and Space/Sky.

## Structure

- `site/` – the published website (HTML, CSS, JS, images). This is what gets served.
- `build/` – small Python generator that writes the HTML pages in `site/` (shared header, footer and page content live here).
- `Dockerfile`, `Caddyfile` – production container (Caddy static file server on `$PORT`, `/healthz` health check, security headers).
- `railway.json` – Railway deployment config.
- `cloudbuild.yaml`, `deploy/gcp-deploy.sh`, `docs/DEPLOY-GCP.md` – Google Cloud Run hosting (see **Deploy to GCP** below).
- `Makefile` – shortcuts: `make serve`, `make check`, `make docker-run`, `make deploy-railway`, `make deploy-gcp PROJECT=...`.

## Edit content

Change text in `build/home.py` (home page), `build/elements.py` (Air, Fire, Water, Earth, Sky pages), `build/build.py` (contact page) or `build/layout.py` (contact details, header, footer), then run:

```
python3 build/build.py
```

## Preview locally

```
make serve            # or: cd site && python3 -m http.server 8000
```

Open http://localhost:8000

## Deploy to Railway

1. Push this folder to a GitHub repository.
2. In Railway: New Project → Deploy from GitHub repo → pick the repository. Railway detects `railway.json` and builds the Dockerfile.
3. Settings → Networking → Generate Domain to get a public `*.up.railway.app` link (a custom domain can be added later).

Or with the Railway CLI from this folder: `railway login`, `railway init`, `railway up`, then `railway domain`.

## Deploy to GCP

Full guide: [docs/DEPLOY-GCP.md](docs/DEPLOY-GCP.md). Short version:

```
./deploy/gcp-deploy.sh <gcp-project-id> asia-south1 isepl-website
```

## CI/CD

- **CI** (`.github/workflows/ci.yml`, GitHub Actions) runs on every push and pull request: regenerates the pages and fails if `site/` is out of date, checks every link and image, builds the Docker image and smoke-tests every page in the running container.
- **CD** is Railway's GitHub integration: each push to `main` redeploys automatically. Turn on **Wait for CI** in the Railway service settings so a deploy only goes out after CI passes.

## Enquiry form

The site is static, so the enquiry form opens the visitor's email app with the details pre-filled to salesinfo.isepl@gmail.com (cc isepl.india@gmail.com). A form backend can be added later.
