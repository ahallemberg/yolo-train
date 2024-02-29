import yaml
import os
import torch

task = os.getenv("TASK")
if task == "tune":
    basename = "tune.yaml"
elif task == "train":
    basename = "train.yaml"
else: 
    raise RuntimeError(f"Invalid value for env varable TASK: {task}")

config_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "config", basename))

with open(config_path, 'r') as f:
    data = yaml.safe_load(f)
    if "device" in data["params"]:
        device = data["params"]["device"]

        if device in ["auto", None]: 
            if torch.cuda.is_available():
                device_count = torch.cuda.device_count()
                data["params"]["device"] = list(range(device_count))

with open(config_path, 'w') as f:
    yaml.dump(data, f)