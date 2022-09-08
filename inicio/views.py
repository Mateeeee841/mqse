from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Consulta
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
# Create your views here.

def ver_mas(request):
    context={}
    plantilla=loader.get_template("mas.html")  
    documento= plantilla.render (context)    
    return HttpResponse(documento)

def ver_index(request):
    context={}
    plantilla=loader.get_template("index.html")  
    documento= plantilla.render (context)    
    return HttpResponse(documento)

def ver_acerca_de_mi(request):
    context={}
    plantilla=loader.get_template("about.html")  
    documento= plantilla.render (context)    
    return HttpResponse(documento)

def ver_productos(request):
    context={}
    plantilla=loader.get_template("products.html")  
    documento= plantilla.render (context)    
    return HttpResponse(documento)

def ver_productos2(request):
    context={}
    plantilla=loader.get_template("products2.html")  
    documento= plantilla.render (context)    
    return HttpResponse(documento)

def ver_store(request):
    context={}
    plantilla=loader.get_template("store.html")  
    documento= plantilla.render (context)    
    return HttpResponse(documento)


class Consultas(CreateView):
    model=Consulta
    success_url=reverse_lazy("consultas")            
    template_name="contacto.html"
    fields=["nombre","mensaje","email"]


