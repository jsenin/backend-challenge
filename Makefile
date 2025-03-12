# Variables
DOCKER_IMAGE = "backend-chanllege"
APP_CONTAINER = app
PROJECT_DIR = $(shell pwd)

.PHONY: release build up up-d down restart clear shell tests

release:
	@echo "Building Docker image..."
	docker build -t $(DOCKER_IMAGE) --target production .
	@echo "Docker image built."

build:
	@echo "Starting FastAPI application..."
	docker compose build
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