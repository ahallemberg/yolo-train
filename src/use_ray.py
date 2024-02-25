import os
import yaml 

with open(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "params", "tune.yaml")), 'r') as f:
    data = yaml.safe_load(f)
    
    if "use_ray" in data["params"]:
        if data["params"]["use_ray"]:
            print("1")
        else: 
            print("0")
    else:
        print("export LOGGER=0")
