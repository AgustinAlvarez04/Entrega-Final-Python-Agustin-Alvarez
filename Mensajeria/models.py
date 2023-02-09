from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Perfil(models.Model):
    nombre=models.CharField(max_length=60)
    apellido=models.CharField(max_length=60)
    edad=models.IntegerField()
    email=models.EmailField()
    imagen= models.ImageField(upload_to="imagenes")
    def __str__(self):
        return f"{self.nombre} - {self.apellido}"

class Mensaje(models.Model):
    remitente=models.CharField(max_length=50)
    mensaje=RichTextField(max_length=500)
    def __str__(self):
        return f"{self.remitente}"

class Msjs(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    receptor = models.CharField(max_length=50)
    mensaje = models.TextField()
    leido = models.BooleanField(default=False)
    def __str__(self):
        return self.mensaje
    
class Descripcion(models.Model):
    descripcion = models.TextField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

class Url(models.Model):
    url = models.URLField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)