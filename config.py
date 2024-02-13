import os
import datetime


LEARNING_RATE = float(os.getenv('LEARNING_RATE'))

WEIGHTS = os.getenv('WEIGHTS')
RESUME = bool(os.getenv('RESUME'))
DEVICE = os.getenv('DEVICE')
DATA = os.getenv('DATA')
IMG_SIZE = int(os.getenv('IMG_SIZE'))
EPOCHS=int(os.getenv('EPOCHS'))
BATCH_SIZE = int(os.getenv('BATCH_SIZE'))
PATIENCE = int(os.getenv('PATIENCE'))
SAVE_PERIOD = int(os.getenv('SAVE_PERIOD')) 
TIME_OUT = int(os.getenv('TIME_OUT'))
VERBOSE = bool(os.getenv('VERBOSE'))
PLOTS = bool(os.getenv('PLOTS'))
FREEZE = None if os.getenv('FREEZE') == 0 else int(os.getenv('FREEZE'))
CACHE = False 
match os.getenv('CACHE'):
    case "1":
        CACHE = True
    case "ram":
        CACHE = "ram"
    case "disk":
        CACHE = "disk"
    case _:
        raise ValueError("Invalid value for env varable CACHE")

PROJECT="runs/train/",
NAME=datetime.now().strftime("%Y-%m-%d_%H:%M:%S"),

# config logger 
# clearml 
# comet
