"""
URL routing for Care Access Hospital Management System API.
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.health_check, name='health-check'),
    path('login', views.login, name='login'),
    path('doctors', views.get_doctors, name='get-doctors'),
    path('appointments', views.get_appointments, name='get-appointments'),
    path('book-appointment', views.book_appointment, name='book-appointment'),
]
