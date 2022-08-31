from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Consulta
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
# Create your views here.

def ver_cvesp(request):
    plantilla=loader.get_template("indexesp.html")  
    documento= plantilla.render ()    
    return HttpResponse(documento)

def ver_cv(request):
    context={}
    plantilla=loader.get_template("index.html")  
    documento= plantilla.render (context)    
    return HttpResponse(documento)

class Consultas(CreateView):
    model=Consulta
    success_url=reverse_lazy("vercvesp")            
    template_name="contacto.html"
    fields=["nombre","mensaje","email"]
   
class contact(CreateView):
    model=Consulta
    success_url=reverse_lazy("vercv")            
    template_name="contact.html"
    fields=["nombre","mensaje","email"]
