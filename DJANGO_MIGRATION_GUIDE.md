# Django Backend Migration Guide

## What Changed

✅ **Flask → Django**

- Replaced Flask 3.1.0 with Django 4.2.13
- Removed Flask-CORS → Added django-cors-headers
- Flask routes → Django URLs and Views
- Flask-style JSON → Django REST Framework serializers

## File Structure Overview

```
backend/
├── manage.py                 # Django management script
├── setup.py                  # Initial setup script
├── pytest.ini                # Pytest configuration
├── requirements.txt          # Production dependencies
├── requirements-dev.txt      # Development dependencies
├── config/                   # Django project settings
│   ├── settings.py          # Main Django configuration
│   ├── urls.py              # Main URL router
│   ├── wsgi.py              # WSGI application
│   └── __init__.py
├── api/                     # Django app with API logic
│   ├── models.py            # Database models (User, Doctor, Appointment)
│   ├── views.py             # API endpoints
│   ├── serializers.py       # Data serializers
│   ├── urls.py              # API URLs
│   ├── admin.py             # Django admin configuration
│   ├── apps.py              # App configuration
│   ├── migrations/          # Database migrations
│   │   ├── __init__.py
│   │   └── 0001_initial.py # Initial schema migration
│   ├── management/
│   │   └── commands/
│   │       └── load_initial_data.py # Command to load sample data
│   └── __init__.py
└── tests/                   # Test files
    ├── __init__.py
    ├── conftest.py          # Pytest configuration
    └── test_api.py          # API tests
```

## Installation & Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

### 2. Run Setup Script (Recommended)

This script runs migrations and loads initial data:

```bash
python setup.py
```

Alternatively, do it manually:

```bash
python manage.py migrate
python manage.py load_initial_data
```

### 3. Start the Server

```bash
python manage.py runserver
```

Server runs at: **http://127.0.0.1:8000/**

## API Endpoints

All endpoints return JSON:

| Method | Endpoint            | Description          |
| ------ | ------------------- | -------------------- |
| GET    | `/`                 | Health check         |
| POST   | `/login`            | User login           |
| GET    | `/doctors`          | Get all doctors      |
| GET    | `/appointments`     | Get all appointments |
| POST   | `/book-appointment` | Book new appointment |

### Example Requests

**Login:**

```bash
curl -X POST http://localhost:8000/login \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "admin123"}'
```

**Get Doctors:**

```bash
curl http://localhost:8000/doctors
```

**Book Appointment:**

```bash
curl -X POST http://localhost:8000/book-appointment \
  -H "Content-Type: application/json" \
  -d '{
    "patientName": "John Doe",
    "patientAge": 30,
    "doctorId": 1,
    "paymentMethod": "UPI",
    "upiId": "john@upi"
  }'
```

## Testing

Run all tests:

```bash
pytest
```

Run with verbose output:

```bash
pytest -v
```

Run specific test file:

```bash
pytest tests/test_api.py
```

## Linting

```bash
pylint api/
```

## Database & Admin Panel

### Create Admin User

```bash
python manage.py createsuperuser
```

### Access Admin Panel

1. Create a superuser (if not done already)
2. Visit: **http://127.0.0.1:8000/admin/**
3. Use your superuser credentials to login

### Reset Database

```bash
rm db.sqlite3
python manage.py migrate
python manage.py load_initial_data
```

## Environment Variables

Create a `.env` file (copy from `.env.example`):

```
DJANGO_DEBUG=true
DJANGO_SECRET_KEY=your-secret-key-here
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
CORS_ALLOWED_ORIGINS=http://localhost:5173,http://127.0.0.1:5173
```

## Key Differences from Flask

| Flask          | Django                            |
| -------------- | --------------------------------- |
| `flask run`    | `python manage.py runserver`      |
| `@app.route()` | URL patterns in `urls.py`         |
| `jsonify()`    | Django REST Framework serializers |
| `Flask-CORS`   | `django-cors-headers` middleware  |
| In-memory data | SQLite database with models       |
| No admin panel | Built-in Django admin             |

## Deployment with Gunicorn

```bash
gunicorn config.wsgi:application --bind 0.0.0.0:8000
```

The `Procfile` is already configured for Heroku deployment:

```
web: gunicorn config.wsgi:application
```

## Troubleshooting

**Port already in use:**

```bash
python manage.py runserver 8001
```

**Database locked:**

```bash
rm db.sqlite3
python manage.py migrate
python manage.py load_initial_data
```

**Import errors:**

```bash
python manage.py check
```

**Clear cache:**

```bash
find . -type d -name __pycache__ -exec rm -r {} +
find . -type f -name "*.pyc" -delete
```

## Next Steps

1. ✅ Install dependencies
2. ✅ Run setup script
3. ✅ Start development server
4. Test API endpoints
5. Access Django admin panel
6. Customize models and API logic as needed
