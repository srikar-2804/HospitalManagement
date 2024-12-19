from django.shortcuts import render
from .models import Doctor

def doctors_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctors/doctors_list.html', {'doctors': doctors})
