#!/bin/bash
# check https://docs.ultralytics.com/modes/train/#arguments for valid arguments for training

export DEVICE=cpu
export CACHE=ram 
export DATA="data.yaml"
export WEIGHTS="models/yolov8n.pt"
export RESUME=0 # true if you want to resume training
export IMG_SIZE=640
export EPOCHS=10
export BATCH_SIZE=16
export FREEZE=0
export PATIENCE=50
export SAVE_PERIOD=1
export TIMEOUT=1 
export VERBOSE=1
export PLOTS=1