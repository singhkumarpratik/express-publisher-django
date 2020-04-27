from django import forms
from django.forms import ModelForm
from .models import *

class express_publishForm(forms.ModelForm):
    class Meta:
        model=express_publish
        fields='__all__'