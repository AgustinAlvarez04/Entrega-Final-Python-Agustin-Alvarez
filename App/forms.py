from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import datetime

class AvatarForm(forms.Form):
    imagen=forms.ImageField(label="Imagen")
    
class RegistroUsuarioForm(UserCreationForm):
    
    email= forms.EmailField(label="Email")
    password1= forms.CharField(label="Cotraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Confirmar Cotraseña", widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=["username","email", "password1", "password2"]
        help_texts= {k:"" for k in fields}

class UserEditForm(UserCreationForm):
    
    email= forms.EmailField(label="Email")
    password1= forms.CharField(label="Cotraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Confirmar Cotraseña", widget=forms.PasswordInput)
    first_name= forms.CharField(label="Modificar nombre")
    last_name= forms.CharField(label="Modificar apellido")

    class Meta:
        model=User
        fields=["email", "password1", "password2", "first_name", "last_name"]
        help_texts= {k:"" for k in fields}



class BlogForm(forms.Form):
    titulo= forms.CharField(label="Titulo", max_length=50)
    subtitulo= forms.CharField(label="Subtitulo", max_length=50)
    cuerpo= forms.CharField(label="Cuerpo", max_length=50)
    autor= forms.CharField(label="Autor", max_length=50)










