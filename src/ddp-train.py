import os
import torch
import torch.distributed as dist
from ultralytics import YOLO
from config import cfg
from logger import get_logger

def main():
    # Initialize the distributed environment.
    dist.init_process_group(backend='nccl')
    local_rank = torch.distributed.get_rank()
    torch.cuda.set_device(local_rank)
    
    # setup environment
    os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
    
    # Load and wrap the model for DDP
    model = YOLO(cfg.weights)
    model.cuda(local_rank)
    model = torch.nn.parallel.DistributedDataParallel(model, device_ids=[local_rank], output_device=local_rank)
    
    # setup logger 
    logger = get_logger()
    if logger: 
        logger.setup()
        logger.connect(cfg.params, model.module)
  
    # train/tune model with the configurations
    task = os.getenv("TASK")
    if task == "tune":
        model.module.tune(**cfg.params)
    elif task == "train":
        model.module.train(**cfg.params) 
    else: 
        raise RuntimeError("Invalid task")

if __name__ == "__main__": 
    main()
else:
    raise RuntimeError("This script is meant to be run as a standalone script")
