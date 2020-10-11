from django import forms
from .models import Project
from django.forms.widgets import TextInput, Textarea

TYPE_USER_CHOICES = [('Gerente', 'Gerente'), ('Analista', 'Analista'), ('Cliente', 'Cliente'), ('Programador', 'Programador')]

    
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control'}),
        }
    
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget = forms.Textarea(attrs={'class': 'form-control'})
        
        

class NewMember(forms.Form):
    user = forms.CharField(widget=TextInput(
        attrs={'class': 'form-control form-control-user', 'placeholder': 'usuario@ejemplo.com',
        'type': 'email'}))
    type_user = forms.ChoiceField(widget=forms.RadioSelect(attrs={'class':'form-check-input'}), choices=TYPE_USER_CHOICES)

    #type_user = forms.CharField(label="type_user",required=True, help_text="Tipo de Usuario")
        
