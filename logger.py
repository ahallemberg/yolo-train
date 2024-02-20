from  dotenv import load_dotenv

from abc import ABC, abstractmethod
from config import LOGGER, NAME, ID

class Logger(ABC):
    @abstractmethod
    def setup(self): ...
    
    @abstractmethod
    def connect(self, args: dict): ...

class ClearMLLogger(Logger): 
    def __init__(self, task_class):
        self.task_class = task_class
    def setup(self):
        self.task = self.task_class.init(project_name=NAME+ID, task_name=NAME)
    
    def connect(self, args: dict):
        self.task.connect(args)

class CometLogger(Logger):
    def __init__(self, lib):
        self.lib = lib
        load_dotenv()
        
    def setup(self):
        self.lib.init(project_name=NAME+ID)
        self.experiment = self.lib.Experiment(project_name=NAME+ID)

    def connect(self, args: dict):
        self.experiment.log_parameters(args)
        
def get_logger() -> Logger | None:
    match LOGGER:
        case "CLEAR_ML":
            from clearml import Task
            return ClearMLLogger(Task)

        case "COMET_ML":
            import comet_ml 
            return CometLogger(comet_ml)

        case "0":
            return None
        case _:
            raise ValueError(f"Invalid value for env varable LOGGER: {LOGGER}")
