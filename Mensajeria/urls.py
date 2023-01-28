from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView
urlpatterns= [
    
    path("perfil/", perfil, name="perfil"),
    path("editarPerfil/", editarPerfil, name="editarPerfil"),
    path("msj/", msj, name="msj"),
    path("buscarRemitente/", buscarRemitente, name="buscarRemitente"),
    path("resultadosRemitente/", resultadosRemitente, name="resultadosRemitente"),
    path("leerMensajes/", leerMensajes, name="leerMensajes"),
    path("busqueda/", busqueda, name="busqueda"),
    path("agregarInformacion/", agregarInformacion, name="agregarInformacion"),
    path("leerInformacion/", leerInformacion, name="leerInformacion"),
    path("eliminarInformacion/<id>", eliminarInformacion, name="eliminarInformacion"),

]


