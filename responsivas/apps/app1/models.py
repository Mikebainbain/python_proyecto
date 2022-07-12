from django.db import models

# Create your models here.

class Usuario(models.Model):
    id = models.AutoField(Primary_key = True)
    nombres = models.CharField(max_leght = 40, blank = False, null = False)
    apellidoP = models.CharField(max_leght = 30, blank = False, null = False)
    apellidoM = models.CharField(max_legth= 30, blank = False, null = False)
    correo = models.CharField(max_length= 60, blank = False, null = False)
