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
    lista=Avatar.objects.filter(user=request.user)
    if len(lista)!=0:
        avatar=lista[0].imagen.url
    else:
        avatar="/media/avatars/images.png"
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
def resultados(request):
    return render(request, 'App/resultados.html') 
@login_required
def blogs(request):
    return render(request, 'App/blogs.html') 


#--------------------------------- BUSCADORES --------------------------------------#
@login_required
def buscarBlog(request):
    return render(request, "App/buscarBlog.html")
@login_required
def buscar(request):
        blog= request.GET['blog']
        if blog != "":
            blog= Blogs.objects.filter(blog__icontains=blog)
            return render(request, "App/resultados.html", {"blog": blog})
        else:
            return render(request, "App/buscarBlog.html", {"mensaje": "Ingresaste un blog equivocado"})

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
            usuario=authenticate(username=usuario, password=clave)
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
            return render(request, "App/inicio.html", {"mensaje" : f"Usuario {usuario.username} editado correctamente"})
        else:
            return render(request, "App/editarPerfil.html", {"form":form , "nombreusuario": usuario.username})    
    else:
        form=UserEditForm(instance=usuario)
        return render(request, "App/editarPerfil.html", {"form":form , "nombreusuario": usuario.username})

#--------------------------------- CREACION DE FORMULARIOS --------------------------------------#

@login_required
def crearBlog(request):
    if request.method=="POST":
        form= BlogForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            titulo= informacion["titulo"]
            subtitulo= informacion["subtitulo"]
            cuerpo= informacion["cuerpo"]
            autor= informacion["autor"]
            fecha= informacion["fecha"]
            imagen= informacion["imagen"]
            blogs= Blogs( titulo=titulo, subtitulo=subtitulo, cuerpo=cuerpo, autor=autor, fecha=fecha, imagen=imagen )
            blogs.save()
            return render (request, "App/crearBlog.html", {"mensaje": "Post subido correctamente"})
        else:
            return render (request, "App/crearBlog.html", {"form": form, "mensaje": "Informacion no valida"})
    else:
        formulario= BlogForm()
        return render(request, "App/crearBlog.html",{"form": formulario})

@login_required
def leerBlogs(request):
    blog=Blogs.objects.all()
    return render(request, "App/blogs.html", {"blog":blog})

@login_required
def editarBlog(request, id):
    blog=Blogs.objects.get(id=id)
    if request.method=="POST":
        form=BlogForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            blog.titulo= info["titulo"]
            blog.subtitulo= info["subtitulo"]
            blog.cuerpo= info["cuerpo"]
            blog.autor= info["autor"]
            blog.fecha= info["fecha"]
            blog.imagen= info["imagen"]
            blogs.save()
            blog=Blogs.objects.all()
            return render(request, "App/blogs.html", {"blog":blog, "mensaje": "Profesor editado correctamente"})
        pass
    else:
        formulario= BlogForm(initial={"titulo":blog.titulo, "subtitulo":blog.subtitulo, "cuerpo":blog.cuerpo, "autor":blog.autor, "fecha":blog.fecha, "imagen":blog.imagen})
        return render(request, "App/editarBlog.html", {"form":formulario, "blog":blog })

@login_required
def eliminarBlog(request, id):
    blog= Blogs.objects.get(id=id)
    blog.delete()
    blogs= Blogs.objects.all()
    return render(request, "App/blogs.html", {"blogs":blog , "mensaje":"Blog eliminado correctamente"})













