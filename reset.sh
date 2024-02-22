#!/bin/bash
PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" &>/dev/null && pwd)"
cp "${PROJECT_DIR}/.configs/train.params.default.yaml" "${PROJECT_DIR}/train.params.yaml"
cp "${PROJECT_DIR}/.configs/tune.params.default.yaml" "${PROJECT_DIR}/tune.params.yaml"