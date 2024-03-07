# yolo-train

## Setup 

### Logger 

#### Comet ML 
Setup a .env file with the COMET_ML api key if you want to use comet<br/>
```
COMET_API_KEY=YOUR_API_KEY
```

#### ClearML 
Setup a clearml.conf file with configs found on the clearml website if you want to use clearml. This needs to be at home dir level. ~/clearml.conf<br />

#### Weight and Biases
Create a file called ~/.netrc that looks like this<br />

```
machine api.wandb.ai
    login user
    password YOUR_API_KEY
```

### Config
To change training configurations, edit the yaml file config/train.yaml, or config/tune.yaml for tuning

### Dataset 
Move training dataset(s) to the datasets folder

## Usage 
### Train
Make train file executable

Execute file
```
./train
```

#### Options
```
-v|--venv   (to train in a new venv)
-t|--tune   (to tune insted of standard training)
-r|--reset  (to reset config to default)
```

### DDP 
Execute file on each node with the correct options
```
./train-ddp --nproc_per_node 1 --nnodes 2 --node_rank 0 --master_addr "10.0.20.1" --master_port 8456
```


#### Required options
```
--nproc_per_node  (The number of processes to run on each node)
--nnodes          (The total number of nodes)
--node_rank       (The rank of the current node)
--master_addr     (The address of the master node)
--master_port     (The port of the master node)
```


