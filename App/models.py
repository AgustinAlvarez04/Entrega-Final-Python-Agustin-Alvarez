from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.

class Avatar(models.Model):
    imagen= models.ImageField(upload_to="avatars")
    user= models.ForeignKey(User, on_delete=models.CASCADE)

class Blogs(models.Model):
    titulo = models.CharField(max_length=50)
    subtitulo= models.CharField(max_length=50)
    cuerpo = RichTextField(max_length=250)
    autor = models.CharField(max_length=50)
    fecha = models.CharField(max_length=50)
    imagen= models.ImageField(upload_to="media")

