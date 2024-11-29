from django.db import models

# Create your models here.
class Jaula(models.Model):
    id=models.CharField(primary_key=True, max_length=50)
    tipo=models.CharField(max_length=100)
    capacidad=models.PositiveSmallIntegerField()
    candado=models.CharField(max_length=50)
    tamaño=models.CharField(max_length=15)
    comida=models.PositiveSmallIntegerField()
    agua=models.PositiveSmallIntegerField()


    def __str__(self) -> str:
        return self.tipo
