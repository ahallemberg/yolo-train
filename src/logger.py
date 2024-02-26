import os
from typing import Any
from abc import ABC, abstractmethod
from config import cfg
import secrets

class Logger(ABC):
    @abstractmethod
    def setup(self): ...
    
    @abstractmethod
    def connect(self, args: dict[str, Any]): ...

    def get_id(self) -> str:
        return secrets.token_hex(8)

class ClearMLLogger(Logger): 
    def __init__(self, task_class):
        self.task_class = task_class
        self.id = self.get_id()
    def setup(self):
        self.task = self.task_class.init(project_name=cfg.params["name"]+self.id, task_name=cfg.params["name"])
    
    def connect(self, args: dict[str, Any]):
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

    def connect(self, args: dict[str, Any]):
        self.experiment.log_parameters(args)

class WANDBLogger(Logger):
    def __init__(self, lib):
        self.lib = lib
        self.id = self.get_id()
        
    def setup(self):
        pass

    def connect(self, args: dict[str, Any]):
        self.lib.log(args)
        
def get_logger() -> Logger | None:
    logger = os.getenv("LOGGER")
    match logger:
        case "CLEAR_ML":
            from clearml import Task
            return ClearMLLogger(Task)

        case "COMET_ML":
            import comet_ml 
            return CometLogger(comet_ml)

        case "0":
            return None
        case _:
            raise ValueError(f"Invalid value for env varable LOGGER: {logger}")
