#!/bin/bash
# Installation script for Smart Clipboard Manager

echo "🚀 Installing Smart Clipboard Manager..."

# Check Python version
python_version=$(python3 --version 2>&1 | awk '{print $2}')
echo "Python version: $python_version"

# Create virtual environment (optional but recommended)
read -p "Create virtual environment? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]
then
    echo "Creating virtual environment..."
    python3 -m venv venv
    source venv/bin/activate
fi

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Platform-specific dependencies
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    echo "Detected Linux"
    echo "Installing xdotool for app detection..."
    sudo apt-get install -y xdotool
elif [[ "$OSTYPE" == "darwin"* ]]; then
    echo "Detected macOS"
    echo "No additional dependencies needed"
elif [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    echo "Detected Windows"
    echo "Installing Windows-specific dependencies..."
    pip install pywin32 psutil
fi

echo ""
echo "✅ Installation complete!"
echo ""
echo "To start the Smart Clipboard Manager, run:"
echo "  python main.py"
echo ""
echo "Or if you created a virtual environment:"
echo "  source venv/bin/activate"
echo "  python main.py"

