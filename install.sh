#!/bin/bash

# Claude Code Agentic System - Installation Script
# For Ubuntu 24.04 LTS

set -e

echo "🤖 Claude Code Agentic System - Installation Script"
echo "=================================================="

# Check if running on Linux
if [[ "$OSTYPE" != "linux-gnu"* ]]; then
    echo "❌ This script is designed for Linux systems"
    exit 1
fi

# Update system packages
echo "📦 Updating system packages..."
sudo apt-get update -y

# Install Python 3 and pip if not already installed
echo "🐍 Installing Python 3 and pip..."
sudo apt-get install -y python3 python3-pip python3-venv

# Install Git if not already installed
echo "📝 Installing Git..."
sudo apt-get install -y git

# Create virtual environment
echo "🔧 Creating Python virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "🔄 Activating virtual environment..."
source venv/bin/activate

# Install Python requirements
echo "📚 Installing Python requirements..."
pip install --upgrade pip
pip install -r requirements.txt

# Create workspace directory
echo "📁 Creating workspace directory..."
mkdir -p workspace
mkdir -p logs

# Set up permissions
echo "🔐 Setting up permissions..."
chmod -R 755 workspace
chmod +x main.py

# Create systemd service file (optional)
if command -v systemctl &> /dev/null; then
    echo "🚀 Creating systemd service..."
    
    cat > claude-agents.service << EOF
[Unit]
Description=Claude Code Agentic Development System
After=network.target

[Service]
Type=simple
User=$USER
WorkingDirectory=$(pwd)
Environment=PATH=$(pwd)/venv/bin
ExecStart=$(pwd)/venv/bin/python main.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
EOF

    echo "📋 Systemd service file created: claude-agents.service"
    echo "   To install: sudo cp claude-agents.service /etc/systemd/system/"
    echo "   To enable: sudo systemctl enable claude-agents"
    echo "   To start: sudo systemctl start claude-agents"
fi

echo ""
echo "✅ Installation completed successfully!"
echo ""
echo "🚀 To start the system:"
echo "   1. Activate the virtual environment: source venv/bin/activate"
echo "   2. Run the system: python main.py"
echo "   3. Open your browser to: http://localhost:5000"
echo ""
echo "📖 For more information, see the README.md file"
echo ""
echo "🎉 Happy coding with Claude Agent System!"