#!/bin/sh

docker build -f Dockerfile.py3 -t xdjk/py3.8 . --rm
docker build -t script_audit:v1.0 . --rm
docker run -tid --name audit -p 8000:8000 script_audit:v1.0
