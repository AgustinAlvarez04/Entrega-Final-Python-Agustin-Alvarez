from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.

class Perfil(models.Model):
    nombre=models.CharField(max_length=60)
    apellido=models.CharField(max_length=60)
    edad=models.IntegerField()
    email=models.EmailField()
    descripcion= RichTextField(max_length=1000)
    imagen= models.ImageField(upload_to="imagenes")
    def __str__(self):
        return f"{self.nombre} - {self.apellido}"

class Mensaje(models.Model):
    remitente=models.CharField(max_length=50)
    mensaje=RichTextField(max_length=500)
    def __str__(self):
        return f"{self.remitente}"