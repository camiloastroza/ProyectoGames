from django.db import models
from django.urls import reverse
import uuid

class Game(models.Model):
    titulo = models.CharField(max_length=200)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,help_text='ID Unico del VideoJuego')

    descripcion = models.TextField(max_length=1000, help_text='Ingrese una breve descripcion del VideoJuego')
    creador = models.CharField(max_length=200)
    tipogame = models.CharField(max_length=200)
    
    def __str__(self):
        return self.titulo
