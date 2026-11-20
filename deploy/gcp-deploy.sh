#!/usr/bin/env bash
# One-command deploy of the ISEPL website to Google Cloud Run.
#
# Usage:  ./deploy/gcp-deploy.sh <gcp-project-id> [region] [service-name]
# Example: ./deploy/gcp-deploy.sh isepl-prod asia-south1 isepl-website
#
# Requires: gcloud CLI, logged in (`gcloud auth login`) with Owner/Editor on the project.
set -euo pipefail

PROJECT_ID="${1:?Usage: $0 <gcp-project-id> [region] [service-name]}"
REGION="${2:-asia-south1}"
SERVICE="${3:-isepl-website}"
REPO="web"

cd "$(dirname "$0")/.."

echo "==> Using project $PROJECT_ID, region $REGION, service $SERVICE"
gcloud config set project "$PROJECT_ID" >/dev/null

echo "==> Enabling required APIs (safe to re-run)"
gcloud services enable run.googleapis.com cloudbuild.googleapis.com artifactregistry.googleapis.com

echo "==> Ensuring Artifact Registry repository '$REPO' exists"
gcloud artifacts repositories describe "$REPO" --location="$REGION" >/dev/null 2>&1 || \
  gcloud artifacts repositories create "$REPO" --repository-format=docker --location="$REGION" \
    --description="ISEPL website images"

echo "==> Granting Cloud Build permission to deploy to Cloud Run (safe to re-run)"
PROJECT_NUMBER="$(gcloud projects describe "$PROJECT_ID" --format='value(projectNumber)')"
for SA in "${PROJECT_NUMBER}@cloudbuild.gserviceaccount.com" "${PROJECT_NUMBER}-compute@developer.gserviceaccount.com"; do
  for ROLE in roles/run.admin roles/iam.serviceAccountUser roles/artifactregistry.writer; do
    gcloud projects add-iam-policy-binding "$PROJECT_ID" --member="serviceAccount:$SA" --role="$ROLE" \
      --condition=None >/dev/null 2>&1 || true
  done
done

echo "==> Building and deploying with Cloud Build"
gcloud builds submit --config cloudbuild.yaml \
  --substitutions="_REGION=$REGION,_SERVICE=$SERVICE,_REPO=$REPO"

URL="$(gcloud run services describe "$SERVICE" --region="$REGION" --format='value(status.url)')"
echo "==> Live at: $URL"
curl -fsS "$URL/healthz" && echo "  (health check OK)"
