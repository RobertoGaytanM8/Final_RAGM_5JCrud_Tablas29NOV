from django.shortcuts import render, redirect
from .models import Adoptante
# Create your views here.
def inicio_vistaa(request):
    losadoptantes=Adoptante.objects.all()
    return render(request,'gestionarAdoptantes.html',{"misadoptante":losadoptantes})

def registrarAdoptante(request):
    id=request.POST["txtid"]
    nombre=request.POST["txtnombre"]
    apellido=request.POST["txtapellido"]
    dni=request.POST["numdni"]
    edad=request.POST["numedad"]
    sexo=request.POST["txtsexo"]
    

    guardarAdoptante=Adoptante.objects.create(
        id=id,nombre=nombre,apellido=apellido,dni=dni,edad=edad,sexo=sexo
    ) 
    return redirect('/')

def seleccionarAdoptante(request,id):
    adoptante=Adoptante.objects.get(id=id)
    return render(request,"editarAdoptantes.html",{"misadoptante":adoptante})


def editarAdoptante(request):
    id=request.POST["txtid"]
    nombre=request.POST["txtnombre"]
    apellido=request.POST["txtapellido"]
    dni=request.POST["numdni"]
    edad=request.POST["numedad"]
    sexo=request.POST["txtsexo"]
    adoptante=Adoptante.objects.get(id=id)
    adoptante.id=id
    adoptante.nombre=nombre
    adoptante.apellido=apellido
    adoptante.dni=dni
    adoptante.edad=edad
    adoptante.sexo=sexo
    adoptante.save()
    return redirect("/") #dsf


def borrarAdoptante(request,id):
    adoptante=Adoptante.objects.get(id=id)
    adoptante.delete()
    return redirect("/") #asdsda


