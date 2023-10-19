from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Disco(models.Model):
    nombre = models.CharField(max_length=40)
    autor = models.CharField(max_length=40)
    año = models.IntegerField()
    precio = models.IntegerField()
    
    def __str__(self):
        return f"{self.nombre} - {self.autor} - {self.año}"

    
class Usuario(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)

class Producto(models.Model):
    album = models.CharField(max_length=40)
    artista = models.CharField(max_length=40)
    precio = models.IntegerField()
    

class Comentario(models.Model):
    comentario = models.ForeignKey(Disco, related_name='comentarios', on_delete=models.CASCADE, null=True)
    nombre = models.CharField(max_length=40)
    mensaje = models.TextField(null=True, blank=True)
    fechaComentario = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fechaComentario']

    def __str__(self):
        return '%s - %s' % (self.nombre, self.comentario)





