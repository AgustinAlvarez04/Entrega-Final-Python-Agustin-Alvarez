from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.

class Avatar(models.Model):
    imagen= models.ImageField(upload_to="avatars")
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.user}"

class Blog(models.Model):
    titulo= models.CharField(max_length=60)
    subtitulo= models.CharField(max_length=70)
    imagen= models.ImageField(upload_to="imagenes")
    cuerpo= RichTextField(max_length=3000)
    autor= models.CharField(max_length=30)
    fecha= models.CharField(max_length=30)
    def __str__(self):
        return f"{self.titulo} - {self.autor}"

class Perfil(models.Model):
    nombre=models.CharField(max_length=60)
    apellido=models.CharField(max_length=60)
    edad=models.IntegerField()
    email=models.EmailField()
    descripcion=models.CharField(max_length=60)
    imagen= models.ImageField(upload_to="imagenes")
    def __str__(self):
        return f"{self.nombre} - {self.apellido}"

