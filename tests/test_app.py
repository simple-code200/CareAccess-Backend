import sys
from pathlib import Path

import pytest

# Add parent directory to path so we can import app
sys.path.insert(0, str(Path(__file__).parent.parent))

from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_health_check(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json == {"message": "Care Access backend is running"}


def test_login_success(client):
    response = client.post(
        "/login",
        json={"username": "admin", "password": "admin123"},
    )
    assert response.status_code == 200
    assert response.json["success"] is True
    assert response.json["role"] == "Admin"


def test_login_failure(client):
    response = client.post(
        "/login",
        json={"username": "wrong", "password": "wrong"},
    )
    assert response.status_code == 401
    assert response.json["success"] is False


def test_get_doctors(client):
    response = client.get("/doctors")
    assert response.status_code == 200
    assert response.json["success"] is True
    assert isinstance(response.json["doctors"], list)
    assert len(response.json["doctors"]) > 0


def test_get_appointments(client):
    response = client.get("/appointments")
    assert response.status_code == 200
    assert response.json["success"] is True
    assert isinstance(response.json["appointments"], list)


def test_book_appointment_success(client):
    response = client.post(
        "/book-appointment",
        json={
            "patientName": "Test Patient",
            "patientAge": "30",
            "doctorId": 1,
            "paymentMethod": "Cash",
            "upiId": "",
        },
    )
    assert response.status_code == 200
    assert response.json["success"] is True
    assert response.json["appointment"]["patientName"] == "Test Patient"
