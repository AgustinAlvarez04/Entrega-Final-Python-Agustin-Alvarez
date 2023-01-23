from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView
urlpatterns= [

    path("", inicio, name="Inicio"),
    path('about/', about, name="About"),
    path('contact/', contact, name="Contact"),
    path('pages/', pages, name="Pages" ),
    path("blogs/", blogs, name="Blogs"),

    path("register/", register, name="register"),
    path("login/", login_request, name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),

    path("editarPerfil/", editarPerfil, name="editarPerfil"),
    path("agregarAvatar/", agregarAvatar, name="agregarAvatar"),
    
    path("buscar/", buscar, name="buscar"),
    path("resultados/", resultados, name="resultados"),
    path("buscarBlog/", buscarBlog, name="buscarBlog"),

    path("crearBlog/", crearBlog, name="crearBlog"),
    path("leerBlogs/", leerBlogs, name="leerBlogs"),
    path("editarBlog/<id>", editarBlog, name="editarBlog"),
    path("eliminarBlog/<id>", eliminarBlog, name="eliminarBlog"),
    




]