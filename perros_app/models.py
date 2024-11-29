from django.db import models

# Create your models here.
class Perro(models.Model):
    codigo=models.CharField(primary_key=True, max_length=50)
    raza=models.CharField(max_length=100)
    edad=models.PositiveSmallIntegerField()
    comportamiento=models.TextField(verbose_name="Comportamiento", max_length=300)
    vacunas=models.TextField(verbose_name="vacunas", max_length=300)
    sexo=models.CharField(max_length=15)


    def __str__(self) -> str:
        return self.raza
