#!/bin/bash

# Function to check if a command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Determine whether to use python3 or python
if command_exists python3; then
    PYTHON=python3
elif command_exists python; then
    PYTHON=python
else
    echo "Error: Python is not installed."
    exit 1
fi

# Pull the latest changes
echo "Pulling the latest changes..."
git pull || { echo "Error: Failed to pull the latest changes."; exit 1; }

# Remove the local database if it exists
if [ -f db.sqlite3 ]; then
    echo "Removing the existing database..."
    rm db.sqlite3 || { echo "Error: Failed to remove the database."; exit 1; }
else
    echo "No existing database found. Skipping removal."
fi

# Build virtual environment
echo "Creating virtual environment..."
$PYTHON -m venv venv || { echo "Error: Failed to create virtual environment."; exit 1; }

# Activate the virtual environment
echo "Activating virtual environment..."
source venv/bin/activate || { echo "Error: Failed to activate virtual environment."; exit 1; }

# Install the requirements
echo "Installing requirements..."
pip install -r requirements.txt || { echo "Error: Failed to install requirements."; exit 1; }

# Recreate the database
echo "Applying migrations..."
python manage.py migrate || { echo "Error: Failed to apply migrations."; exit 1; }

# Clear existing content types to avoid conflicts
echo "Clearing existing content types..."
python manage.py shell -c "from django.contrib.contenttypes.models import ContentType; ContentType.objects.all().delete()" || { echo "Error: Failed to clear content types."; exit 1; }

# Load the new data
echo "Loading initial data..."
python manage.py loaddata init_data.json || { echo "Error: Failed to load initial data."; exit 1; }

echo "Database updated successfully."