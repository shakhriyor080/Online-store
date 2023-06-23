from django import forms 
from  .models import *

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['client_name',  'client_phone_number']