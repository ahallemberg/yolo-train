import os 
from ultralytics import YOLO
from config import VALIDATE, DROPOUT, MASK_RATIO, OVERLAP_MASK, NOMINAL_BATCH_SIZE, LABEL_SMOOTHING, KEYPOINT_OBJECTNESS_LOSS_WEIGHT, POSE_LOSS_WEIGHT, DISTRIBUTED_FOCAL_LOSS_WEIGHT, CLASSIFICATION_LOSS_WEIGHT, BOX_LOSS_WEIGHT, WARMUP_BIAS_LEARNING_RATE, WARMUP_MOMENTUM, WARMUP_EPOCHS, WEIGHT_DECAY, MOMENTUM, PROFILE, INITIAL_LEARNING_RATE, FINAL_LEARNING_RATE, FRACTION, AUTOMATIC_MIXED_PRECISION, CLOSE_MOSAIC, COSINE_LEARNING_RATE, DETERMINISTIC, SEED,OPTIMIZER, EXIST_OK, WORKERS,PROJECT, EPOCHS, FREEZE, RESUME, CACHE, BATCH_SIZE, IMG_SIZE, DATA, WEIGHTS, DEVICE, TIMEOUT, VERBOSE, PLOTS, PATIENCE, SAVE_PERIOD, NAME, INITIAL_LEARNING_RATE, FINAL_LEARNING_RATE
from logger import get_logger

def main():
    # setup environment
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    # setup logger 
    logger = get_logger()
    if logger: logger.setup()


    # Load a model
    model = YOLO(WEIGHTS)  
    print(DEVICE)
    model.train(
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
        project=PROJECT, 
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

if __name__ == "__main__": 
    main()
else:
    raise RuntimeError("This script is meant to be run as a standalone script")