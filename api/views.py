"""
API views for Care Access Hospital Management System.
"""

from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import User, Doctor, Appointment
from .serializers import UserSerializer, DoctorSerializer, AppointmentSerializer


@api_view(['GET'])
def health_check(request):
    """Health check endpoint."""
    return Response({"message": "Care Access backend is running"})


@api_view(['POST'])
def login(request):
    """User login endpoint."""
    data = request.data or {}
    username = data.get("username", "").strip()
    password = data.get("password", "").strip()

    try:
        user = User.objects.get(username=username, password=password)
        return Response({
            "success": True,
            "message": f"{user.role} login successful",
            "role": user.role,
        })
    except User.DoesNotExist:
        return Response(
            {"success": False, "message": "Invalid credentials"},
            status=status.HTTP_401_UNAUTHORIZED
        )


class DoctorViewSet(viewsets.ModelViewSet):
    """ViewSet for Doctor operations."""
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    http_method_names = ['get']


@api_view(['GET'])
def get_doctors(request):
    """Get all doctors."""
    doctors = Doctor.objects.all()
    serializer = DoctorSerializer(doctors, many=True)
    return Response({
        "success": True,
        "doctors": serializer.data
    })


@api_view(['GET'])
def get_appointments(request):
    """Get all appointments."""
    appointments = Appointment.objects.all()
    serializer = AppointmentSerializer(appointments, many=True)
    return Response({
        "success": True,
        "appointments": serializer.data
    })


@api_view(['POST'])
def book_appointment(request):
    """Book an appointment."""
    data = request.data or {}
    patient_name = data.get("patientName", "").strip()
    patient_age = data.get("patientAge", "")
    doctor_id = data.get("doctorId")
    payment_method = data.get("paymentMethod", "").strip()
    upi_id = data.get("upiId", "").strip()

    # Validation
    if not patient_name or not patient_age or doctor_id is None or not payment_method:
        return Response(
            {
                "success": False,
                "message": "Patient name, patient age, doctor, and payment method are required",
            },
            status=status.HTTP_400_BAD_REQUEST
        )

    try:
        patient_age_int = int(patient_age)
        if patient_age_int <= 0:
            raise ValueError()
    except (ValueError, TypeError):
        return Response(
            {"success": False, "message": "Enter a valid patient age"},
            status=status.HTTP_400_BAD_REQUEST
        )

    try:
        doctor = Doctor.objects.get(id=doctor_id)
    except Doctor.DoesNotExist:
        return Response(
            {"success": False, "message": "Doctor not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    if doctor.availability != "Available":
        return Response(
            {"success": False, "message": "Doctor is currently busy"},
            status=status.HTTP_400_BAD_REQUEST
        )

    if payment_method not in {"Cash", "UPI"}:
        return Response(
            {"success": False, "message": "Invalid payment method"},
            status=status.HTTP_400_BAD_REQUEST
        )

    if payment_method == "UPI" and not upi_id:
        return Response(
            {"success": False, "message": "UPI ID is required for UPI payment"},
            status=status.HTTP_400_BAD_REQUEST
        )

    # Create appointment
    appointment = Appointment.objects.create(
        patient_name=patient_name,
        patient_age=patient_age_int,
        doctor=doctor,
        payment_method=payment_method,
        payment_status="Paid",
        appointment_status="Confirmed",
        upi_id=upi_id if payment_method == "UPI" else "",
    )

    serializer = AppointmentSerializer(appointment)
    return Response(
        {
            "success": True,
            "message": f"Appointment booked for {patient_name} with {doctor.name} and payment marked as paid.",
            "appointment": serializer.data,
        },
        status=status.HTTP_200_OK
    )
