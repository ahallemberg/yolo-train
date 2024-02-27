# remove venv
if [ "$CREATE_VENV" = true ]; then
    echo "Removing virtual environment..."
    deactivate
    rm -rf "${PROJECT_DIR}/.venv"
    echo "Virtual environment removed"
fi
