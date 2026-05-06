# Care Access Portal - Backend 🏥

## 📖 Overview

This repository contains the backend APIs for the Care Access Portal built with Django.

The backend handles:

- Authentication
- Appointments
- Patient Records
- Doctor Data

## ✨ Features

- REST API Services with Django REST Framework
- Role-Based Login
- CRUD Operations
- JSON Responses
- CORS Enabled
- SQLite Database
- Django Admin Interface

## 🛠️ Tech Stack

- Python 3.8+
- Django 4.2+
- Django REST Framework
- django-cors-headers
- Gunicorn

## 🚀 Installation & Setup

```bash
git clone https://github.com/simple-code200/CareAccess-Backend.git
cd backend
pip install -r requirements.txt
python setup.py  # Runs migrations and loads initial data
python manage.py runserver
```

The backend will be available at `http://127.0.0.1:8000/`

### 🧪 Testing and Linting

```bash
pip install -r requirements-dev.txt
pytest
pylint api/
```

### 🔧 Django Management Commands

```bash
# Run migrations
python manage.py migrate

# Load initial data
python manage.py load_initial_data

# Create superuser for admin panel
python manage.py createsuperuser

# Access Django admin at http://127.0.0.1:8000/admin
```

## 📁 Project Structure

```bash
backend/
├── manage.py
├── setup.py
├── pytest.ini
├── requirements.txt
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── __init__.py
├── api/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── urls.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   ├── management/
│   │   └── commands/
│   │       └── load_initial_data.py
│   └── __init__.py
└── tests/
├── README.md
└── .gitignore
```
