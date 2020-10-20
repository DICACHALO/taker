from django import forms
from .models import SRFFile, SRnFFile
from django.forms.widgets import ClearableFileInput,TextInput, Textarea

class SpecificRequeriment(forms.Form):
    input = forms.CharField(label="Entrada", widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    output = forms.CharField(label="Salida", widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    source = forms.CharField(label="Fuente", widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    destination = forms.CharField(label="Destino", widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    process = forms.CharField(label="Proceso", widget=forms.Textarea(
        attrs={'class': 'form-control'}))
    restriction = forms.CharField(label="Restricciones", widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    collateral_damage = forms.CharField(label="Daño Colateral", widget=forms.TextInput(
        attrs={'class': 'form-control'}))

class SpecificnFRequeriment(forms.Form):
    sub_type = forms.CharField(label="Sub-tipo", widget=forms.TextInput(
        attrs={'class': 'form-control'}))

class SpecificRequerimentFeed(forms.ModelForm):
    class Meta:
        model = SRFFile
        fields = ['file']
        widgets = {
            'file': ClearableFileInput(attrs={'multiple': True, 'class':'form-control'}),
        }

class NonSpecificRequerimentFeed(forms.ModelForm):
    class Meta:
        model = SRnFFile
        fields = ['file']
        widgets = {
            'file': ClearableFileInput(attrs={'multiple': True, 'class':'form-control'}),
        }

