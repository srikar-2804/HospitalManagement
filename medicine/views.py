from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.hashers import check_password  # To check the hashed password
from .models import Medicine, Order
from patient.models import Patient  # Importing the Patient model
from .forms import MedicineOrderForm, LoginForm
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from patient.forms import PatientLoginForm
# Patient Login View (Modified for Patient model)

def login(request):
    if request.method == 'POST':
        form = PatientLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            try:
                # Check if a patient with the given email exists
                patient = Patient.objects.get(email=email)
                # Validate password using check_password
                if check_password(password, patient.password):
                    # Save patient ID in session for authentication
                    request.session['patient_id'] = patient.id
                    messages.success(request, "Login successful!")
                    return redirect('medicines:medicine_order')  # Redirect to patient home page
                else:
                    messages.error(request, "Invalid email or password.")
            except Patient.DoesNotExist:
                messages.error(request, "Invalid email or password.")
        else:
            messages.error(request, "Invalid form input.")
    else:
        form = PatientLoginForm()

    return render(request, 'medicines/login.html', {'form': form})

from django.shortcuts import render
from patient.models import Patient

def medicine_order(request):
    # Get the logged-in patient's details
    patient = Patient.objects.get(id=request.session.get('patient_id'))

    # Fetch medicines or any other data needed
    medicines = Medicine.objects.all()  # or any filter you need for medicines

    return render(request, 'medicines/medicine_order.html', {
        'patient': patient,
        'medicines': medicines
    })

# Medicine Search via AJAX
def search_medicine(request):
    query = request.GET.get('q', '')
    medicines = Medicine.objects.filter(name__icontains=query)[:5]  # Return only the top 5 results

    results = [{
        'id': medicine.id,
        'name': medicine.name,
    } for medicine in medicines]

    return JsonResponse(results, safe=False)

# Medicine Details View
def medicine_detail_view(request, id):
    # Retrieve the medicine by its ID
    medicine = get_object_or_404(Medicine, id=id)

    # Pass the medicine to the template
    return render(request, 'medicines/medicine_detail.html', {'medicine': medicine})

# Logout View
def logout_view(request):
    logout(request)
    
    return redirect('medicines:login')


# views.py in the medicines app

from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import MedicineOrder, Medicine

from django.http import JsonResponse

def submit_order(request):
    if request.method == 'POST':
        # Process the cart data here
        try:
            cart = json.loads(request.body.decode('utf-8'))['cart']
            # Process the cart and create the order
            # Example: Save the order to the database

            # Return success response
            return JsonResponse({'status': 'success', 'message': 'Order submitted successfully!'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})