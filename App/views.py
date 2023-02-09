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
#------------------------- NAVBAR -----------------------------------#
def inicio(request):
    return render(request, "App/inicio.html")
@login_required
def about(request):
    return render(request, 'App/about.html')
@login_required
def contact(request):
    return render(request, 'App/contact.html')
@login_required
def pages(request):
    return render(request, 'App/pages.html')
@login_required
def blogs(request):
    return render(request, 'App/blogs.html') 
#--------------------------------- CREACION DE USUARIOS --------------------------------------#
def register(request):
    if request.method=="POST":
        form= RegistroUsuarioForm(request.POST)
        if form.is_valid():
            username= form.cleaned_data.get("username")
            form.save()
            return render(request, "App/register.html", {"mensaje": f"Usuario {username} creado correctamente", "mensaje2": "Ya puede loguearse"})
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
            usuario=authenticate(username=usuario, password=clave)
            if usuario is not None:
                login(request, usuario)
                return render(request, "Mensajeria/perfil.html", {"mensaje":f"Usuario {usuario} logueado correctamente"})
            else:
                return render(request, "App/login.html", {"form":form, "mensaje":"Usuario o contraseña incorrectos"})
        else:
            return render(request, "App/login.html", {"form":form, "mensaje":"Usuario o contraseña incorrectos"})
    else:    
        form= AuthenticationForm()
        return render(request, "App/login.html", {"form":form})

#--------------------------------- BUSCADORES --------------------------------------#
@login_required
def buscarBlog(request):
    return render(request, "App/buscarBlog.html")
@login_required
def buscar(request):
    titulo=request.GET['titulo']
    if titulo!="":
        blog=Blog.objects.filter(titulo__icontains=titulo)
        return render(request, "App/resultadosBlog.html", {"blog":blog})
    else:
        return render(request, "App/buscarBlog.html", {"mensaje":"Ingresa un titulo para buscar!"})
@login_required
def resultadosBlog(request):
    return render(request, 'App/resultados.html')  
#--------------------------------- CREACION DE FORMULARIOS --------------------------------------#
#--------------------------------- CRUD --------------------------------------#
@login_required
def crearBlog(request):
    if request.method=="POST":
        form= BlogForm(request.POST, request.FILES)
        if form.is_valid():
            informacion=form.cleaned_data
            titulo=informacion["titulo"]
            subtitulo=informacion["subtitulo"]
            cuerpo=informacion["cuerpo"]
            autor=informacion["autor"]
            fecha=informacion["fecha"]
            imagen=request.FILES["imagen"]
            blog=Blog(titulo=titulo, subtitulo=subtitulo, cuerpo=cuerpo, autor=autor, fecha=fecha, imagen=imagen)
            blog.save()
            return render (request, "App/blogs.html" ,{"mensaje": "Blog subido correctamente", "mensaje2":"Mira tu blog en 'Inspeccionar publicaciones'"})
        else:
            return render (request, "App/crearBlog.html", {"form":form , "mensaje":"Informacio no valida"})
    else:
        formulario= BlogForm()
        return render (request, "App/crearBlog.html", {"form":formulario})
@login_required
def leerBlog(request):
    blog= Blog.objects.all()
    return render(request, "App/leerBlog.html", {"blog":blog, 'avatar': obtenerAvatar(request)})
@login_required
def eliminarBlog(request, id):
    blog=Blog.objects.get(id=id)
    blog.delete()
    blog=Blog.objects.all()
    return render(request, "App/leerBlog.html", {"blog":blog, "mensaje":"¡Blog borrado correctamente!"})
@login_required
def editarBlog(request, id):
    blog=Blog.objects.get(id=id)
    if request.method=="POST":
        form=BlogForm(request.POST, request.FILES)
        if form.is_valid():
            info=form.cleaned_data
            blog.titulo= info["titulo"]
            blog.subtitulo= info["subtitulo"]
            blog.cuerpo= info["cuerpo"]
            blog.autor= info["autor"]
            blog.fecha= info["fecha"]
            blog.imagen= info["imagen"]
            blog.save()
            blog=Blog.objects.all()
            return render(request, "App/leerBlog.html", {"blog":blog, "mensaje": "Articulo editado correctamente"})
        pass
    else:
        formulario= BlogForm(initial={"titulo":blog.titulo, "subtitulo":blog.subtitulo, "cuerpo":blog.cuerpo, "autor":blog.autor, "fecha":blog.fecha})
        return render(request, "App/editarBlog.html", {"form":formulario, "blog":blog })