#!/bin/bash
export PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" &>/dev/null && pwd)"
export TASK=train
source "${PROJECT_DIR}/setup_env.sh"
python3 "${PROJECT_DIR}/train.py"