from django import forms
#from .models import project

class Mensajeform(forms.Form):

    mensaje = forms.CharField(label="msj",required=True, help_text="Type message..", widget=forms.Textarea)

class PreChatform(forms.Form):

    nombre = forms.CharField(label="Nombre")
    email = forms.CharField(label="Correo")
    problema = forms.CharField(label="Problema", widget=forms.Textarea)