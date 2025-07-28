#!/bin/bash

# Set the name of your virtual environment folder
VENV_DIR="venv"

# Check if the virtual environment directory exists
if [ ! -d "$VENV_DIR" ]; then
    echo "Virtual environment not found, creating one..."

    # Create a virtual environment
    python3 -m venv $VENV_DIR
    
    echo "Virtual environment created in '$VENV_DIR'."

    # Activate the virtual environment
    source $VENV_DIR/bin/activate

    # Check if requirements.txt exists and install the dependencies
    if [ -f "requirements.txt" ]; then
        echo "Found requirements.txt, installing dependencies..."
        pip install -r requirements.txt
    else
        echo "No requirements.txt found. You can manually install dependencies later."
    fi
else
    echo "Virtual environment already exists. Activating..."

    # Activate the existing virtual environment
    source $VENV_DIR/bin/activate
fi

echo "Virtual environment is now activated."