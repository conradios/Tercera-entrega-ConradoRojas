from django.db import models

class Producto(models.Model):
  nombre = models.CharField(max_length=100)
  marca = models.CharField(max_length=100)
  descripcion = models.CharField(max_length=200)
  precio = models.IntegerField()

  def __str__(self):
      return self.nombre
