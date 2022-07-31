from django.urls import path, include
from . import views

urlpatterns = [
    # FRONTEND
    # Path to home page (frontend)
    path('', views.home, name="home"),
    # Path to send the message
    path('send_message', views.send_message, name="send_message"),

    # BACKEND
    # Path to inbox page (backend)
    path('inbox/', views.inbox, name="inbox"),
    # Path to delete the message
    path('delete_message/<str:customer_id>', views.delete_message, name="delete_message"),
    # Path to view the message individually
    path('customer/<str:customer_id>', views.customer, name="customer"),
    # Path to mark the message as read
    path('mark_message/', views.mark_message, name="mark_message"),
    # Path to reply email
    path('email/', views.email, name="email"),
    # Path to auto logout
    path('autologout/', views.AutoLogoutUser, name="AutoLogoutUser"),
]