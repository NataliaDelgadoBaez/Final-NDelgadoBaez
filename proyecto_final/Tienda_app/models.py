from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Disco(models.Model):
    nombre = models.CharField(max_length=40)
    autor = models.CharField(max_length=40)
    año = models.IntegerField()
    imagen = models.ImageField(null=True, blank=True, upload_to="assets/img/")
    descripcion = models.CharField(max_length=120, null=True, blank=True)
    precio = models.IntegerField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def _str_(self):
        return f"{self.nombre} - {self.autor} - {self.año} - {self.imagen} - {self.precio}"
    

    
class Usuario(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)


class Comentario(models.Model):
    comentario = models.ForeignKey(Disco, related_name='comentarios', on_delete=models.CASCADE, null=True)
    nombre = models.CharField(max_length=40)
    mensaje = models.TextField(null=True, blank=True)
    fechaComentario = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fechaComentario']

    def __str__(self):
        return '%s - %s' % (self.nombre, self.comentario)

class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)




