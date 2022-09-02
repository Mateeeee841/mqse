from django.urls import path
from . import views 

urlpatterns = [
    path("",views.ver_index,name="index"),
    path("acerca/",views.ver_acerca_de_mi,name="acm"),
    path("retiros/",views.ver_productos,name="productos"),
    path("agenda/",views.ver_store,name="store"),
    path("mas/",views.ver_mas,name="mas"),
    path("contacto/",views.Consultas.as_view(),name="consultas"),
    
]