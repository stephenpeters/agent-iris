#!/bin/bash
# Run IRIS agent

cd "$(dirname "$0")"

# Load environment
source .venv/bin/activate

# Set data directory
export MNEMOSYNE_DATA_DIR="/Users/stephenpeters/Library/CloudStorage/Dropbox/Mnemosyne"

# Run service
python main.py
