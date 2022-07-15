# from email import message
from django import forms
from .models import Customer

class Customerform(forms.ModelForm):
    file = forms.FileField(required=False)
    class Meta:
        model = Customer
        fields = "__all__"

# Reply emails
class EmailForm(forms.Form):
    email = forms.EmailField()
    cc = forms.EmailField(required=False)
    subject = forms.CharField(max_length=100)
    attach = forms.FileField(required=False, widget=forms.ClearableFileInput(attrs={'multiple': True}))
    message = forms.CharField(widget=forms.Textarea)