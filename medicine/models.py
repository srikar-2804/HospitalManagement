from django.db import models
from django.contrib.auth.models import User
from patient.models import Patient
# Patient Model (extends the User model for simplicity)
# class Patient(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     phone_number = models.CharField(max_length=15)

#     def __str__(self):
#         return self.user.username

# Medicine Model
class Medicine(models.Model):
    name = models.CharField(max_length=100,blank=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2)  # Medicine cost
    brand = models.CharField(max_length=100)  # Medicine brand
    cure_for = models.TextField()  # Description of what it cures
    image = models.ImageField(upload_to='medicine_images/', null=True, blank=True)  # Image field

    def __str__(self):
        return self.name

# Order Model (medicine order with quantity and associated patient)
class Order(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    ordered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order by {self.patient.user.username} for {self.medicine.name}"

class MedicineOrder(models.Model):
    patient = models.ForeignKey('patient.Patient', on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order by {self.patient.name} for {self.medicine.name}"
