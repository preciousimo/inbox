from django import forms
from .models import Customer

class Customerform(forms.ModelForm):
    file = forms.FileField(required=False)
    class Meta:
        model = Customer
        fields = "__all__"