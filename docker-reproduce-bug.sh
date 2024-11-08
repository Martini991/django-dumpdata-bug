#!/usr/bin/env bash

# Looked up tickets:
# https://code.djangoproject.com/ticket/35238
# https://code.djangoproject.com/ticket/35159

SCRIPT_DIR=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" &>/dev/null && pwd)

docker build "${SCRIPT_DIR}" --tag wrong_user_manager:latest
docker run -it --rm \
  --env-file "${SCRIPT_DIR}/.env" \
  -w /run/wrong_user_manager/ \
  -v "${SCRIPT_DIR}:/run/wrong_user_manager/" \
  -p "80:80" \
  wrong_user_manager:latest django-admin dumpdata child_app.item --all --traceback -o /dev/null
