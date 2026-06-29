#!/usr/bin/env bash
set -e

echo "Testing Python basics..."
cd projects/python/basics
PYTHONPATH=. pytest -q

echo "Testing FastAPI starter..."
cd ../../web/fastapi-starter
PYTHONPATH=. pytest -q

echo "Testing Flask starter..."
cd ../flask-starter
PYTHONPATH=. pytest -q

echo "All lab tests passed."
