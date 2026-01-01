#!/bin/bash
# Run script for local testing

# Activate virtual environment if it exists
if [ -d "venv" ]; then
    source venv/bin/activate
fi

# Run the game
python src/main.py

