"""
Pytest configuration and fixtures for tests.
"""

import os
import django
import pytest
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Configure Django if not already configured
if not settings.configured:
    django.setup()


@pytest.fixture
def django_db_setup():
    """Configure Django database for tests."""
    settings.DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }


@pytest.fixture
def api_client():
    """Provide Django test client."""
    from django.test import Client
    return Client()
