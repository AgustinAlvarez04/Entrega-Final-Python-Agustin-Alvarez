from django import forms
from django.forms import ModelForm
from .models import *

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import datetime

class PerfilForm(forms.Form):
    nombre= forms.CharField(label="Nombre", max_length=60)
    apellido= forms.CharField(label="Apellido", max_length=60)
    edad= forms.IntegerField(label="Edad")
    email= forms.EmailField(label="Email")
    descripcion= forms.CharField(label="Descripcion", max_length=60)
    imagen= forms.ImageField(label="Imagen")
    

class MensajeForm(forms.Form):
    remitente= forms.CharField(label="Remitente", max_length=50)
    mensaje= forms.CharField(label="Mensaje", max_length=500)