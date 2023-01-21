from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView
urlpatterns= [

    path("", inicio, name="Inicio"),
    path('about/', about, name="About"),
    path('contact/', contact, name="Contact"),
    path('pages/', pages, name="Pages" ),

    path("register/", register, name="register"),
    path("login/", login_request, name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),

    path("busqueda/", busqueda, name="busqueda"),
    path("resultados/", resultados, name="resultados"),
   
]