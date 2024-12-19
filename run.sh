#!/bin/bash


# Update package list and install ffmpeg
echo "Installing ffmpeg..."
sudo apt update && sudo apt install -y ffmpeg

# Check if pip is installed
if ! command -v pip &>/dev/null; then
    echo "pip is not installed. Installing pip..."
    sudo apt install -y python3-pip
fi

# Install Python dependencies
if [[ -f "requirements.txt" ]]; then
    echo "Installing Python dependencies from requirements.txt..."
    pip install -r requirements.txt
else
    echo "requirements.txt file not found. Skipping Python dependencies installation."
fi

# Tunnel port 5000 using Serveo
echo "Tunneling port 5000 using Serveo..."
read -p "Enter the desired Serveo subdomain: " SUBDOMAIN

ssh -R "${SUBDOMAIN}:80:localhost:5000" serveo.net &

# Run app.py
if [[ -f "app.py" ]]; then
    echo "Running app.py..."
    python3 app.py
else
    echo "app.py not found in the current directory. Exiting."
fi

echo "Setup complete. ffmpeg installed, Python dependencies handled, Serveo tunneling active, and app.py launched (if available)."
