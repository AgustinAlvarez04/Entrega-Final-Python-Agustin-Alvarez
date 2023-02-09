from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView
urlpatterns= [
    
    path("perfil/", perfil, name="perfil"),
    path("editarPerfil/", editarPerfil, name="editarPerfil"),
    path("agregarInformacion/", agregarInformacion, name="agregarInformacion"),
    path("leerInformacion/", leerInformacion, name="leerInformacion"),
    path("eliminarInformacion/<id>", eliminarInformacion, name="eliminarInformacion"),

    path('enviarMsj/', enviarMsj, name='enviarMsj'),
    path('mensajes/', mensajes, name='mensajes'),
    path('buzonMsj/', buzonMsj, name='buzonMsj'),
    path('verMsj/<id>', verMsj, name='verMsj'),
    path('eliminarMsj/<id>', eliminarMsj, name='eliminarMsj'),
    path('responderMsj/<id>', responderMsj, name='responderMsj'),
    path('agregarUrl/', agregarUrl, name='agregarUrl'),
    path('agregarDescripcion/', agregarDescripcion, name='agregarDescripcion'),

]


