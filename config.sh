#!/bin/bash
# check https://docs.ultralytics.com/modes/train/#arguments for valid arguments for training

export WEIGHTS="models/yolov8n.pt"
export DATA="data.yaml"
export EPOCHS=10
export TIMEOUT=1 
export PATIENCE=50
export BATCH_SIZE=16
export IMG_SIZE=640
export SAVE_PERIOD=1
export CACHE=ram 
export DEVICE=cpu
export WORKERS=8
export PROJECT="runs/train/"
export NAME="exp"
export EXIST_OK=0
export OPTIMIZER=auto 
export VERBOSE=1
export SEED=0
export DETERMINISTIC=1
export COSINE_LEARNING_RATE=0
export CLOSE_MOSAIC=10 
export RESUME=0 # true if you want to resume training
export AUTOMATIC_MIXED_PRECISION=1
export FRACTION=1.0
export PROFILE=0 # Enables profiling of ONNX and TensorRT speeds during training, useful for optimizing model deployment.
export FREEZE=0
export INITIAL_LEARNING_RATE=0.01
export FINAL_LEARNING_RATE=0.01 # Final learning rate as a fraction of the initial rate = (`INITIAL_LEARNING_RATE` * `FINAL_LEARNING_RATE`), used in conjunction with schedulers to adjust the learning rate over time.
export MOMENTUM=0.937
export WEIGHT_DECAY=0.0005
export WARMUP_EPOCHS=3
export WARMUP_MOMENTUM=0.8
export WARMUP_BIAS_LR=0.1
export BOX_LOSS_WEIGHT=7.5
export CLASSIFICATION_LOSS_WEIGHT=0.5
export DISTRIBUTED_FOCAL_LOSS_WEIGHT=0
export POSE_LOSS_WEIGHT=12
export KEYPOINT_LOSS_WEIGHT=2.0 
export LABEL_SMOOTHING=0.0 
export NOMINAL_BATCH_SIZE=64 
export OVERLAP_MASK=1
export MASK_RATIO=4
export DROPOUT=0.0
export VALIDATE=1
export PLOTS=1