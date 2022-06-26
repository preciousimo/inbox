from django.db import models
from django.utils.html import format_html
# Create your models here.
class Customer(models.Model):

    STATUS = (
        ('Pending', 'Pending'),
        ('Read', 'Read'),
    )

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    phone = models.CharField(max_length=30)
    email = models.CharField(max_length=40)
    subject = models.CharField(max_length=25)
    message = models.TextField(max_length=1000)
    file = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS)

    # Control Read/Unread messages on admin.py
    def situation(self):
        if self.status == 'Read':
            return format_html('<span style="color: black">{0}</span>', self.status)
        else:
            return format_html('<span style="color: red">{0}</span>', self.status)
    situation.allow_tags = True

    def __str__(self):
        return self.name
    