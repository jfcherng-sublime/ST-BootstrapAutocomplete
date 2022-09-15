#!/usr/bin/env bash

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="${SCRIPT_DIR}/.."
DB_DIR="${PROJECT_DIR}/db"

mkdir -p "${DB_DIR}"

pushd "${PROJECT_DIR}" || exit

echo "Download and parse Bootstrap 3..."
python \
    "${SCRIPT_DIR}/extract_class_names.py" \
    "https://cdn.jsdelivr.net/npm/bootstrap@3/dist/css/bootstrap.min.css" \
    --output_format="json" \
    --lib_name="Bootstrap" \
    --lib_version="3" \
    >"${DB_DIR}/3.json"

echo "Download and parse Bootstrap 4..."
python \
    "${SCRIPT_DIR}/extract_class_names.py" \
    "https://cdn.jsdelivr.net/npm/bootstrap@4/dist/css/bootstrap.min.css" \
    --output_format="json" \
    --lib_name="Bootstrap" \
    --lib_version="4" \
    >"${DB_DIR}/4.json"

echo "Download and parse Bootstrap 5..."
python \
    "${SCRIPT_DIR}/extract_class_names.py" \
    "https://cdn.jsdelivr.net/npm/bootstrap@5/dist/css/bootstrap.min.css" \
    --output_format="json" \
    --lib_name="Bootstrap" \
    --lib_version="5" \
    >"${DB_DIR}/5.json"

popd || exit
