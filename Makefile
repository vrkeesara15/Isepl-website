.PHONY: build check serve docker-run deploy-railway deploy-gcp

build:          ## Regenerate HTML pages in site/ from build/*.py
	python3 build/build.py

check: build    ## Regenerate and verify every link/image
	python3 tools/check_site.py

serve: build    ## Preview at http://localhost:8000
	cd site && python3 -m http.server 8000

docker-run:     ## Run the production container at http://localhost:8080
	docker build -t isepl-site . && docker run --rm -p 8080:8080 isepl-site

deploy-railway: ## Deploy current folder to the linked Railway service
	railway up --detach

deploy-gcp:     ## Deploy to Cloud Run: make deploy-gcp PROJECT=my-gcp-project
	./deploy/gcp-deploy.sh $(PROJECT)
