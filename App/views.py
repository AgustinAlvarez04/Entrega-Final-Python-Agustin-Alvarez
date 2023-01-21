from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.urls import reverse_lazy
from App.forms import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import login, authenticate
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required #para vistas basadas en funciones
from django.contrib.auth.mixins import LoginRequiredMixin #para vistas basadas en clases


def obtenerAvatar(request):
    lista=Avatar.objects.filter(user=request.user)
    if len(lista)!=0:
        avatar=lista[0].imagen.url
    else:
        avatar="/media/avatars/images.png"
    return avatar

#------------------------- NAVBAR -----------------------------------#
def inicio(request):
    return render(request, "App/inicio.html")

def about(request):
    return render(request, 'App/about.html')

def contact(request):
    return render(request, 'App/contact.html')

def pages(request):
    return render(request, 'App/pages.html')

def busqueda(request):
    return render(request, 'App/busqueda.html')

def resultados(request):
    return render(request, 'App/resultados.html') 

#--------------------------------- CREACION DE USUARIOS --------------------------------------#

def register(request):
    if request.method=="POST":
        form= RegistroUsuarioForm(request.POST)
        if form.is_valid():
            username= form.cleaned_data.get("username")
            form.save()
            return render(request, "App/register.html", {"mensaje": f"Usuario {username} creado correctamente"})
        else:
            return render(request, "App/register.html", {"form": form, "mensaje":"Error al crear usuario"})
    else:
        form= RegistroUsuarioForm()
        return render (request, "App/register.html" , {"form":form})

def login_request(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usuario=info["username"]
            clave=info["password"]
            usuario=authenticate(username=usuario, password=clave)# verifica su el usuario existe
            if usuario is not None:
                login(request, usuario)
                return render(request, "App/inicio.html", {"mensaje":f"Usuario {usuario} logeuado correctamente"})
            else:
                return render(request, "App/login.html", {"form":form, "mensaje":"Usuario o contraseña incorrectos"})
        else:
            return render(request, "App/login.html", {"form":form, "mensaje":"Usuario o contraseña incorrectos"})
    else:    
        form= AuthenticationForm()
        return render(request, "App/login.html", {"form":form})

@login_required
def editarPerfil(request):
    usuario=request.user
    if request.method=="POST":
        form=UserEditForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usuario.email=info["email"]
            usuario.password1=info["password1"]
            usuario.password2=info["password2"]
            usuario.first_name=info["first_name"]
            usuario.last_name=info["last_name"]
            usuario.save()
            return render(request, "App/inicio.html", {"mensaje":f"Usuario {usuario} editado correctamente"})
        else:
            return render(request, "App/editarPerfil.html", {"form":form , "nombreusuario": usuario.username})    
    else:

        form=UserEditForm(instance=usuario)
        return render(request, "App/editarPerfil.html", {"form":form , "nombreusuario": usuario.username})