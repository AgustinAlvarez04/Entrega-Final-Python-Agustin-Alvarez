from django.shortcuts import render
from .models import *
from App.models import *
from django.http import HttpResponse
from django.urls import reverse_lazy
from Mensajeria.forms import *
from App.forms import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import login, authenticate
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required #para vistas basadas en funciones
from django.contrib.auth.mixins import LoginRequiredMixin #para vistas basadas en clases

@login_required
def agregarAvatar(request):
    if request.method=="POST":
        form=AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            avatar=Avatar(user=request.user, imagen=request.FILES["imagen"])
            avatarViejo=Avatar.objects.filter(user=request.user)
            if len(avatarViejo)>0:
                avatarViejo[0].delete()
            avatar.save()
            return render(request , "Mensajeria/perfil.html", {"avatar":avatar, "mensaje": "Avatar subido correctamente"})
        else:
            return render(request , "App/agregarAvatar.html", {"form":form, "usuario":request.user, "mensaje":"Error al subir imagen"})
    else:
        form=AvatarForm
        return render(request , "App/agregarAvatar.html", {"form":form, "usuario":request.user})
@login_required
def obtenerAvatar(request):
    lista=Avatar.objects.filter(user=request.user)
    if len(lista)!=0:
        avatar=lista[0].imagen.url
    else:
        avatar="/media/avatars/homero.png"
    return avatar

@login_required
def perfil(request):
    perfil=Perfil.objects.all()
    return render(request, "Mensajeria/perfil.html", {"perfil": perfil, "avatar": obtenerAvatar(request)})
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
            return render(request, "Mensajeria/perfil.html", {"mensaje" : f"Usuario {usuario.username} editado correctamente"})
        else:
            return render(request, "Mensajeria/editarPerfil.html", {"form":form , "nombreusuario": usuario.username})    
    else:
        form=UserEditForm(instance=usuario)
        return render(request, "Mensajeria/editarPerfil.html", {"form":form , "nombreusuario": usuario.username})

@login_required
def msj(request):
    if request.method=="POST":
        form= MensajeForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            remitente=informacion['remitente']
            mensaje=informacion['mensaje']
            mensajes=Mensaje(remitente=remitente, mensaje=mensaje)
            mensajes.save()
            return render(request, "Mensajeria/msj.html", {"mensaje":"Mensaje enviado"})
        else:
            return render(request, "Mensajeria/msj.html", {"mensaje":"Informacion no valida"})
    else:
        formulario=MensajeForm()
        return render(request, "Mensajeria/msj.html", {"form":formulario})
@login_required
def buscarRemitente(request):
    return render(request, "Mensajeria/buscarRemitente.html")
@login_required
def busqueda(request):
    remitente=request.GET['remitente']
    if remitente!="":
        mensaje=Mensaje.objects.filter(remitente__icontains=remitente)
        return render(request, "Mensajeria/resultadosRemitente.html", {"mensaje":mensaje})
    else:
        return render(request, "Mensajeria/buscarRemitente.html", {"mensaje":"Ingresa un titulo para buscar!"})
@login_required
def resultadosRemitente(request):
    return render(request, 'Mensajeria/resultadosRemitente.html')  
@login_required
def leerMensajes(request):
    return render(request, "Mensajeria/leerMensajes.html")
@login_required
def agregarInformacion(request):
    if request.method=="POST":
        form= PerfilForm(request.POST, request.FILES)
        if form.is_valid():
            informacion=form.cleaned_data
            nombre=informacion["nombre"]
            apellido=informacion["apellido"]
            edad=informacion["edad"]
            email=informacion["email"]
            imagen=informacion["imagen"]
            perfil=Perfil(nombre=nombre, apellido=apellido, edad=edad, email=email, imagen=imagen)
            perfil.save()
            return render(request, "Mensajeria/perfil.html", {"mensaje":"Informacion agregada correctamente"})
        else:
            return render(request, "Mensajeria/agregarInformacion.html", {"mensaje":"Informacion no valida"})
    else:
        formulario=PerfilForm()
        return render(request, "Mensajeria/agregarInformacion.html", {"form":formulario})
@login_required
def leerInformacion(request):
    perfil= Perfil.objects.all()
    return render(request, "Mensajeria/leerInformacion.html", {"perfil":perfil})
@login_required
def eliminarInformacion(request, id):
    perfil= Perfil.objects.get(id=id)
    perfil.delete()
    perfiles=Perfil.objects.all()
    return render(request, "Mensajeria/leerInformacion.html", {"perfiles":perfiles, "mensaje":"¡Informacion borrado correctamente!"})