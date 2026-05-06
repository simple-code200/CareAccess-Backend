"""
Models for Care Access Hospital Management System.
"""

from django.db import models


class User(models.Model):
    """User model for authentication."""
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Doctor', 'Doctor'),
        ('Patient', 'Patient'),
    ]
    
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    
    def __str__(self):
        return f"{self.username} ({self.role})"


class Doctor(models.Model):
    """Doctor model for hospital staff."""
    AVAILABILITY_CHOICES = [
        ('Available', 'Available'),
        ('Busy', 'Busy'),
    ]
    
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    availability = models.CharField(max_length=20, choices=AVAILABILITY_CHOICES)
    experience = models.CharField(max_length=50)
    
    class Meta:
        ordering = ['id']
    
    def __str__(self):
        return f"Dr. {self.name} ({self.specialization})"


class Appointment(models.Model):
    """Appointment model for booking."""
    PAYMENT_METHOD_CHOICES = [
        ('Cash', 'Cash'),
        ('UPI', 'UPI'),
    ]
    
    PAYMENT_STATUS_CHOICES = [
        ('Paid', 'Paid'),
        ('Pending', 'Pending'),
    ]
    
    APPOINTMENT_STATUS_CHOICES = [
        ('Confirmed', 'Confirmed'),
        ('Booked', 'Booked'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]
    
    patient_name = models.CharField(max_length=100)
    patient_age = models.PositiveIntegerField()
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='appointments')
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES)
    appointment_status = models.CharField(max_length=20, choices=APPOINTMENT_STATUS_CHOICES)
    upi_id = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Appointment: {self.patient_name} with Dr. {self.doctor.name}"
