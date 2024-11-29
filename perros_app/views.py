from django.shortcuts import render, redirect
from .models import Perro
# Create your views here.
def inicio_perros(request):
    losperros=Perro.objects.all()
    return render(request,'gestionarPerros.html',{"misperros":losperros})

def registrarPerro(request):
    codigo=request.POST["txtcodigo"]
    raza=request.POST["txtraza"]
    edad=request.POST["numedad"]
    comportamiento=request.POST["txtcomportamiento"]
    vacunas=request.POST["txtvacunas"]
    sexo=request.POST["txtsexo"]



    guardarPerro=Perro.objects.create(
        codigo=codigo,raza=raza,edad=edad,comportamiento=comportamiento,vacunas=vacunas,sexo=sexo
    ) 
    return redirect ("/")

def seleccionarPerro(request,codigo):
    perro=Perro.objects.get(codigo=codigo)
    return render(request,"editarPerros.html",{"misperros":perro})


def editarPerro(request):
    codigo=request.POST["txtcodigo"]
    raza=request.POST["txtraza"]
    edad=request.POST["numedad"]
    comportamiento=request.POST["txtcomportamiento"]
    vacunas=request.POST["txtvacunas"]
    sexo=request.POST["txtsexo"]
    perro=Perro.objects.get(codigo=codigo)
    perro.raza=raza
    perro.edad=edad
    perro.comportamiento=comportamiento
    perro.vacunas=vacunas
    perro.sexo=sexo
    perro.save()
    return redirect("/") #dsf


def borrarPerro(request,codigo):
    perro=Perro.objects.get(codigo=codigo)
    perro.delete()
    return redirect("/") #asdsda
