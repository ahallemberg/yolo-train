import os

WEIGHTS = os.getenv('WEIGHTS')
if not os.path.exists(WEIGHTS): raise ValueError(f"Invalid value for env varable WEIGHTS: {WEIGHTS}. File not found")

DATA = os.getenv('DATA')
if not os.path.exists(DATA): raise ValueError(f"Invalid value for env varable DATA: {DATA}. File not found")

EPOCHS = int(os.getenv('EPOCHS'))

TIMEOUT = int(os.getenv('TIMEOUT'))
if TIMEOUT == 0: TIMEOUT = None

PATIENCE = int(os.getenv('PATIENCE'))
BATCH_SIZE = int(os.getenv('BATCH_SIZE'))
IMG_SIZE = int(os.getenv('IMG_SIZE'))
SAVE_PERIOD = int(os.getenv('SAVE_PERIOD')) 

_cache = os.getenv('CACHE')
match _cache:
    case "0":
        CACHE = False
    case "1":
        CACHE = True
    case "ram":
        CACHE = "ram"
    case "disk":
        CACHE = "disk"
    case _:
        raise ValueError(f"Invalid value for env varable CACHE: {_cache}")

_device = os.getenv('DEVICE')
if _device == "cpu":
    DEVICE = "cpu"
elif _device == "mps":
    DEVICE = "mps"
else:
    try:
        _targ_dev = ""
        _device_list = _device.split(",")
        for _dvs in _device_list:
            _dvs = _dvs.strip()
            _targ_dev += f"{_dvs},"
        
        DEVICE = _targ_dev 

    except:
        raise ValueError(f"Invalid value for env varable DEVICE: {_device}")

WORKERS = int(os.getenv('WORKERS'))
PROJECT = os.getenv('PROJECT')
NAME = os.getenv('NAME')
EXIST_OK = bool(os.getenv('EXIST_OK'))

OPTIMIZER = os.getenv('OPTIMIZER')
VERBOSE = bool(os.getenv('VERBOSE'))
SEED = int(os.getenv('SEED'))
DETERMINISTIC = bool(os.getenv('DETERMINISTIC'))
COSINE_LEARNING_RATE = bool(os.getenv('COSINE_LEARNING_RATE'))
CLOSE_MOSAIC = int(os.getenv('CLOSE_MOSAIC'))

RESUME = bool(os.getenv('RESUME'))
AUTOMATIC_MIXED_PRECISION = bool(os.getenv('AUTOMATIC_MIXED_PRECISION'))
FRACTION = float(os.getenv('FRACTION'))

PROFILE = bool(os.getenv('PROFILE'))

if os.getenv('FREEZE_ON') == 1:
    _freeze = os.getenv('FREEZE')
    if len(_freeze.split(",")) > 1:
        FREEZE = tuple(map(int, _freeze.split(",")))
        FREEZE = tuple(map(int, _freeze.split(",")))
    FREEZE = int(os.getenv('FREEZE'))

else:
    FREEZE = None

INITIAL_LEARNING_RATE = float(os.getenv('INITIAL_LEARNING_RATE'))
FINAL_LEARNING_RATE= float(os.getenv('FINAL_LEARNING_RATE'))
MOMENTUM = float(os.getenv('MOMENTUM'))
WEIGHT_DECAY= float(os.getenv('WEIGHT_DECAY'))
WARMUP_EPOCHS = int(os.getenv('WARMUP_EPOCHS'))
WARMUP_MOMENTUM = float(os.getenv('WARMUP_MOMENTUM'))
WARMUP_BIAS_LEARNING_RATE = float(os.getenv('WARMUP_BIAS_LEARNING_RATE'))
BOX_LOSS_WEIGHT = float(os.getenv('BOX_LOSS_WEIGHT'))
CLASSIFICATION_LOSS_WEIGHT = float(os.getenv('CLASSIFICATION_LOSS_WEIGHT'))
DISTRIBUTED_FOCAL_LOSS_WEIGHT = float(os.getenv('DISTRIBUTED_FOCAL_LOSS_WEIGHT'))
POSE_LOSS_WEIGHT = float(os.getenv('POSE_LOSS_WEIGHT'))
KEYPOINT_OBJECTNESS_LOSS_WEIGHT = float(os.getenv('KEYPOINT_OBJECTNESS_LOSS_WEIGHT'))
LABEL_SMOOTHING = float(os.getenv('LABEL_SMOOTHING'))
NOMINAL_BATCH_SIZE = int(os.getenv('NOMINAL_BATCH_SIZE'))
OVERLAP_MASK = bool(os.getenv('OVERLAP_MASK'))
MASK_RATIO = int(os.getenv('MASK_RATIO'))
DROPOUT = float(os.getenv('DROPOUT'))
VALIDATE = bool(os.getenv('VALIDATE'))
PLOTS = bool(os.getenv('PLOTS'))
LOGGER = os.getenv('LOGGER')
