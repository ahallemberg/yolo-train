# yolov8-train

## Setup 

### Logger 

#### Comet ML 
Setup a .env file with the COMET_ML api key if you want to use comet<br/>
COMET_API_KEY=<br/>

#### ClearML 
Setup a clearml.conf file with configs if you want to use clearml. This needs to be at home dir level. ~/clearml.conf<br />

#### Weight and Biases
Create a file called ~/.netrc that looks like this<br />

machine api.wandb.ai<br />
&nbsp;&nbsp;&nbsp;&nbsp;login user<br />
&nbsp;&nbsp;&nbsp;&nbsp;password API_KEY<br />

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
-v|--venv (to train in a new venv)
-t|--tune (to tune insted of standard training)
-r|--reset (to reset config to default)
```



