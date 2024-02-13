from ultralytics import YOLO
from datetime import datetime



# Load a model

model = YOLO("yolov8n.pt")  # load a pretrained model (recommended for training)

model.train(
    data="config.yaml", 
    time= None,
    epochs=3,
    batch=16,
    patience=3,
    imsz=640,
    save_period=1,
    cache=True,
    device="cpu",
    project="runs/train/",
    name=datetime.now().strftime("%Y-%m-%d_%H:%M:%S"),
    verbose=True,
    plots=True
)  
