import os
from typing import Any, Union
from abc import ABC, abstractmethod
from config import cfg
import secrets
from ultralytics import YOLO


class Logger(ABC):
    @abstractmethod
    def setup(self): ...

    @abstractmethod
    def connect(self, args: dict[str, Any], model: YOLO): ...

    def get_id(self) -> str:
        return secrets.token_hex(8)


class ClearMLLogger(Logger): 
    def __init__(self, task_class):
        self.task_class = task_class
        self.id = self.get_id()

    def setup(self):
        self.task = self.task_class.init(project_name=cfg.params["name"]+self.id, task_name=cfg.params["name"])
    
    def connect(self, args: dict[str, Any], model: YOLO):
        self.task.connect(args)


class CometLogger(Logger):
    def __init__(self, lib):
        self.lib = lib
        self.id = self.get_id()
        from dotenv import load_dotenv
        load_dotenv()
        
    def setup(self):
        self.lib.init(project_name=cfg.params["name"]+self.id)
        self.experiment = self.lib.Experiment(project_name=cfg.params["name"]+self.id)

    def connect(self, args: dict[str, Any], model: YOLO):
        self.experiment.log_parameters(args)


class WANDBLogger(Logger):
    def __init__(self, lib):
        self.lib = lib
        self.id = self.get_id()
        
    def setup(self):
        # Step 1: Initialize a Weights & Biases run
        task = os.getenv("TASK")
        self.lib.init(project=cfg.params["name"]+self.id, job_type=task)

    def connect(self, args: dict[str, Any], model: YOLO):
        from wandb.integration.ultralytics import add_wandb_callback
        add_wandb_callback(model)

    def __del__(self):
        self.lib.finish()

        
def get_logger() -> Union[None, Logger]:
    logger = os.getenv("LOGGER")

    if logger == "CLEAR_ML":
        from clearml import Task
        return ClearMLLogger(Task)
    
    elif logger == "COMET_ML":
        import comet_ml
        return CometLogger(comet_ml)
    
    elif logger == "WANDB":
        import wandb
        return WANDBLogger(wandb)
    
    elif logger == "0":
        return None
    
    else:
        raise ValueError(f"Invalid value for env varable LOGGER: {logger}")