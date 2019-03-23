from django import forms
from .models import ExerType, Exerlog

class TypeForm(forms.ModelForm):
    class Meta:
        model=ExerType
        fields='__all__'