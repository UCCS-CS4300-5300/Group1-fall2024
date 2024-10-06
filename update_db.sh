#!/bin/bash

# Pull the latest changes
git pull

# Remove the local database
rm db.sqlite3

# build venv
python3 -m venv venv

# Activate the virtual environment

source venv/bin/activate

# Install the requirements

pip install -r requirements.txt

# Recreate the database
python manage.py migrate

# Load the new data
python manage.py loaddata init_data.json

echo "Database updated successfully."