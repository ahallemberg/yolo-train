#!/bin/bash
PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" &>/dev/null && pwd)"
cp "${PROJECT_DIR}/.configs/params.train.default.yaml" "${PROJECT_DIR}/params/train.yaml"
cp "${PROJECT_DIR}/.configs/params.tune.default.yaml" "${PROJECT_DIR}/params/tune.yaml"
