"""
Serializers for Care Access Hospital Management System.
"""

from rest_framework import serializers
from .models import User, Doctor, Appointment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'role']


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'name', 'specialization', 'availability', 'experience']


class AppointmentSerializer(serializers.ModelSerializer):
    doctor_name = serializers.CharField(source='doctor.name', read_only=True)
    specialization = serializers.CharField(source='doctor.specialization', read_only=True)
    
    class Meta:
        model = Appointment
        fields = [
            'id',
            'patient_name',
            'patient_age',
            'doctor',
            'doctor_name',
            'specialization',
            'payment_method',
            'payment_status',
            'appointment_status',
            'upi_id',
            'created_at',
        ]
        read_only_fields = ['id', 'created_at', 'doctor_name', 'specialization']
