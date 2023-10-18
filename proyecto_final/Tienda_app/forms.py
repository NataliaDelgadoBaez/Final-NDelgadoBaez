from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
 
class Crearalbumform(forms.Form):
    usuario = forms.CharField(max_length=40)
    album = forms.CharField()
    artista= forms.CharField()
    año = forms.IntegerField()
    precio = forms.IntegerField()
    contacto = forms.IntegerField()
    
class Buscaralbumform(forms.Form):
    album= forms.CharField()
    artista= forms.CharField()
    
    
class Mostraralbumform(forms.Form):
    nombre= forms.CharField()
    artista= forms.CharField()
    
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
 
class Meta:
    model = User
    fields = ['username', 'email', 'password1', 'password2']
        # Saca los mensajes de ayuda
    help_texts = {k:"" for k in fields}
   
    

