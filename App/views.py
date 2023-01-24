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
            return render(request , "App/inicio.html", {"mensaje": "Avatar subido correctamente"})
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
            blog= Blog.objects.filter(blog__icontains=blog)
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
def perfil(request):
    perfil=Perfil.objects.all()
    return render(request, "App/perfil.html", {"perfil": perfil, "avatar": obtenerAvatar(request)})



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
        titulo=request.POST["titulo"]
        subtitulo=request.POST["subtitulo"]
        cuerpo=request.POST["cuerpo"]
        autor=request.POST["autor"]
        fecha=request.POST["fecha"]
        imagen=request.POST["imagen"]
        blog= Blog(titulo=titulo, subtitulo=subtitulo, cuerpo=cuerpo, autor=autor, fecha=fecha, imagen=imagen)
        blog.save()
        return render (request, "App/blogs.html" ,{"mensaje": "Blog subido correctamente"})

    else:
        return render (request, "App/crearBlog.html")

@login_required
def leerBlogs(request):
    blog=Blog.objects.all()
    return render(request, "App/blogs.html", {"blog":blog})

@login_required
def editarBlog(request, id):
    blog=Blog.objects.get(id=id)
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
            blog.save()
            blog=Blog.objects.all()
            return render(request, "App/blogs.html", {"blog":blog, "mensaje": "Profesor editado correctamente"})
        pass
    else:
        formulario= BlogForm(initial={"titulo":blog.titulo, "subtitulo":blog.subtitulo, "cuerpo":blog.cuerpo, "autor":blog.autor, "fecha":blog.fecha, "imagen":blog.imagen})
        return render(request, "App/editarBlog.html", {"form":formulario, "blog":blog })

@login_required
def eliminarBlog(request, id):
    blog= Blog.objects.get(id=id)
    blog.delete()
    blog= Blog.objects.all()
    return render(request, "App/blogs.html", {"blogs":blog , "mensaje":"Blog eliminado correctamente"})













