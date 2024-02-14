import os, subprocess
from  dotenv import load_dotenv
from abc import abstractmethod, ABC
from config import LOGGER, NAME, PROJECT
import clearml, comet_ml 


class Logger(ABC):
    @abstractmethod
    def setup(self): ...

    def _load_dotenv(self):
        load_dotenv()

class ClearMLLogger(Logger): 
    def setup(self):
        ## load all the env variables
        self._load_dotenv()

        subprocess.run("clearml-init", shell=True) 
        clearml.Task.init(project_name=PROJECT, task_name=NAME)
        print("CLEARML")

class CometLogger(Logger):
    def setup(self):
        self._load_dotenv()

        comet_ml.init()
        print("COMET")

        
def get_logger():
    match LOGGER:
        case "CLEARML":
            return ClearMLLogger()

        case "COMET":
            return CometLogger()

        case "0":
            return None
