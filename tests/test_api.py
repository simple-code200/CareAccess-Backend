"""
Tests for the Care Access Hospital Management System API.
"""

import pytest
from django.test import Client
from api.models import User, Doctor, Appointment


@pytest.fixture
def setup_data(db):
    """Set up test data."""
    # Create users
    User.objects.create(username="admin", password="admin123", role="Admin")
    User.objects.create(username="doctor1", password="doc123", role="Doctor")
    User.objects.create(username="patient1", password="pat123", role="Patient")

    # Create doctors
    doctor1 = Doctor.objects.create(
        name="Dr. Aanya Sharma",
        specialization="Cardiology",
        availability="Available",
        experience="11 years",
    )
    
    # Create appointments
    Appointment.objects.create(
        patient_name="Aarav Patel",
        patient_age=34,
        doctor=doctor1,
        payment_method="UPI",
        payment_status="Paid",
        appointment_status="Confirmed",
        upi_id="aarav@upi",
    )

    return {
        "doctor": doctor1,
    }


@pytest.mark.django_db
def test_health_check():
    """Test health check endpoint."""
    client = Client()
    response = client.get('/')
    assert response.status_code == 200
    assert response.json()["message"] == "Care Access backend is running"


@pytest.mark.django_db
def test_login_success(setup_data):
    """Test successful login."""
    client = Client()
    response = client.post(
        '/login',
        data='{"username": "admin", "password": "admin123"}',
        content_type='application/json'
    )
    assert response.status_code == 200
    data = response.json()
    assert data["success"] is True
    assert data["role"] == "Admin"


@pytest.mark.django_db
def test_login_failure():
    """Test failed login."""
    client = Client()
    response = client.post(
        '/login',
        data='{"username": "wrong", "password": "wrong"}',
        content_type='application/json'
    )
    assert response.status_code == 401
    data = response.json()
    assert data["success"] is False


@pytest.mark.django_db
def test_get_doctors(setup_data):
    """Test get doctors endpoint."""
    client = Client()
    response = client.get('/doctors')
    assert response.status_code == 200
    data = response.json()
    assert data["success"] is True
    assert isinstance(data["doctors"], list)
    assert len(data["doctors"]) > 0


@pytest.mark.django_db
def test_get_appointments(setup_data):
    """Test get appointments endpoint."""
    client = Client()
    response = client.get('/appointments')
    assert response.status_code == 200
    data = response.json()
    assert data["success"] is True
    assert isinstance(data["appointments"], list)


@pytest.mark.django_db
def test_book_appointment_success(setup_data):
    """Test successful appointment booking."""
    client = Client()
    response = client.post(
        '/book-appointment',
        data='{"patientName": "Test Patient", "patientAge": "30", "doctorId": ' + str(setup_data["doctor"].id) + ', "paymentMethod": "Cash", "upiId": ""}',
        content_type='application/json'
    )
    assert response.status_code == 200
    data = response.json()
    assert data["success"] is True
    assert data["appointment"]["patient_name"] == "Test Patient"
