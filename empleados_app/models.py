from django.db import models

# Create your models here.
class Empleados(models.Model):
    id=models.CharField(primary_key=True, max_length=50)
    nombre=models.CharField(max_length=100)
    apellidos=models.CharField(max_length=100)
    dni=models.CharField(max_length=10)
    salario=models.IntegerField()
    feching=models.DateField()
    sexo=models.CharField(max_length=15)


    def __str__(self) -> str:
        return self.nombre
