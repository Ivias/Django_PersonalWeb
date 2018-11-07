from django.db import models

# Create your models here.
class Project (models.Model):
    title = models.CharField(max_length=2000)
    description = models.TextField()
    image = models.ImageField()
    #Sólo se alamcena la hora de la creación
    created = models.DateField(auto_now_add=True)
    #Se almacena la hora de cada acceso
    ipdated = models.DateField(auto_now=True)