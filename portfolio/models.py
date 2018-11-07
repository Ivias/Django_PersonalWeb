from django.db import models

# Create your models here.
class Project (models.Model):
    title = models.CharField(max_length=2000, verbose_name='Título')
    description = models.TextField(verbose_name='Descripción')
    image = models.ImageField(verbose_name='Imagen', upload_to = "projects")
    #Sólo se alamcena la hora de la creación
    created = models.DateField(auto_now_add=True,  verbose_name='Fecha de creación')
    #Se almacena la hora de cada acceso
    updated = models.DateField(auto_now=True,  verbose_name='Fecha de edición')

    class Meta:
        verbose_name = 'proyecto'
        verbose_name_plural = 'proyectos'
        ordering = ["-created"]
    
    def __str__(self):
        return self.title
