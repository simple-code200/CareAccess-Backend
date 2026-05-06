"""
Management command to load initial data into the database.
"""

from django.core.management.base import BaseCommand
from api.models import User, Doctor, Appointment


class Command(BaseCommand):
    help = 'Load initial data for the hospital management system'

    def handle(self, *args, **options):
        # Clear existing data
        User.objects.all().delete()
        Doctor.objects.all().delete()
        Appointment.objects.all().delete()

        # Create users
        users_data = [
            {"username": "admin", "password": "admin123", "role": "Admin"},
            {"username": "doctor1", "password": "doc123", "role": "Doctor"},
            {"username": "patient1", "password": "pat123", "role": "Patient"},
        ]
        for user_data in users_data:
            User.objects.create(**user_data)
        self.stdout.write(self.style.SUCCESS(f"Created {len(users_data)} users"))

        # Create doctors
        doctors_data = [
            {
                "name": "Dr. Aanya Sharma",
                "specialization": "Cardiology",
                "availability": "Available",
                "experience": "11 years",
            },
            {
                "name": "Dr. Rohan Mehta",
                "specialization": "Dermatology",
                "availability": "Busy",
                "experience": "9 years",
            },
            {
                "name": "Dr. Priya Nair",
                "specialization": "Neurology",
                "availability": "Available",
                "experience": "14 years",
            },
            {
                "name": "Dr. Arjun Kapoor",
                "specialization": "Orthopedics",
                "availability": "Busy",
                "experience": "8 years",
            },
            {
                "name": "Dr. Sneha Reddy",
                "specialization": "Pediatrics",
                "availability": "Available",
                "experience": "10 years",
            },
            {
                "name": "Dr. Vikram Iyer",
                "specialization": "General Medicine",
                "availability": "Available",
                "experience": "13 years",
            },
            {
                "name": "Dr. Kavya Rao",
                "specialization": "Gynecology",
                "availability": "Busy",
                "experience": "12 years",
            },
            {
                "name": "Dr. Siddharth Bose",
                "specialization": "ENT",
                "availability": "Available",
                "experience": "7 years",
            },
            {
                "name": "Dr. Neha Verma",
                "specialization": "Psychiatry",
                "availability": "Busy",
                "experience": "15 years",
            },
            {
                "name": "Dr. Aditya Singh",
                "specialization": "Pulmonology",
                "availability": "Available",
                "experience": "9 years",
            },
            {
                "name": "Dr. Ishita Das",
                "specialization": "Ophthalmology",
                "availability": "Available",
                "experience": "6 years",
            },
            {
                "name": "Dr. Karan Malhotra",
                "specialization": "Urology",
                "availability": "Busy",
                "experience": "10 years",
            },
            {
                "name": "Dr. Meera Joshi",
                "specialization": "Endocrinology",
                "availability": "Available",
                "experience": "16 years",
            },
            {
                "name": "Dr. Rahul Chawla",
                "specialization": "Oncology",
                "availability": "Busy",
                "experience": "18 years",
            },
            {
                "name": "Dr. Tanvi Kulkarni",
                "specialization": "Radiology",
                "availability": "Available",
                "experience": "8 years",
            },
            {
                "name": "Dr. Aman Gupta",
                "specialization": "Gastroenterology",
                "availability": "Available",
                "experience": "12 years",
            },
            {
                "name": "Dr. Pooja Menon",
                "specialization": "Nephrology",
                "availability": "Busy",
                "experience": "11 years",
            },
            {
                "name": "Dr. Yash Patil",
                "specialization": "Physiotherapy",
                "availability": "Available",
                "experience": "5 years",
            },
            {
                "name": "Dr. Ritu Bansal",
                "specialization": "Dental Surgery",
                "availability": "Available",
                "experience": "9 years",
            },
            {
                "name": "Dr. Nikhil Arora",
                "specialization": "Hepatology",
                "availability": "Busy",
                "experience": "13 years",
            },
        ]
        for doctor_data in doctors_data:
            Doctor.objects.create(**doctor_data)
        self.stdout.write(self.style.SUCCESS(f"Created {len(doctors_data)} doctors"))

        # Create sample appointments
        doctors = Doctor.objects.all()
        appointments_data = [
            {
                "patient_name": "Aarav Patel",
                "patient_age": 34,
                "doctor": doctors[0],
                "payment_method": "UPI",
                "payment_status": "Paid",
                "appointment_status": "Confirmed",
                "upi_id": "aarav@upi",
            },
            {
                "patient_name": "Diya Thomas",
                "patient_age": 27,
                "doctor": doctors[4],
                "payment_method": "Cash",
                "payment_status": "Paid",
                "appointment_status": "Booked",
                "upi_id": "",
            },
            {
                "patient_name": "Manoj Kumar",
                "patient_age": 51,
                "doctor": doctors[12],
                "payment_method": "UPI",
                "payment_status": "Paid",
                "appointment_status": "Completed",
                "upi_id": "manojk@okaxis",
            },
        ]
        for appt_data in appointments_data:
            Appointment.objects.create(**appt_data)
        self.stdout.write(self.style.SUCCESS(f"Created {len(appointments_data)} appointments"))

        self.stdout.write(
            self.style.SUCCESS("Successfully loaded initial data")
        )
