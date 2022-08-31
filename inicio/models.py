from django.db import models

# Create your models here.
from django.db import models
# Create your models here.
class Consulta(models.Model):
    nombre=models.CharField(max_length=30)
    mensaje=models.TextField(max_length=200)
    email=models.EmailField()
    fecha=models.DateTimeField(auto_now_add=True)
    
#con esto voy a ver el name de los pokemons en el django admin de la pagina
    def __str__(self):              
        return f"{self.nombre}"