from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
 
class DiscoFormulario(forms.Form):
    nombre = forms.CharField()
    autor= forms.CharField()
    año = forms.IntegerField()
    precio = forms.IntegerField()
    
class Formulario(forms.Form):
    curso = forms.CharField()
    autor = forms.IntegerField()
    
class BuscarDiscoForm(forms.Form):
    album= forms.CharField()
    autor= forms.CharField()
    
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
 
class Meta:
    model = User
    fields = ['username', 'email', 'password1', 'password2']
        # Saca los mensajes de ayuda
    help_texts = {k:"" for k in fields}
   
class UserEditForm(UserCreationForm):

    # Obligatorios
    email = forms.EmailField(label="Ingrese su email:")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput, required=False)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput, required=False)

    last_name = forms.CharField(required=False)
    first_name = forms.CharField(required=False)
    imagen = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['email', 'last_name', 'first_name', 'password1', 'password2']    

