from django import forms
from .models import *


class InputForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    jsonb = forms.CharField()

    class Meta:
        model = Value
        fields = ('name','jsonb')