"""
Django admin configuration for Care Access Hospital Management System.
"""

from django.contrib import admin
from .models import User, Doctor, Appointment


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'role']
    search_fields = ['username']


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['name', 'specialization', 'availability', 'experience']
    search_fields = ['name', 'specialization']
    list_filter = ['availability', 'specialization']


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['patient_name', 'doctor', 'payment_status', 'appointment_status', 'created_at']
    search_fields = ['patient_name', 'doctor__name']
    list_filter = ['appointment_status', 'payment_status', 'created_at']
