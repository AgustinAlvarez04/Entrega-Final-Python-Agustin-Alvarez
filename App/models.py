from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
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
    cuerpo= RichTextUploadingField()
    autor= models.CharField(max_length=30)
    fecha= models.DateField()
    def __str__(self):
        return f"{self.titulo} - {self.autor}"


