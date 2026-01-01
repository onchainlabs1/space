#!/bin/bash
# Build script for web version using pygbag

# Activate virtual environment if it exists
if [ -d "venv" ]; then
    source venv/bin/activate
fi

# Build for web
python -m pygbag --template index.html src/main.py

echo "Build complete! Output is in build/web/"
echo "To serve locally, run: cd build/web && python -m http.server 8000"

