from django.db import models

# Create your models here.
class Adoptante(models.Model):
    id=models.CharField(primary_key=True, max_length=50)
    nombre=models.CharField(max_length=100)
    apellido=models.CharField(max_length=100)
    dni=models.CharField(max_length=10)
    edad=models.IntegerField()
    sexo=models.CharField(max_length=15)


    def __str__(self) -> str:
        return self.nombre
