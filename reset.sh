#!/bin/bash
PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" &>/dev/null && pwd)"
cp "${PROJECT_DIR}/.default/train.yaml" "${PROJECT_DIR}/params/train.yaml"
cp "${PROJECT_DIR}/.default/tune.yaml" "${PROJECT_DIR}/params/tune.yaml"
cp "${PROJECT_DIR}/.default/data.yaml" "${PROJECT_DIR}/datasets/data.yaml"