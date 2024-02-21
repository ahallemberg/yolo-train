import os 
from ultralytics import YOLO
from config import ID, WEIGHTS, DATA, EPOCHS, TIMEOUT, PATIENCE, BATCH_SIZE, IMG_SIZE, SAVE_PERIOD, CACHE, DEVICE, WORKERS, PROJECT, NAME, EXIST_OK, OPTIMIZER, VERBOSE, SEED, COSINE_LEARNING_RATE, CLOSE_MOSAIC, RESUME, AUTOMATIC_MIXED_PRECISION, FRACTION, PROFILE, FREEZE, INITIAL_LEARNING_RATE, FINAL_LEARNING_RATE, MOMENTUM, WEIGHT_DECAY, WARMUP_EPOCHS, WARMUP_MOMENTUM, WARMUP_BIAS_LEARNING_RATE, BOX_LOSS_WEIGHT, CLASSIFICATION_LOSS_WEIGHT, DISTRIBUTED_FOCAL_LOSS_WEIGHT, POSE_LOSS_WEIGHT, KEYPOINT_OBJECTNESS_LOSS_WEIGHT, LABEL_SMOOTHING, NOMINAL_BATCH_SIZE, OVERLAP_MASK, MASK_RATIO, DROPOUT, VALIDATE, PLOTS, DETERMINISTIC
from logger import get_logger

def main():
    # setup environment
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    # arguments
    args = dict(
        save=True, 
        save_json=True,
        data=DATA,
        epochs=EPOCHS,
        time=TIMEOUT,
        patience=PATIENCE,
        batch=BATCH_SIZE,
        imgsz=IMG_SIZE,
        save_period=SAVE_PERIOD,
        cache=CACHE,
        device=DEVICE,
        workers=WORKERS,
        project=PROJECT+ID, 
        name=NAME,
        exist_ok=EXIST_OK,
        optimizer=OPTIMIZER, 
        verbose=VERBOSE,
        seed=SEED,
        deterministic=DETERMINISTIC,
        cos_lr=COSINE_LEARNING_RATE,
        close_mosaic=CLOSE_MOSAIC,
        resume=RESUME,
        amp=AUTOMATIC_MIXED_PRECISION,
        fraction=FRACTION,
        profile=PROFILE,
        freeze=FREEZE,
        lr0=INITIAL_LEARNING_RATE,
        lrf=FINAL_LEARNING_RATE,
        momentum=MOMENTUM,
        weight_decay=WEIGHT_DECAY,
        warmup_epochs=WARMUP_EPOCHS,
        warmup_momentum=WARMUP_MOMENTUM,
        warmup_bias_lr=WARMUP_BIAS_LEARNING_RATE,
        box=BOX_LOSS_WEIGHT,
        cls=CLASSIFICATION_LOSS_WEIGHT,
        dfl=DISTRIBUTED_FOCAL_LOSS_WEIGHT,
        pose=POSE_LOSS_WEIGHT,
        kobj=KEYPOINT_OBJECTNESS_LOSS_WEIGHT,
        label_smoothing=LABEL_SMOOTHING,
        nbs=NOMINAL_BATCH_SIZE,
        overlap_mask=OVERLAP_MASK,
        mask_ratio=MASK_RATIO,
        dropout=DROPOUT,
        val=VALIDATE,
        plots=PLOTS
        )
  
    # setup logger 
    logger = get_logger()
    if logger: 
        logger.setup()
        logger.connect(args)

    # Load a model
    model = YOLO(WEIGHTS)  

    # train model with the configurations
    model.train(**args)

if __name__ == "__main__": 
    main()
else:
    raise RuntimeError("This script is meant to be run as a standalone script")