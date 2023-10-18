from django.db import models

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
   







