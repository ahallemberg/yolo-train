CREATE_VENV=false
TUNING=false
RESET=false

help_options (){
    echo "Usage: train [OPTIONS]"
    echo "Options:"
    echo "  -v, --venv   Create a virtual environment"
    echo "  -t, --tune   Tune the model"
    echo "  -r, --reset  Reset the parameters to default"
    exit 1
}

get_options(){
  TEMP=$(getopt -o vrt --long venv,tune,reset -n 'train' -- "$@")
    if [ $? != 0 ]; then echo "Terminating..." >&2; exit 1; fi

    eval set -- "$TEMP"

    while true; do
        case "$1" in
            -v|--venv)
                CREATE_VENV=true
                shift
                ;;
            -r|--reset)
                RESET=true
                shift
                ;;
            -t|--tune)
                TUNING=true
                shift
                ;;
            --)
                shift
                break
                ;;
            *)
                help
                ;;
        esac
    done

    set_options
}

set_options() {
    if [ "$RESET" = true ]; then
        reset
    fi

    export CREATE_VENV=$CREATE_VENV

    if [ "$TUNING" = true ]; then
        export TASK=tune
    else
        export TASK=train
    fi

    if [ "$RESET" = true ]; then
        reset
    fi
}

help_ddp_options() {
    echo "Usage: train-ddp [OPTIONS]"
    echo "Options:"
    echo "  --nproc_per_node   Number of processes per node"
    echo "  --nnodes           Number of nodes"
    echo "  --node_rank        Rank of the node"
    echo "  --master_addr      IP address of the master node"
    echo "  --master_port      Port of the master node"
    exit 1
}

get_ddp_options(){
    TEMP=$(getopt -o vrt --long venv,reset,tune,nproc_per_node:,nnodes:,node_rank:,master_addr:,master_port: -n 'train-ddp' -- "$@")    
    if [ $? != 0 ]; then echo "Terminating..." >&2; exit 1; fi

    eval set -- "$TEMP"

    while true; do
        case "$1" in
            -v|--venv)
                CREATE_VENV=true
                shift
                ;;
            -r|--reset)
                RESET=true
                shift
                ;;
            -t|--tune)
                TUNING=true
                shift
                ;;
            --nproc_per_node)
                export NPROC_PER_NODE=$2
                shift 2
                ;;
            --nnodes)
                export NNODES=$2
                shift 2
                ;;
            --node_rank)
                export NODE_RANK=$2
                shift 2
                ;;
            --master_addr)
                export MASTER_ADDR=$2
                shift 2
                ;;
            --master_port)
                export MASTER_PORT=$2
                shift 2
                ;;
            --)
                shift
                break
                ;;
            *)
                help
                ;;
        esac
    done

    set_options

    if [ -z "$NPROC_PER_NODE" ] || [ -z "$NNODES" ] || [ -z "$NODE_RANK" ] || [ -z "$MASTER_ADDR" ] || [ -z "$MASTER_PORT" ]; then
        echo "Error: All of the following options must be provided:"
        echo "--nproc_per_node"
        echo "--nnodes"
        echo "--node_rank"
        echo "--master_addr"
        echo "--master_port"
        exit 1
    fi
}

reset(){
    echo "Resetting parameters to default..."
    cp "${PROJECT_DIR}/.default/train.yaml" "${PROJECT_DIR}/config/train.yaml"
    cp "${PROJECT_DIR}/.default/tune.yaml" "${PROJECT_DIR}/config/tune.yaml"
    cp "${PROJECT_DIR}/.default/data.yaml" "${PROJECT_DIR}/datasets/data.yaml"
    exit 0
}

cleanup_env(){
    if [ "$CREATE_VENV" = true ]; then
        echo "Removing virtual environment..."
        if deactivate > /dev/null 2>&1; then
            deactivate
        fi 
        rm -rf "${PROJECT_DIR}/.venv"
        echo "Virtual environment removed"
    fi
}