from django import forms
from django.forms import ModelForm
from .models import *
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

class express_publishForm(forms.ModelForm):
    class Meta:
        model=express_publish
        fields=['title','author','body']
        widgets = {
            'body': SummernoteWidget(),
        }
    def __init__(self, *args, **kwargs):
        super(express_publishForm, self).__init__(*args, **kwargs)
        self.visible_fields()[0].field.widget.attrs['class'] = 'input'
        self.visible_fields()[1].field.widget.attrs['class'] = 'input'
        self.visible_fields()[0].field.widget.attrs['placeholder'] = 'Enter Title'
        self.visible_fields()[1].field.widget.attrs['placeholder'] = 'Enter Your Name'
        self.visible_fields()[0].field.widget.attrs['style'] = 'margin-bottom:0.5em;'
        self.visible_fields()[1].field.widget.attrs['style'] = 'margin-bottom:0.5em;'
