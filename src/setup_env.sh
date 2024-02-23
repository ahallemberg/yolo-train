#!/bin/bash

# Check if pip is installed by trying to invoke pip via Python
if python3 -m pip -V >/dev/null 2>&1; then
    echo "pip is already installed."
else
    echo "pip not found, checking OS..."

    # Check for Debian/Ubuntu and install pip using apt-get
    if [ -f /etc/debian_version ]; then
            echo "Attempting to install pip using apt-get..."
            sudo apt-get update
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

# check if ultrralytics is installed
if ! [ -x "$(command -v ultralytics)" ]; then
    echo "ultralytics is not installed. Installing ultralytics..."
    python3 -m pip install ultralytics
fi 

eval $(python3 "${PROJECT_DIR}/src/export_logger.py")

# check if logger is CLEAR_ML
if [ "$LOGGER" = "CLEAR_ML" ]; then
    # check if clearml is already configured
    yolo settings clearml=True
    if [ -z "$CLEARML_IS_CONFIGURED" ]; then
        # check if clearml is installed pip
        if ! [ -x "$(command -v clearml-init)" ]; then
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
    if ! [ -x "$(command -v comet)" ]; then
        echo "comet_ml is not installed. Installing comet_ml..."
        python3 -m pip install comet_ml
        echo "comet_ml is now installed"
    fi

    # Check if python-dotenv is installed
    if ! python3 -c "import dotenv" 2>/dev/null; then
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