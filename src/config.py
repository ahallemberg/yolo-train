import os
import secrets
import yaml

class Config():
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Config, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self, u: str):
        if not self._initialized:
            self.id = secrets.token_hex(8)
            if u == "tune":
                self.load_params("tune.yaml", ["name", "data", "project", "epochs", "iterations"])
            elif u == "train":
                self.load_params("train.yaml", ["name", "data", "project", "epochs"])
            else: 
                raise ValueError(f"Invalid value for parameter: {u}")
            
            self._initialized = True

    def load_params(self, base_name: str, required: list[str]):
        target_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "config", base_name))
        with open(target_file, 'r') as f:
            data = yaml.safe_load(f)
            self.params = data["params"]
            self.weights = data["weights"]

        for key in required:
            if key not in self.params:
                raise ValueError(f"Missing required parameter: {key}")
            elif not self.params[key]:
                raise ValueError(f"Invalid value for parameter: {key}")

task = os.getenv("TASK")          
if task == "tune":
    cfg = Config("tune")
elif task == "train":
    cfg = Config("train")
else: 
    raise RuntimeError(f"Invalid value for env varable TASK: {task}")
