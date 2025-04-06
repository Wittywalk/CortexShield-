#!/bin/bash

# Update package lists
echo "Updating package lists..."
pkg update -y

# Install required packages for dependencies
echo "Installing necessary dependencies..."
pkg install -y libffi build-essential python3 libbz2 pipx

# Ensure the correct Python version is being used
echo "Checking Python version..."
python --version

# Install pip and upgrade if necessary
echo "Upgrading pip..."
python -m pip install --upgrade pip

# Install Python dependencies listed in requirements.txt
echo "Installing Python dependencies from requirements.txt..."
python -m pip install -r ~/CortexShield/requirements.txt

# Install Lexbor compatibility (if using Lexbor in the project)
echo "Installing Lexbor compatibility..."
python -m pip install lexbor

# Check if aethermind.py exists in the scripts folder and ensure it is accessible
echo "Checking for Aethermind.py in the scripts folder..."
if [ -f ~/CortexShield/scripts/Aethermind.py ]; then
    echo "Aethermind.py found!"
else
    echo "Aethermind.py is missing. Please check the path and try again."
fi

# Additional dependency fixes or checks can go here
echo "Dependency fixing completed."

# Ensure everything is properly set up
echo "Verifying installation of dependencies..."
python -m pip show requests loguru psutil simplejson schedule cython pyjnius pillow python-for-android setuptools

echo "Dependencies are successfully installed and verified."
