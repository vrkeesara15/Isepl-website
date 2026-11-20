# Hosting the ISEPL website on Google Cloud (GCP)

The website is a static site packaged as a small Docker container (Caddy web server, about 50 MB). The same container runs on Railway today and runs unchanged on **Google Cloud Run**, which is the recommended GCP option: fully managed, HTTPS included, scales to zero, and typically costs little to nothing at this traffic level.

## What's in this repository

| File | Purpose |
|---|---|
| `site/` | The finished website (HTML, CSS, JS, images). This is what's served. |
| `Dockerfile` | Builds the container: Caddy plus the `site/` folder. |
| `Caddyfile` | Web server config: listens on `$PORT` (default 8080), gzip/zstd, caching, security headers, `/healthz`, custom 404. |
| `cloudbuild.yaml` | Cloud Build pipeline: build the image, push it to Artifact Registry, deploy it to Cloud Run. |
| `deploy/gcp-deploy.sh` | One-command script that does the setup and runs the pipeline. |
| `build/` | Python generator for the HTML pages (only needed when editing content). |

## Prerequisites

- A GCP project with billing enabled.
- The [gcloud CLI](https://cloud.google.com/sdk/docs/install), logged in with `gcloud auth login`.
- Owner or Editor role on the project.

## Option A: one command (recommended)

```bash
git clone https://github.com/vrkeesara15/Isepl-website.git
cd Isepl-website
./deploy/gcp-deploy.sh <PROJECT_ID> asia-south1 isepl-website
```

The script:
1. Enables the Cloud Run, Cloud Build and Artifact Registry APIs.
2. Creates an Artifact Registry Docker repository called `web`.
3. Grants Cloud Build permission to deploy.
4. Builds the image, deploys it to Cloud Run and prints the live `https://…run.app` URL.

You can re-run it at any time to deploy a new version.

## Option B: manual steps

```bash
PROJECT_ID=<your-project>
REGION=asia-south1
gcloud config set project $PROJECT_ID
gcloud services enable run.googleapis.com cloudbuild.googleapis.com artifactregistry.googleapis.com
gcloud artifacts repositories create web --repository-format=docker --location=$REGION
gcloud builds submit --config cloudbuild.yaml --substitutions=_REGION=$REGION,_SERVICE=isepl-website
```

Or deploy directly from source with no Artifact Registry setup (Cloud Run builds the Dockerfile itself):

```bash
gcloud run deploy isepl-website --source . --region asia-south1 --allow-unauthenticated --port 8080
```

## Automatic deploys on every push (optional)

In the Cloud Console go to **Cloud Build → Triggers → Create trigger**:
- Source: this GitHub repository, branch `^main$`
- Configuration: `cloudbuild.yaml`

Each push to `main` then rebuilds and redeploys the site.

## Custom domain and HTTPS

The simplest route is **Cloud Run → Manage custom domains → Add mapping**. Pick the service, enter the domain (for example `www.isepl.in`), and add the DNS records shown at your domain registrar. Google provisions and renews the HTTPS certificate automatically.

For production traffic or a CDN, use a **global external Application Load Balancer** with a serverless NEG pointing at the Cloud Run service, a Google-managed certificate, and optionally Cloud CDN. See [Cloud Run custom domains](https://cloud.google.com/run/docs/mapping-custom-domains).

## Alternative: Cloud Storage + Cloud CDN (no container)

The site is fully static, so the contents of `site/` can also be uploaded to a Cloud Storage bucket behind a load balancer with Cloud CDN:

```bash
gsutil mb -l asia-south1 gs://<bucket-name>
gsutil -m rsync -r -d site gs://<bucket-name>
gsutil web set -m index.html -e 404.html gs://<bucket-name>
gsutil iam ch allUsers:objectViewer gs://<bucket-name>
```

Note that the extensionless URL rewrites (`/air` → `/air.html`), security headers and `/healthz` live in the Caddyfile and won't apply with this option. All internal links in the site use `.html`, so it still works.

## Health check and verification

- `GET /healthz` returns `200 ok`. Use it for uptime checks and load balancer health checks.
- Smoke test after a deploy:

```bash
URL=$(gcloud run services describe isepl-website --region asia-south1 --format='value(status.url)')
for p in / /air.html /fire.html /water.html /earth.html /sky.html /contact.html /healthz; do
  echo "$p $(curl -s -o /dev/null -w '%{http_code}' $URL$p)"; done
```

## Run locally

```bash
docker build -t isepl-site . && docker run --rm -p 8080:8080 isepl-site
# open http://localhost:8080
```

## Notes

- **Enquiry form:** The site is static. The contact form opens the visitor's email app with the enquiry pre-filled to salesinfo.isepl@gmail.com. To receive submissions directly, add a form backend (for example a small Cloud Run function or a form service).
- **Costs:** Cloud Run bills per request and scales to zero (`--min-instances=0`). Set `--min-instances=1` if you want to avoid a cold start of about a second after idle periods.
