source config.sh

# Export all variables in .env file

# check if logger is CLEAR_ML
if [ "$LOGGER" = "CLEAR_ML" ]; then
    # check if clearml is already configured
    if [ -z "$CLEARML_IS_CONFIGURED" ]; then
        # check if clearml is installed pip
        if ! [ -x "$(command -v clearml-init)" ]; then
            echo "clearml is not installed. Installing clearml..."
            python3 -m pip install clearml
            echo "clearml is now installed"
        fi

        # check if clearml.conf exists
        if [ -f "clearml.conf" ]; then
            # configure clearml
            echo "configuring env for ClearML..."
            clearml-init --file clearml.conf
            export CLEARML_IS_CONFIGURED=1
            echo "ClearML env is now configured"
        else
            echo "clearml.conf not found. Trying to configure without it..."
            # configure clearml
            clearml-init
            export CLEARML_IS_CONFIGURED=1
            echo "ClearML env is now configured"
        fi
    
    else
        echo "ClearML is already configured"
    fi

elif [ "$LOGGER" = "COMET_ML" ]; then
    # check if comet_ml is installed pip
    if ! [ -x "$(command -v comet)" ]; then
        echo "comet_ml is not installed. Installing comet_ml..."
        pip install comet_ml
        echo "comet_ml is now installed"
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
    for var in $(env | grep -E 'COMET' | cut -d= -f1); do
        unset $var
    done
    export COMET_AUTO_LOG_DISABLE=1 # disable comet auto logging
fi

if [ "$LOGGER" != "COMET_ML" ]; then
    for var in $(env | grep -E 'CLEARML' | cut -d= -f1); do
        unset $var
    done
fi