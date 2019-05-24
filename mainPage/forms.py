from django import forms
from .models import *

class BackForm(forms.ModelForm):

    class Meta:
        model = Form
        exclude = ['']