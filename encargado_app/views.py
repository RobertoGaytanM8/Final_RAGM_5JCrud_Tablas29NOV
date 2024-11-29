from django.shortcuts import render, redirect
from .models import Encargados
# Create your views here.
def inicio_encargado(request):
    losencargados=Encargados.objects.all()
    return render(request,'gestionarEncargados.html',{"misencargados":losencargados})

def registrarEncargados(request):
    id=request.POST["txtid"]
    nombre=request.POST["txtnombre"]
    apellidos=request.POST["txtapellidos"]
    dni=request.POST["txtdni"]
    fechaenc=request.POST["datefec"]
    sexo=request.POST["txtsexo"]


    guardarEncargados=Encargados.objects.create(
        id=id,nombre=nombre,apellidos=apellidos,dni=dni,fechaenc=fechaenc,sexo=sexo
    ) 
    return redirect ("/")

def seleccionarEncargados(request,id):
    encargado=Encargados.objects.get(id=id)
    return render(request,"editarEncargados.html",{"misencargados":encargado})


def editarEncargados(request):
    id=request.POST["txtid"]
    nombre=request.POST["txtnombre"]
    nombre=request.POST["txtnombre"]
    apellidos=request.POST["txtapellidos"]
    dni=request.POST["txtdni"]
    fechaenc=request.POST["datefec"]
    sexo=request.POST["txtsexo"]
    encargado=Encargados.objects.get(id=id)
    encargado.nombre=nombre
    encargado.nombre=nombre
    encargado.apellidos=apellidos
    encargado.dni=dni
    encargado.fechaenc=fechaenc
    encargado.sexo=sexo
    encargado.save()
    return redirect("/") #dsf


def borrarEncargados(request,id):
    encargado=Encargados.objects.get(id=id)
    encargado.delete()
    return redirect("/") #asdsda
