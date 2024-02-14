import subprocess
from  dotenv import load_dotenv
from abc import abstractmethod
from config import LOGGER, PROJECT, NAME

import clearml, comet_ml 


class Logger:
    def __init__(self):
        load_dotenv()

    @abstractmethod
    def setup(self): ...

class ClearMLLogger(Logger): 
    def __init__(self):
        super().__init__()

    def setup(self):
        subprocess.run("clearml-init", shell=True) 
        clearml.Task.init(project_name=PROJECT, task_name=NAME)

class CometLogger(Logger):
    def __init__(self):
        super().__init__()
        
    def setup(self):
        comet_ml.init(project_name=PROJECT, workspace=NAME)
    
        
def get_logger() -> Logger | None:
    match LOGGER:
        case "CLEAR_ML":
            return ClearMLLogger()

        case "COMET_ML":
            return CometLogger()

        case "0":
            return None
