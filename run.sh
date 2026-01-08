#!/bin/bash

# Password Strength Analyzer - Startup Script

echo "🔐 Password Strength Analyzer"
echo "================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

echo "✓ Python found: $(python3 --version)"
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
    echo "✓ Virtual environment created"
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Install requirements
echo "📥 Installing dependencies..."
pip install -r requirements.txt -q
echo "✓ Dependencies installed"

echo ""
echo "================================"
echo "🚀 Starting application..."
echo "📱 Open your browser and go to: http://127.0.0.1:5000"
echo "⌨️  Press Ctrl+C to stop the server"
echo "================================"
echo ""

# Run the Flask app
python3 app.py
