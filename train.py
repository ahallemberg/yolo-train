from ultralytics import YOLO
from config import PROJECT, EPOCHS, FREEZE, RESUME, CACHE, BATCH_SIZE, IMG_SIZE, DATA, WEIGHTS, DEVICE, TIME_OUT, VERBOSE, PLOTS, PATIENCE, SAVE_PERIOD, NAME, INITIAL_LEARNING_RATE, FINAL_LEARNING_RATE
from logger import get_logger

# setup logger 
logger = get_logger()
if logger: logger.setup()


# Load a model
model = YOLO(WEIGHTS)  # load a pretrained model (recommended for training)

model.train(
    save=True, 
    data=DATA,
    time=TIME_OUT,
    epochs=EPOCHS,
    batch=BATCH_SIZE,
    patience=PATIENCE,
    imsz=IMG_SIZE,
    save_period=SAVE_PERIOD,
    cache=CACHE,
    device=DEVICE,
    project=PROJECT,
    name=NAME,
    verbose=VERBOSE,
    plots=PLOTS,  
    resume=RESUME,
    freeze=FREEZE,
    lr0=INITIAL_LEARNING_RATE,
    lrf=FINAL_LEARNING_RATE
) 

