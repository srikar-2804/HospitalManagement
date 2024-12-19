from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Order, Medicine

# User registration form
class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# Medicine Order form
class MedicineOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['medicine', 'quantity']

# Login form (using Django’s built-in Authentication Form)
class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
