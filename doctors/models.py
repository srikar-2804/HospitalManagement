from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialist_in = models.CharField(max_length=100)  # Example: "Cardiology"
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    date_of_joining = models.DateField()
    years_experience = models.PositiveIntegerField()
    study = models.TextField()  # Example: "MBBS, MD"
    image = models.ImageField(upload_to='doctors/images/')

    def __str__(self):
        return self.name
