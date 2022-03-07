APP=$(shell basename $(CURDIR))

DOCKER_HUB_USER = lecovich
REGISTRY ?= $(DOCKER_HUB_USER)/$(APP)
REVISION ?= $(shell git rev-parse --short=8 HEAD)
VERSION ?= $(shell git rev-parse --abbrev-ref HEAD)
BUILDTIME = $(shell date -u +"%Y%m%d%H%M%S")

## -
## Docker commands:

##   docker/login - login to Docker Hub
.PHONY: docker/login
docker/login:
	@echo "Logging in"
	docker login -u $(DOCKER_HUB_USER)

##   docker/image/build - build an image
.PHONY: docker/image/build
docker/image/build:
	@echo "Building docker image"
	docker build \
	    --no-cache \
		--build-arg REVISION=$(REVISION) \
		--build-arg BUILDTIME=$(BUILDTIME) \
		-t $(REGISTRY):$(VERSION) \
		-t $(REGISTRY):$(REVISION) backend

##   docker/runserver - run a dev server connected to local PG and Redis
.PHONY: docker/runserver
docker/runserver:
	@echo "Running dev server"
	docker run --rm \
		-v $(PWD)/backend:/app/ \
		-w /app \
		-p 8000:8000 \
		$(REGISTRY):$(VERSION) poetry run uvicorn app:app --host=0.0.0.0 --port=8000

## -
## help - this message
.PHONY: help
help: Makefile
	@echo "Application: ${APP}\n"
	@echo "Run command:\n  make <target>\n"
	@grep -E -h '^## .*' $(MAKEFILE_LIST) | sed -n 's/^##//p'  | column -t -s '-' |  sed -e 's/^/ /'