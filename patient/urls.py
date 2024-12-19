from django.urls import path
from . import views

app_name = 'patient'

urlpatterns = [
    path('register/', views.register, name='patient-register'),
    path('login/', views.login, name='patient-login'),
    path('home/', views.patient_home, name='patient-home'),
    path('profile/', views.profile, name='patient-profile'),
    path('schedule-appointment/', views.schedule_appointment, name='patient-appointment'),
    path('appointment-success/', views.appointment_success, name='appointment-success'),
    path('logout/', views.logout, name='patient-logout'),
     path('test-reports/', views.test_reports, name="test-reports"),
]
