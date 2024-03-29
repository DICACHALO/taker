from django import forms
from django.forms.widgets import TextInput, Textarea

choices_priority = [('Alta','Alta'),('Media','Media'),('Baja','Baja')]
choices_cost = [('Alto','Alto'),('Medio','Medio'),('Bajo','Bajo')]
choices_state = [('Propuesta','Propuesta'),('Aprobado','Aprobado'),('En curso','En curso'),('Implementado','Implementado'),('Aplazado','Aplazado'),('Rechazado','Rechazado')]
choices_type = [('Requerimiento de producto','Requerimiento de producto'),('Requerimiento organizacional','Requerimiento organizacional'),('Requerimiento externo','Requerimiento externo')]

class NewFunctionalrequeriments(forms.Form):
    title = forms.CharField(widget=TextInput(
        attrs={'class': 'form-control'}))
    description = forms.CharField(label="description",required=True, widget=forms.Textarea(
        attrs={'class': 'form-control'}))
    comments = forms.CharField(label="description",required=True, widget=forms.Textarea(
        attrs={'class': 'form-control'}))

    priority = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}), choices=choices_priority)
    
    cost = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}), choices=choices_cost)

    state = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}), choices=choices_state)
    
    type_r = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}), choices=choices_type)  