# yolov8-train

## Setup 

### Logger 

#### Comet ML 
Setup a .env file with the COMET_ML api key if you want to use comet<br/>
COMET_API_KEY=<br/>

#### ClearML 
Setup a clearml.conf file with configs if you want to use clearml. This needs to be at home dir level. ~/clearml.conf<br

#### Weight and Biases
Set WANDB_API_KEY in a file named ~/.netrc

### Config
To change training params, edit the yaml file config/train.yaml, or config/tune.yaml for tuning


### Dataset 
Move training dataset(s) to the datasets folder

## Usage
Make train file executable
```
chmod +x train 
```

Execute file
```
./train
```

### Options
```
--venv (to train in a new venv)
--tune (to tune insted of standard training)
--reset (to reset config to default)
```



