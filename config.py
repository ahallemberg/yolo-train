import os

def __init():
    def str_to_bool(x: str): return x in ['1', 'True', 'true', 't', 'T']

    global WEIGHTS, DATA, EPOCHS, TIMEOUT, PATIENCE, BATCH_SIZE, IMG_SIZE, SAVE_PERIOD, CACHE, DEVICE, WORKERS, PROJECT, NAME, EXIST_OK, OPTIMIZER, VERBOSE, SEED, DETERMINISTIC, COSINE_LEARNING_RATE, CLOSE_MOSAIC, RESUME, AUTOMATIC_MIXED_PRECISION, FRACTION, PROFILE, FREEZE, INITIAL_LEARNING_RATE, FINAL_LEARNING_RATE, MOMENTUM, WEIGHT_DECAY, WARMUP_EPOCHS, WARMUP_MOMENTUM, WARMUP_BIAS_LEARNING_RATE, BOX_LOSS_WEIGHT, CLASSIFICATION_LOSS_WEIGHT, DISTRIBUTED_FOCAL_LOSS_WEIGHT, POSE_LOSS_WEIGHT, KEYPOINT_OBJECTNESS_LOSS_WEIGHT, LABEL_SMOOTHING, NOMINAL_BATCH_SIZE, OVERLAP_MASK, MASK_RATIO, DROPOUT, VALIDATE, PLOTS, LOGGER

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

    __cache = os.getenv('CACHE')
    match __cache:
        case "0":
            CACHE = False
        case "1":
            CACHE = True
        case "ram":
            CACHE = "ram"
        case "disk":
            CACHE = "disk"
        case _:
            raise ValueError(f"Invalid value for env varable CACHE: {__cache}")

    __device = os.getenv('DEVICE')
    if __device == "cpu":
        DEVICE = "cpu"
    elif __device == "mps":
        DEVICE = "mps"
    else:
        try:
            _targ_dev = ""
            _device_list = __device.split(",")
            for _dvs in _device_list:
                _dvs = _dvs.strip()
                _targ_dev += f"{_dvs},"
            
            DEVICE = _targ_dev 

        except:
            raise ValueError(f"Invalid value for env varable DEVICE: {__device}")

    WORKERS = int(os.getenv('WORKERS'))
    PROJECT = os.getenv('PROJECT')
    NAME = os.getenv('NAME')
    EXIST_OK = str_to_bool(os.getenv('EXIST_OK'))

    OPTIMIZER = os.getenv('OPTIMIZER')
    VERBOSE = str_to_bool((os.getenv('VERBOSE')))
    SEED = int(os.getenv('SEED'))
    DETERMINISTIC = str_to_bool((os.getenv('DETERMINISTIC')))
    COSINE_LEARNING_RATE = str_to_bool((os.getenv('COSINE_LEARNING_RATE')))
    CLOSE_MOSAIC = int(os.getenv('CLOSE_MOSAIC'))

    RESUME = str_to_bool(os.getenv('RESUME'))
    AUTOMATIC_MIXED_PRECISION = str_to_bool(os.getenv('AUTOMATIC_MIXED_PRECISION'))
    FRACTION = float(os.getenv('FRACTION'))

    PROFILE = str_to_bool(os.getenv('PROFILE'))

    if str_to_bool(os.getenv('FREEZE_ON')):
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
    OVERLAP_MASK = str_to_bool(os.getenv('OVERLAP_MASK'))
    MASK_RATIO = int(os.getenv('MASK_RATIO'))
    DROPOUT = float(os.getenv('DROPOUT'))
    VALIDATE = str_to_bool(os.getenv('VALIDATE'))
    PLOTS = str_to_bool(os.getenv('PLOTS'))
    LOGGER = os.getenv('LOGGER')

__init()