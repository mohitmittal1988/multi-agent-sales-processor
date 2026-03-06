#!/bin/bash
# Simple helper to build and launch the entire stack with Docker Compose
set -e

echo "Building and starting services..."
docker-compose up --build
