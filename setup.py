"""
Helper script to set up Django and load initial data.
Run this after installing dependencies.
"""

import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

# Run migrations
from django.core.management import call_command

print("Running migrations...")
call_command('migrate')

print("Loading initial data...")
call_command('load_initial_data')

print("Setup complete! You can now run the server with:")
print("python manage.py runserver")
