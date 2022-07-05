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
]