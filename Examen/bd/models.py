from django.db import models

# Create your models here.

class alumnos(models.Model):
    nombre=models.CharField(max_length=30)
    apellidopaterno=models.CharField(max_length=30)
    apellidomaterno=models.CharField(max_length=30)
    JEFE = "JF"
    SUBJEFE = "SJ"
    ORDINARIO = "OR"
    rol_estudiante = [
        (JEFE, "Jefe de Grupo"),
        (SUBJEFE, "Sub Jefe de Grupo"),
        (ORDINARIO, "Ordinario"),
    ]
    rol_estudiante = models.CharField(max_length=2,choices=rol_estudiante,default=JEFE)
    

class grupo(models.Model):
    nombre=models.CharField(max_length=50)
    estatus=models.BooleanField()

class clase(models.Model):
    nombre=models.CharField(max_length=40)