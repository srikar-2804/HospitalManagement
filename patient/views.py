from django.shortcuts import render, redirect
from .models import Patient, Appointment
from .forms import PatientRegisterForm, PatientLoginForm, ProfileUpdateForm, AppointmentForm
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import TestReport
# Register View
def register(request):
    if request.method == 'POST':
        form = PatientRegisterForm(request.POST)
        if form.is_valid():
            patient = form.save(commit=False)
            patient.password = make_password(form.cleaned_data['password'])
            patient.save()
            messages.success(request, "Registration successful. Please log in.")
            return redirect('patient:patient-login')
    else:
        form = PatientRegisterForm()
    return render(request, 'patient/register.html', {'form': form})

# Login View
def login(request):
    if request.method == 'POST':
        form = PatientLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                patient = Patient.objects.get(email=email)
                if check_password(password, patient.password):
                    request.session['patient_id'] = patient.id  # Save patient in session
                    messages.success(request, "Login successful!")
                    return redirect('patient:patient-home')
                else:
                    messages.error(request, "Invalid email or password.")
            except Patient.DoesNotExist:
                messages.error(request, "Invalid email or password.")
    else:
        form = PatientLoginForm()
    return render(request, 'patient/login.html', {'form': form})

# Logout View
def logout(request):
    request.session.flush()
    messages.success(request, "Logged out successfully!")
    return redirect('patient:patient-login')

# Home Page
def patient_home(request):
    patient_id = request.session.get('patient_id')
    if not patient_id:
        return redirect('patient:patient-login')
    patient = Patient.objects.get(id=patient_id)
    return render(request, 'patient/home.html', {'patient': patient})

# Profile Update
def profile(request):
    patient_id = request.session.get('patient_id')
    if not patient_id:
        return redirect('patient:patient-login')
    patient = Patient.objects.get(id=patient_id)

    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect('patient:patient-home')
    else:
        form = ProfileUpdateForm(instance=patient)

    return render(request, 'patient/profile.html', {'form': form, 'patient': patient})


# Schedule Appointment
def schedule_appointment(request):
    patient_id = request.session.get('patient_id')
    if not patient_id:
        return redirect('patient:patient-login')
    patient = Patient.objects.get(id=patient_id)

    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.patient = patient
            appointment.save()
            messages.success(request, "Appointment booked successfully!")
            return redirect('patient:appointment-success')
    else:
        form = AppointmentForm()

    return render(request, 'patient/appointment.html', {'form': form, 'patient': patient})

def appointment_success(request):
    patient_id = request.session.get('patient_id')
    if not patient_id:
        return redirect('patient:patient-login')
    patient = Patient.objects.get(id=patient_id)
    return render(request, 'patient/appointment_success.html', {'patient': patient})

# def test_reports(request):
#     patient_id = request.session.get('patient_id')
#     patient_email=request.session.get('patient')
#     if not patient_id:
#         return redirect('patient:patient-login')
#     patient = Patient.objects.get(id=patient_id)
#     reports = TestReport.objects.filter(email=patient_email)
#     return render(request, 'patient/test_reports.html', {'reports': reports},{'patient': patient})
# def test_reports(request):
#     user = request.user
#     reports = TestReport.objects.filter(patient__email=user.email)
#     return render(request, 'patient/test_reports.html', {'reports': reports})
from django.shortcuts import render, redirect
from .models import Patient, TestReport

def test_reports(request):
    # Retrieve patient ID from the session
    patient_id = request.session.get('patient_id')
    if not patient_id:
        return redirect('patient:patient-login')  # Redirect if the patient is not logged in

    # Get the Patient object
    try:
        patient = Patient.objects.get(id=patient_id)
    except Patient.DoesNotExist:
        return redirect('patient:patient-login')  # Redirect if the patient does not exist

    # Query TestReport objects for the logged-in patient
    reports = TestReport.objects.filter(patient=patient)

    # Render the template with the reports and patient context
    return render(request, 'patient/test_reports.html', {'reports': reports, 'patient': patient})
