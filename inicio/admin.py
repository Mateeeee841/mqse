from django.contrib import admin
from .models import Consulta
# Register your models here.
@admin.register(Consulta)
class Consultaadmin(admin.ModelAdmin):
    list_display=("nombre","id")

