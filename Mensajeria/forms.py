from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.models import User
from datetime import datetime

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import datetime

class PerfilForm(forms.Form):
    nombre= forms.CharField(label="Nombre", max_length=60)
    apellido= forms.CharField(label="Apellido", max_length=60)
    edad= forms.IntegerField(label="Edad")
    email= forms.EmailField(label="Email")
    imagen= forms.ImageField(label="Imagen")
    
class MsjForm(forms.Form):
    receptor = forms.ChoiceField(label='Receptor', choices=[(user.username, user.username) for user in User.objects.all()],)    
    mensaje = forms.CharField(label="cuerpo", widget=forms.Textarea,)

class Formulario_url(forms.Form):
    url = forms.URLField(label='URL', max_length=200)
    def __str__(self):
        return self.url

class Formulario_descripcion(forms.Form):
    descripcion = forms.CharField(label='Descripcion', max_length=200, widget=forms.Textarea)