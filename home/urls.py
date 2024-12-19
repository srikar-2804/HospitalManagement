from django.urls import path
from .views import home,patientinfo,about,locations,feedback_view
app_name='home'
urlpatterns = [
    path('',home,name='home'),
    path('patient-info',patientinfo,name='patientinfo'),
    path('about/',about,name='about'),
    path('location/',locations,name='location'),
    path('feedback/', feedback_view, name='feedback'),
]
