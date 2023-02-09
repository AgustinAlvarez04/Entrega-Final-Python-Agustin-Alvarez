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
def enviarMsj(request):
    if request.method == 'POST':
        form = MsjForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            usuario = request.user
            receptor = info['receptor']
            mensaje = info['mensaje']
            mensaje = Msjs(usuario=usuario, receptor=receptor, mensaje=mensaje)
            mensaje.save()
            return render(request, 'Mensajeria/mensajes.html', {'mensaje': 'mensaje enviado correctamente', 'avatar': obtenerAvatar(request)})
        else:
            return render(request, 'Mensajeria/enviarMsj.html', {'form': form, 'mensaje': 'mensaje no enviado', 'avatar': obtenerAvatar(request)})
    else:
        form = MsjForm()
        return render(request, 'Mensajeria/enviarMsj.html', {'form': form, 'avatar': obtenerAvatar(request)})
@login_required
def mensajes(request):
    return render(request, 'Mensajeria/mensajes.html', {'avatar': obtenerAvatar(request)})
@login_required
def buzonMsj(request):
    if request.user.is_authenticated:
        mensajes = Msjs.objects.filter(receptor=request.user)
        if len(mensajes) != 0:
            return render(request, 'Mensajeria/buzonMsj.html', {'mensajes': mensajes, 'avatar': obtenerAvatar(request)})
        else:
            return render(request, 'Mensajeria/buzonMsj.html', {'mensaje': 'No hay mensajes', 'avatar': obtenerAvatar(request)})
@login_required
def verMsj(request, id):
    mensaje = Msjs.objects.get(id=id)
    mensaje.leido = True
    mensaje.save()
    return render(request, 'Mensajeria/verMsj.html', {'mensaje': mensaje, 'avatar': obtenerAvatar(request)})
@login_required
def eliminarMsj(request, id):
    mensaje = Msjs.objects.get(id=id)
    mensaje.delete()
    return render(request, 'Mensajeria/mensajes.html', {'mensaje': 'mensaje eliminado correctamente', 'avatar': obtenerAvatar(request)})
@login_required
def responderMsj(request, id):
    mensaje = Msjs.objects.get(id=id)
    if request.method == 'POST':
        form = MsjForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            usuario = request.user
            receptor = info['receptor']
            mensaje = info['mensaje']
            mensaje = Msjs(usuario=usuario, receptor=receptor, mensaje=mensaje)
            mensaje.save()
            return render(request, 'App/inicio.html', {'mensaje': 'mensaje enviado correctamente', 'avatar': obtenerAvatar(request)})
        else:
            return render(request, 'Mensajeria/enviarMsj.html', {'form': form, 'mensaje': 'mensaje no enviado', 'avatar': obtenerAvatar(request)})
    else:
        form = MsjForm()
        return render(request, 'Mensajeria/enviarMsj.html', {'form': form, 'mensaje': mensaje, 'avatar': obtenerAvatar(request)})
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
def agregarUrl (request):
    if request.method == 'POST':
        form = Formulario_url(request.POST)
        if form.is_valid():
            url = Url(usuario=request.user, url=request.POST['url'])
            urlViejo= Url.objects.filter(usuario=request.user)
            if len(urlViejo)>0:
                urlViejo[0].delete()
            url.save()
            return render (request, 'Mensajeria/perfil.html', {'form': form, 'avatar': obtenerAvatar(request), 'url' : obtener_url(request), 'mensaje': 'Url agregada exitosamente'})
        else:
            return render (request, 'Mensajeria/agregarUrl.html', {'form': form, 'avatar': obtenerAvatar(request), 'mensaje': 'Error al agregar la url'})
    else:
        form = Formulario_url()
        return render(request, 'Mensajeria/agregarUrl.html', {'form': form, 'avatar': obtenerAvatar(request)})

@login_required
def obtener_url(request):
    lista = Url.objects.filter(usuario=request.user)
    if len(lista) != 0:
        url = lista[0].url
    else:
        url = ''
    return url

@login_required
def agregarDescripcion (request):
    if request.method == 'POST':
        form = Formulario_descripcion(request.POST)
        if form.is_valid():
            descripcion = Descripcion(usuario=request.user, descripcion=request.POST['descripcion'])
            descripcionVieja= Descripcion.objects.filter(usuario=request.user)
            if len(descripcionVieja)>0:
                descripcionVieja[0].delete()
            descripcion.save()
            return render (request, 'Mensajeria/perfil.html', {'form': form, 'avatar': obtenerAvatar(request), 'mensaje': 'Descripcion agregada exitosamente', 'descripcion': obtener_descripcion(request)})
        else:
            return render (request, 'Mensajeria/agregarDescripcion.html', {'form': form, 'avatar': obtenerAvatar(request), 'mensaje': 'Error al agregar la descripcion'})
    else:
        form = Formulario_descripcion()
        return render(request, 'Mensajeria/agregarDescripcion.html', {'form': form, 'avatar': obtenerAvatar(request)})

@login_required
def obtener_descripcion(request):
    lista = Descripcion.objects.filter(usuario=request.user)
    if len(lista) != 0:
        descripcion = lista[0].descripcion
    else:
        descripcion = ''
    return descripcion






































@login_required
def perfil(request):
    perfil=Perfil.objects.all()
    return render(request, "Mensajeria/perfil.html", {"perfil": perfil, "avatar": obtenerAvatar(request)})
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
