from django.shortcuts import render
from django.contrib.auth.decorators import login_required  # Login required to private pages
from django.views.decorators.cache import cache_control # Destroy the section after logout
from .forms import Customerform # From forms.py
from .models import Customer # From models.py
from django.contrib import messages # Message from backend
from django.http import HttpResponseRedirect # Redirect  page

# FRONTEND
# Fuction to home page (Frontend)
def home(request):
    return render(request, "home.html")

# Function to send a message
def send_message(request):
    if request.method == "POST":
        form = Customerform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Message sent successfully !")
        return HttpResponseRedirect('/')
    else:
        form = Customerform()
    return render(request, "home.html", {'form':form})

# BACKEND
# Fuction to inbox (Backend)
@login_required(login_url="login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def inbox(request):
    return render(request, "inbox.html")