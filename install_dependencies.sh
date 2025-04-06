#!/bin/bash

# Install Termux dependencies
if [ "$(uname)" == "Linux" ] && [ -f "/data/data/com.termux/files/usr/bin/bash" ]; then
    echo "Installing Termux dependencies..."
    pkg install -y $(cat termux_dependencies.txt)

# Install Debian/Ubuntu dependencies
elif [ -f "/usr/bin/apt" ] && [ ! -f "/data/data/com.termux/files/usr/bin/bash" ]; then
    echo "Installing Debian/Ubuntu dependencies..."
    sudo apt-get install -y $(cat debian_apt_dependencies.txt)

# Install Andronix dependencies
elif [ -f "/usr/bin/apt" ] && [ -f "/data/data/com.termux/files/usr/bin/bash" ]; then
    echo "Installing Andronix dependencies..."
    sudo apt-get install -y $(cat andronix_dependencies.txt)
fi

# Install Python dependencies
echo "Installing Python dependencies..."
pip install -r requirements.txt
