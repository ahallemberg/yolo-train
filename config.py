import os
import datetime

WEIGHTS = os.getenv('WEIGHTS')
DATA = os.getenv('DATA')
EPOCHS = int(os.getenv('EPOCHS'))
TIME_OUT = int(os.getenv('TIME_OUT'))
LEARNING_RATE = float(os.getenv('LEARNING_RATE'))

RESUME = bool(os.getenv('RESUME'))
DEVICE = os.getenv('DEVICE')

IMG_SIZE = int(os.getenv('IMG_SIZE'))

BATCH_SIZE = int(os.getenv('BATCH_SIZE'))
PATIENCE = int(os.getenv('PATIENCE'))
SAVE_PERIOD = int(os.getenv('SAVE_PERIOD')) 

VERBOSE = bool(os.getenv('VERBOSE'))
PLOTS = bool(os.getenv('PLOTS'))
FREEZE = None if os.getenv('FREEZE') == 0 else int(os.getenv('FREEZE'))
LOGGER = os.getenv('LOGGER')
INITIAL_LEARNING_RATE = float(os.getenv('INITIAL_LEARNING_RATE'))
FINAL_LEARNING_RATE = float(os.getenv('FINAL_LEARNING_RATE'))
PROFILE = bool(os.getenv('PROFILE'))


match os.getenv('CACHE'):
    case "0":
        CACHE = False
    case "1":
        CACHE = True
    case "ram":
        CACHE = "ram"
    case "disk":
        CACHE = "disk"
    case _:
        raise ValueError("Invalid value for env varable CACHE")


NAME=datetime.now().strftime("%Y-%m-%d_%H:%M:%S"),

# config logger 
# clearml 
# comet
