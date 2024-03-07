import os
import torch.distributed as dist
from ultralytics import YOLO
from config import cfg
from logger import get_logger


def main():
    print("WORKKKKING")
    # Initialize the distributed environment.
    dist.init_process_group(
        init_method='env://',
        backend=os.getenv("BACKEND")
    )

    # setup environment
    os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
    
    # Load and wrap the model for DDP
    model = YOLO(cfg.weights)


    # setup logger s
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
