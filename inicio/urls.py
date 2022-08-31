from django.urls import path
from . import views 

urlpatterns = [
    path("",views.ver_cv,name="vercv"),
    path("Contacto/",views.Consultas.as_view(),name="consultas"),
    
]