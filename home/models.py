from django.db import models
from django.contrib.auth.models import User

class Recurso(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    # Otros campos relacionados con el recurso

class Permiso(models.Model):
    nombre = models.CharField(max_length=100)
    recursos = models.ManyToManyField(Recurso, related_name='permisos')
    # Otros campos relacionados con el permiso
