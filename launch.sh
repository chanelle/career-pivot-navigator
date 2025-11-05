#!/bin/bash
# Career Pivot Navigator - Quick Launch Script

echo "🔥 Career Pivot Navigator - Quick Launch"
echo "=========================================="
echo ""

# Check if .env exists
if [ ! -f ".env" ]; then
    echo "⚠️  Warning: .env file not found in project root"
    echo "Creating .env file..."
    cat > .env << 'EOF'
# Career Pivot Navigator - Environment Variables
# Add your OpenAI API key here

OPENAI_API_KEY=sk-your-key-here

# Optional: Customize LLM settings
# MODEL_NAME=gpt-4o
# TEMPERATURE=0.7
EOF
    echo "✅ Created .env file"
    echo "⚠️  Please edit .env and add your OpenAI API key!"
    echo ""
fi

# Check if virtual environment exists
if [ ! -d ".venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv .venv
    echo "✅ Virtual environment created"
fi

# Activate virtual environment
echo "🔌 Activating virtual environment..."
source .venv/bin/activate

# Check if dependencies are installed
if ! python -c "import langchain" 2>/dev/null; then
    echo "📥 Installing dependencies..."
    pip install -r "Data and Infrastructure/requirements.txt"
    echo "✅ Dependencies installed"
else
    echo "✅ Dependencies already installed"
fi

echo ""
echo "Select mode:"
echo "1) CLI Mode (default)"
echo "2) Web Interface (Streamlit)"
echo ""
read -p "Choice (1 or 2): " choice

cd "Core Logic"

case $choice in
    2)
        echo ""
        echo "🌐 Launching Streamlit web interface..."
        echo "Open browser to: http://localhost:8501"
        echo ""
        python main.py streamlit
        ;;
    *)
        echo ""
        echo "💻 Launching CLI mode..."
        echo ""
        python main.py
        ;;
esac
