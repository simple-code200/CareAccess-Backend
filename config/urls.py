"""URL Configuration for Care Access Hospital Management System."""

from django.urls import path, include

urlpatterns = [
    path('', include('api.urls')),
]
