from django.db import models

# Create your models here.
class Refugio(models.Model):
    id=models.CharField(primary_key=True, max_length=50)
    cantperros=models.PositiveSmallIntegerField()
    empleados=models.PositiveBigIntegerField()
    telefono=models.IntegerField()
    cantcomida=models.PositiveSmallIntegerField()
    encargado=models.CharField(max_length=25)


    def __str__(self) -> str:
        return self.id
