# Variables
DOCKER_IMAGE=backend-challenge
APP_CONTAINER=app
PROJECT_DIR=$(shell pwd)
GIT_HASH=$(shell git rev-parse --short HEAD)
.PHONY: release build up up-d down restart clear shell tests

release:
	@echo "Building Release image..."
	docker build -t "${DOCKER_IMAGE}:${GIT_HASH}" --target production .
	@echo "Docker image built."

build:
	@echo "Starting FastAPI application..."
	docker compose build --no-cache app
	@echo "FastAPI is running"

up:
	@echo "Starting FastAPI application..."
	docker compose up
	@echo "FastAPI is running"

up-d:
	@echo "Starting FastAPI application in background..."
	docker compose up -d
	@echo "FastAPI is running"

down:
	@echo "Stopping Docker container..."
	docker compose stop
	@echo "Docker container stopped."

restart: down up-d

clear:
	@echo "Cleaning up Docker resources..."
	docker compose down
	@echo "Cleanup completed."

shell:
	docker compose exec -it $(APP_CONTAINER) /bin/bash

tests:
	docker compose exec -it $(APP_CONTAINER) pytest -v