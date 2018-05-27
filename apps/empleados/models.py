from django.db import models

from apps.puestos.models import Puesto

# Create your models here.
class Empleado(models.Model):
	"""docstring for Empleado"""
	empleado = models.CharField(max_length=50, primary_key=True)
	puesto =models.ForeignKey(Puesto, null=False, blank=False, on_delete=models.CASCADE)
	nombre = models.CharField(max_length=50)
	apellido_pat = models.CharField(max_length=50)
	apellido_mat = models.CharField(max_length=50)
	calle = models.CharField(max_length=50)
	colonia = models.CharField(max_length=50)
	delegacion = models.CharField(max_length=50)
	municipio = models.CharField(max_length=50)
	codpost = models.CharField(max_length=50)

