from django.shortcuts import render, redirect
from .models import Jaula
# Create your views here.
def inicio_jaulas(request):
    lasjaulas=Jaula.objects.all()
    return render(request,'gestionarJaulas.html',{"misjaulas":lasjaulas})

def registrarJaula(request):
    id=request.POST["txtid"]
    tipo=request.POST["txttipo"]
    capacidad=request.POST["numcapacidad"]
    tamaño=request.POST["txtamano"]
    candado=request.POST["txtcandado"]
    agua=request.POST["numagua"]
    comida=request.POST["numcomida"]


    guardarJaula=Jaula.objects.create(
        id=id,tipo=tipo,capacidad=capacidad,candado=candado,agua=agua,comida=comida
    ) 
    return redirect ("/")

def seleccionarJaulas(request,id):
    jaula=Jaula.objects.get(id=id)
    return render(request,"editarJaulas.html",{"misjaulas":jaula})


def editarJaula(request):
    id=request.POST["txtid"]
    tipo=request.POST["txttipo"]
    capacidad=request.POST["numcapacidad"]
    candado=request.POST["txtcandado"]
    agua=request.POST["numagua"]
    comida=request.POST["numcomida"]
    jaula=Jaula.objects.get(id=id)
    jaula.tipo=tipo
    jaula.capacidad=capacidad
    jaula.candado=candado
    jaula.agua=agua
    jaula.comida=comida
    jaula.save()
    return redirect("/") #dsf


def borrarJaulas(request,id):
    jaula=Jaula.objects.get(id=id)
    jaula.delete()
    return redirect("/") #asdsda
