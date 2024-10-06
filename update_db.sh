#!/bin/bash

# Pull the latest changes
git pull

# Remove the local database
rm db.sqlite3

# Recreate the database
python manage.py migrate

# Load the new data
python manage.py loaddata init_data.json

echo "Database updated successfully."