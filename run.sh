#!/usr/bin/env bash

# Exit immediately if any command fails
set -e

cd "$(dirname "$0")"

IMAGE_NAME="pytest-app"

echo "Building Docker image: $IMAGE_NAME..."
docker build -t "$IMAGE_NAME" .

echo "Running the app..."
docker run --rm --init "$IMAGE_NAME"

echo "Done!"