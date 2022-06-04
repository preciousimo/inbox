from django.shortcuts import render
# Login required to private pages
from django.contrib.auth.decorators import login_required
# Destroy the section after logout
from django.views.decorators.cache import cache_control

# Fuction to home page (Frontend)
def home(request):
    return render(request, "home.html")

# Fuction to inbox (Backend)
@login_required(login_url="login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def inbox(request):
    return render(request, "inbox.html")