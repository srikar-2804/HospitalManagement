from django.shortcuts import render,redirect
from .forms import FeedbackForm,Feedback
from doctors.models import Doctor
from django.contrib import messages

def home(request):
    # Fetch the first 4 doctors
    doctors = Doctor.objects.all()[:4]
    return render(request, 'home/home.html', {'doctors': doctors})

def patientinfo(request):
    feedbacks = Feedback.objects.all().order_by('-created_at')[:5]
    return render(request, 'home/patienthome.html', {'feedbacks': feedbacks})

def about(request):
    return render(request,'home/about.html')

def locations(request):
    return render(request,'home/location.html')

def feedback_view(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you for your feedback!")
            return redirect('home:feedback')
    else:
        form = FeedbackForm()
    
    feedbacks = Feedback.objects.all().order_by('-created_at')[:5]  # Show recent 5 feedbacks
    return render(request, 'home/feedback.html', {'form': form, 'feedbacks': feedbacks})