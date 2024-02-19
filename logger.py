from  dotenv import load_dotenv

from abc import ABC, abstractmethod
from config import LOGGER, PROJECT, NAME

class Logger(ABC):
    @abstractmethod
    def setup(self): ...

class ClearMLLogger(Logger): 
    def __init__(self, lib):
        self.lib = lib
    def setup(self):
        self.lib.Task.init(project_name=PROJECT, task_name=NAME)

class CometLogger(Logger):
    def __init__(self, lib):
        self.lib = lib
        load_dotenv()
        
    def setup(self):
        self.lib.init(project_name=PROJECT, workspace=NAME)

    
        
def get_logger() -> Logger | None:
    match LOGGER:
        case "CLEAR_ML":
            import clearml
            return ClearMLLogger(clearml)

        case "COMET_ML":
            import comet_ml 
            return CometLogger(comet_ml)

        case "0":
            return None
        case _:
            raise ValueError(f"Invalid value for env varable LOGGER: {LOGGER}")
