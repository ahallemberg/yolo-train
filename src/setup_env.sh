#!/bin/bash

# create venv
if [ "$CREATE_VENV" = true ]; then
    echo "Creating virtual environment..."
    python3 -m venv "${PROJECT_DIR}/.venv"
    source "${PROJECT_DIR}/.venv/bin/activate"
    echo "Virtual environment created"
fi

# Check if pip is installed by trying to invoke pip via Python
if python3 -m pip -V >/dev/null 2>&1; then
    echo "pip is already installed."
else
    echo "pip not found, checking OS..."

    # Check for Debian/Ubuntu and install pip using apt-get
    if [ -f /etc/debian_version ]; then
            echo "Attempting to install pip using apt-get..."
            sudo apt-get install -y python3-pip
    else
        python3 -m ensurepip
        python3 -m pip install --upgrade pip
    fi

    if python3 -m pip -V >/dev/null 2>&1; then
        echo "pip has been successfully installed."
    else
        echo "Failed to install pip. Please manually install pip."
    fi
fi

# Check if PyYAML is installed
if ! python3 -m pip show PyYAML > /dev/null 2>&1; then
    python3 -m pip install PyYAML
fi


if [ "$TASK" = "tune" ] && [ "$(python3 "${PROJECT_DIR}/src/use_ray.py")" = "1" ]; then
    # Check if Ray Tune is installed
    if ! python3 -m pip show ray > /dev/null 2>&1; then
        # Try to install Ray Tune
        if ! python3 -m pip install "ray[tune]" > /dev/null 2>&1; then
            echo "Ray Tune could not be installed. It may not be supported on this device. Ether intall it manually, or set use_ray to False in tune.yaml"
            exit 1
        fi
    fi
fi

# check if ultrralytics is installed
if ! python3 -m pip show ultralytics > /dev/null 2>&1; then
    echo "ultralytics is not installed. Installing ultralytics..."
    python3 -m pip install ultralytics
else 
    echo "ultralytics is already installed"
fi

yolo settings datasets_dir="${PROJECT_DIR}/datasets" weights_dir="${PROJECT_DIR}/weights" runs_dir="${PROJECT_DIR}/runs"

eval "$(python3 "${PROJECT_DIR}/src/export_logger.py")"

# check if logger is CLEAR_ML
if [ "$LOGGER" = "CLEAR_ML" ]; then
    # check if clearml is already configured
    yolo settings clearml=True
    if [ -z "$CLEARML_IS_CONFIGURED" ]; then
        # check if clearml is installed pip
        if ! python3 -m pip show clearml > /dev/null 2>&1; then
            echo "clearml is not installed. Installing clearml..."
            python3 -m pip install clearml
            echo "clearml is now installed"
        fi

        # check if clearml.conf exists
        if [ -f ~/clearml.conf ]; then
            echo "Found clearml.conf in home dir. configuring env for ClearML..."
        else
            echo "clearml.conf not found. Trying to configure without it..."
        fi
        clearml-init 
        export CLEARML_IS_CONFIGURED=1
        echo "ClearML env is now configured"
    
    else
        echo "ClearML is already configured"
    fi

elif [ "$LOGGER" = "COMET_ML" ]; then
    unset $COMET_AUTO_LOG_DISABLE
    yolo settings comet=True
    # check if comet_ml is installed pip
    if ! python3 -m pip show comet_ml > /dev/null 2>&1; then
        echo "comet_ml is not installed. Installing comet_ml..."
        python3 -m pip install comet_ml
        echo "comet_ml is now installed"
    fi

    # Check if python-dotenv is installed
    if ! python3 -m pip show python-dotenv > /dev/null 2>&1; then
        echo "python-dotenv is not installed. Installing..."
        python3 -m pip install python-dotenv
    fi

    # check if comet_ml is already configured
    if [ -z "$COMET_ML_IS_CONFIGURED" ]; then
        echo "configuring env for Comet ML..."
        set -a
        source .env
        set +a
        export COMET_ML_IS_CONFIGURED=1 
        echo "Comet ML env is now configured"
    else
        echo "Comet ML env is configured"
    fi

elif [ "$LOGGER" = "WANDB" ]; then
    yolo settings wandb=True
    # check if wandb is installed pip
    if ! python3 -m pip show wandb > /dev/null 2>&1; then
        echo "wandb is not installed. Installing wandb..."
        python3 -m pip install wandb
        echo "wandb is now installed"
    fi

    if [ -f ~/.netrc ]; then
        echo "Found ~/.netrc. Trying to autologin..."
    else
        echo "~/.netrc not found. Trying to login wothout it..."
    fi

    wandb login

else
    echo "No logger is set. Skipping logger configuration..."
fi

if [ "$LOGGER" != "CLEAR_ML" ]; then
    yolo settings clearml=False
fi

if [ "$LOGGER" != "COMET_ML" ]; then
    export COMET_AUTO_LOG_DISABLE=1 # disable comet auto logging
    yolo settings comet=False
fi

if [ "$LOGGER" != "WANDB" ]; then
    yolo settings wandb=False
fi