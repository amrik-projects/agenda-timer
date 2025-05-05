#!/bin/bash
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install PyQt6
echo "Setup complete. To activate the environment, run: source venv/bin/activate"