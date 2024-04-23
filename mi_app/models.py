from django.db import models

# Create your models here.
class Superheroe(models.Model):
    nombre = models.CharField(max_length=50)
    poder = models.CharField(max_length=50)
    debilidad = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to="imagenes", null=True)
    def __str__ (self):
        return self.nombre


class Usuario(models.Model):
    alias = models.CharField(max_length=50)
    edad = models.IntegerField()
    nombre = models.ForeignKey(Superheroe, on_delete=models.PROTECT)

    def __str__ (self): 
        return self.alias




