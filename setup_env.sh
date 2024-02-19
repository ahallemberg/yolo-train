source config.sh

# Export all variables in .env file

# check if logger is CLEAR_ML
if [ "$LOGGER" = "CLEAR_ML" ]; then
    # check if clearml is already configured
    if [ -z "$CLEARML_IS_CONFIGURED" ]; then
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