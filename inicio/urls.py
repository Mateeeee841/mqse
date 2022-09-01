from django.urls import path
from . import views 

urlpatterns = [
    path("",views.ver_index,name="index"),
    path("acerca/",views.ver_acerca_de_mi,name="acm"),
    path("productos/",views.ver_productos,name="productos"),
    path("store/",views.ver_store,name="store"),
    path("contacto/",views.Consultas.as_view(),name="consultas"),
    
]