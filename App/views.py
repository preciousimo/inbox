from django.shortcuts import render
from django.contrib.auth.decorators import login_required  # Login required to private pages
from django.views.decorators.cache import cache_control # Destroy the section after logout 
from .forms import Customerform, EmailForm # From forms.py
from .models import Customer # From models.py
from django.contrib import messages # Message from backend
from django.http import HttpResponseRedirect # Redirect  page
from django.db.models import Q # Global search
from django.core.paginator import Paginator # Pagination
from datetime import datetime # Used to get total message per day (In this case)
from django.core.mail import EmailMessage # Send emails
from django.contrib.auth import logout # Used to get auto logout

# Define a constant for the inbox URL
INBOX_URL = '/inbox'

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
    if 'q' in request.GET:
        q = request.GET['q']
        all_customer_list = Customer.objects.filter(
            Q(name__icontains=q) | Q(phone__icontains=q) |
            Q(email=q) | Q(subject__icontains=q) |
            Q(message__icontains=q) | Q(status__icontains=q)
        ).order_by('-created_at')
    else:
        all_customer_list = Customer.objects.all().order_by('-created_at')

    paginator = Paginator(all_customer_list, 5)
    page = request.GET.get('page')
    all_customer = paginator.get_page(page)

    # Total
    total = Customer.objects.all().count()
    # Read
    read = Customer.objects.filter(status='Read')
    # Unread
    pending = Customer.objects.filter(status='Pending')
    # Today
    base = datetime.now().date()
    today = Customer.objects.filter(created_at__gt = base)

    return render(request, "inbox.html", {'customers':all_customer,
    "total":total, "read":read, "pending":pending, "today":today})

# Function to delete the messages
@login_required(login_url="login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def delete_message(request, customer_id):
    customer = Customer.objects.get(id = customer_id)
    customer.delete()
    messages.success(request, "Message successfully deleted !")
    return HttpResponseRedirect(INBOX_URL)  # Use the constant here

# Function to view the message individually
@login_required(login_url="login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def customer(request, customer_id):
    customer = Customer.objects.get(id = customer_id)
    if customer != None:
        return render(request, "customer.html", {"customer":customer})

# Function to mark the message as read
@login_required(login_url="login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def mark_message(request):
    if request.method == "POST":
        customer = Customer.objects.get(id = request.POST.get('id'))
        if customer != None:
            customer.status = request.POST.get('status')
            customer.save()
            messages.success(request, "Message marked as READ !")
            return HttpResponseRedirect(INBOX_URL)  # Use the constant here

# Function to reply email
def email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST, request.FILES)

        company = "Reply Anxtraoil"

        if form.is_valid():
            subject = form.cleaned_data["subject"]
            message = form.cleaned_data["message"]
            email = form.cleaned_data["email"]
            cc = form.cleaned_data["cc"]
            files = request.FILES.getlist("attach")
            
            mail = EmailMessage(subject, message, company, [email], [cc])
            for f in files:
                mail.attach(f.name, f.read(), f.content_type)
            mail.send()
            
            messages.success(request, "Reply send successfully !")
            return HttpResponseRedirect('/inbox')

        else:
            form = EmailForm()
            return render(request, {'form':form})

# Auto Logout Function
def AutoLogoutUser(request):
    logout(request)
    request.User = None
    messages.info(request, ".") # Argument cannot be empty (It's because i put a dot)
    return HttpResponseRedirect('/')

# ERRORS
# Error 500
def error_500(request):
    return render(request, '500.html')

# Error 404
def error_404(request, exception):
    return render(request, '404.html')