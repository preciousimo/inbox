from django import forms
from .models import Customer

class MultipleClearableFileInput(forms.FileInput):
    def __init__(self, attrs=None, **kwargs):
        super().__init__(attrs, **kwargs)
        self.attrs['multiple'] = True

class Customerform(forms.ModelForm):
    file = forms.FileField(required=False)
    class Meta:
        model = Customer
        fields = "__all__"

class EmailForm(forms.Form):
    email = forms.EmailField()
    cc = forms.EmailField(required=False)
    subject = forms.CharField(max_length=100)
    attach = forms.FileField(
        required=False,
        widget=MultipleClearableFileInput()
    )
    message = forms.CharField(widget=forms.Textarea)