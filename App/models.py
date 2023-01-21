from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Avatar(models.Model):
    imagen= models.ImageField(upload_to="avatars")
    user= models.ForeignKey(User, on_delete=models.CASCADE)



class Blogs(models.Model):
    autor = models.CharField(max_length=50)
    titulo = models.CharField(max_length=50)