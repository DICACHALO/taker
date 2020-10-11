from django import forms
from .models import SRFFile, SRnFFile
from django.forms.widgets import ClearableFileInput

class SpecificRequeriment(forms.Form):
    input = forms.CharField(label="Entrada")
    output = forms.CharField(label="Salida")
    source = forms.CharField(label="Fuente")
    destination = forms.CharField(label="Destino")
    process = forms.CharField(label="Proceso", widget=forms.Textarea)
    restriction = forms.CharField(label="Restricciones")
    collateral_damage = forms.CharField(label="Daño Colateral")

class SpecificnFRequeriment(forms.Form):
    sub_type = forms.CharField(label="Sub-tipo")

class SpecificRequerimentFeed(forms.ModelForm):
    class Meta:
        model = SRFFile
        fields = ['file']
        widgets = {
            'file': ClearableFileInput(attrs={'multiple': True}),
        }

class NonSpecificRequerimentFeed(forms.ModelForm):
    class Meta:
        model = SRnFFile
        fields = ['file']
        widgets = {
            'file': ClearableFileInput(attrs={'multiple': True}),
        }

