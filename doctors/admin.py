from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Doctor

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialist_in', 'years_experience', 'email', 'phone')
    search_fields = ('name', 'specialist_in')
