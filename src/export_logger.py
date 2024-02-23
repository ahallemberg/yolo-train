import yaml
import os

task = os.getenv("TASK")
if task == "tune":
    basename = "tune.yaml"
elif task == "train":
    basename = "train.yaml"
else: 
    raise RuntimeError(f"Invalid value for env varable TASK: {task}")

with open(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "params", basename)), 'r') as f:
    data = yaml.safe_load(f)
    if "logger" in data:
        print(f"export LOGGER={data['logger']}")
    else:
        print("export LOGGER=0")
