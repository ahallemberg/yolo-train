import os 
from ultralytics import YOLO
from config import cfg
from logger import get_logger

def main():
    # setup environment
    os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
    
    # Load a model
    model = YOLO(cfg.weights)  

    # setup logger 
    logger = get_logger()
    if logger: 
        logger.setup()
        logger.connect(cfg.params, model)

  
    # train/tune model with the configurations
    task = os.getenv("TASK")
    if task == "tune":
        model.tune(**cfg.params)
    elif task == "train":
        model.train(**cfg.params)
    else: 
        raise RuntimeError("Invalid task")

if __name__ == "__main__": 
    main()
else:
    raise RuntimeError("This script is meant to be run as a standalone script")
