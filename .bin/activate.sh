#!/bin/bash
# Activate Python virtual environment from the project root

if [ -d "venv" ]; then
  source venv/bin/activate
  echo "Virtual environment activated."
else
  echo "No venv directory found in the project root."
fi