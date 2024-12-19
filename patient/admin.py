from django.contrib import admin
from .models import Appointment

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'issue', 'appointment_date', 'appointment_time', 'created_at')
    list_filter = ('appointment_date', 'doctor')  # Optional filters to quickly find appointments
    search_fields = ('patient__name', 'doctor__name', 'issue')  # Allows searching by patient name, doctor name, and issue
    ordering = ('appointment_date', 'appointment_time')  # Orders the appointments by date and time

    # Optionally, you can also add custom methods to display additional details.
    def patient_name(self, obj):
        return obj.patient.name

    def doctor_name(self, obj):
        return obj.doctor.name

    patient_name.admin_order_field = 'patient__name'  # Allows sorting by patient name
    doctor_name.admin_order_field = 'doctor__name'    # Allows sorting by doctor name

    # Add those fields to the list_display if needed
    list_display = ('patient_name', 'doctor_name', 'issue', 'appointment_date', 'appointment_time', 'created_at')

# Register the Appointment model with the custom admin interface
admin.site.register(Appointment, AppointmentAdmin)
from django.contrib import admin
from .models import Patient, Appointment, TestReport

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')


@admin.register(TestReport)
class TestReportAdmin(admin.ModelAdmin):
    list_display = ('report_name', 'patient', 'uploaded_at')
    list_filter = ('uploaded_at',)
    search_fields = ('report_name', 'patient__name', 'patient__email')
