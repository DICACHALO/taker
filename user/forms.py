from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms.widgets import PasswordInput, TextInput


class Myform(AuthenticationForm):
    username = forms.CharField(widget=TextInput(
        attrs={'class': 'form-control form-control-user', 'placeholder': 'usuario@ejemplo.com',
        'type': 'email'}))

    password = forms.CharField(widget=PasswordInput(
        attrs={'class': 'form-control form-control-user',
               'placeholder': '********'}))


class Myformregistro(UserCreationForm):
    username = forms.CharField(widget=TextInput(
        attrs={'class': 'form-control form-control-user', 'placeholder': 'usuario@ejemplo.com',
        'type': 'email'}))

    password1 = forms.CharField(widget=PasswordInput(
        attrs={'class': 'form-control form-control-user',
               'placeholder': '********',
               'minlength': '8',
               'maxlength': '20'}))
    
    password2 = forms.CharField(widget=PasswordInput(
        attrs={'class': 'form-control form-control-user',
               'placeholder': '********',
               'minlength': '8',
               'maxlength': '20'}))
