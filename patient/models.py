from django.db import models
from doctors.models import Doctor

class Patient(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    password = models.CharField(max_length=128)  # Password is hashed
    dob = models.DateField()

    def __str__(self):
        return self.name


class Appointment(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
    doctor = models.ForeignKey('doctors.Doctor', on_delete=models.CASCADE)
    issue = models.TextField()
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient.name} - {self.doctor.name} - {self.appointment_date}"


class TestReport(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE, related_name="reports")
    report_name = models.CharField(max_length=150, help_text="Title or name of the test report")
    report_image = models.ImageField(upload_to="test_reports/", help_text="Upload the report image")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.report_name} - {self.patient.name}"
