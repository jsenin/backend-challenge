# Variables
DOCKER_IMAGE = "backend-chanllege"
APP_CONTAINER = app
PROJECT_DIR = $(shell pwd)

.PHONY: build up up-d down clear shell

build:
	@echo "Building Docker image..."
	docker build -t $(DOCKER_IMAGE) --target production .
	@echo "Docker image built."

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

clear:
	@echo "Cleaning up Docker resources..."
	docker compose down
	@echo "Cleanup completed."

shell:
	docker compose exec -it $(APP_CONTAINER) /bin/bash