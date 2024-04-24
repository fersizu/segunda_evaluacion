from django.db import models

# Create your models here.
class Superheroe(models.Model):
    nombre = models.CharField(max_length=50)
    poder = models.CharField(max_length=50)
    debilidad = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to="imagenes", null=True)
    def __str__ (self):
        return self.nombre


opciones_respuestas = [
    [0,1],
    [1,2],
    [2,3]


]

class Test(models.Model):
    nombre = models.CharField(max_length=50)
    pregunta1 = models.IntegerField(choices=opciones_respuestas)
    pregunta2 = models.IntegerField(choices=opciones_respuestas)
    pregunta3 = models.IntegerField(choices=opciones_respuestas)
    def calcular_resultado(self):
        return self.pregunta1 + self.pregunta2 + self.pregunta3
    

