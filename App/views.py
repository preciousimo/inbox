from django.shortcuts import render

# Fuction to home page (Frontend)
def home(request):
    return render(request, "home.html")

# Fuction to inbox (Backend)
def inbox(request):
    return render(request, "inbox.html")