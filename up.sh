#!/bin/bash
docker compose -f docker_compose.yaml build --no-cache
docker compose -f docker_compose.yaml up -d