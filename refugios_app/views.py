from django.shortcuts import render, redirect
from .models import Refugio
# Create your views here.
def inicio_refugios(request):
    losrefugios=Refugio.objects.all()
    return render(request,'gestionarRefugios.html',{"misrefugios":losrefugios})

def registrarRefugio(request):
    id=request.POST["txtid"]
    cantperros=request.POST["numperros"]
    empleados=request.POST["txtempleados"]
    telefono=request.POST["numtelefono"]
    cantcomida=request.POST["numcomida"]
    encargado=request.POST["txtencargado"]

    guardarPerro=Refugio.objects.create(
        id=id,cantperros=cantperros,empleados=empleados,telefono=telefono,cantcomida=cantcomida,encargado=encargado
    ) 
    return redirect ("/")

def seleccionarRefugio(request,id):
    refugio=Refugio.objects.get(id=id)
    return render(request,"editarRefugios.html",{"misrefugios":refugio})


def editarRefugio(request):
    id=request.POST["txtid"]
    cantperros=request.POST["numperros"]
    empleados=request.POST["txtempleados"]
    telefono=request.POST["numtelefono"]
    cantcomida=request.POST["numcomida"]
    encargado=request.POST["txtencargado"]
    refugio=Refugio.objects.get(id=id)
    refugio.id=id
    refugio.cantperros=cantperros
    refugio.empleados=empleados
    refugio.telefono=telefono
    refugio.cantcomida=cantcomida
    refugio.encargado=encargado
    refugio.save()
    return redirect("/") #dsf


def borrarRefugio(request,id):
    refugio=Refugio.objects.get(id=id)
    refugio.delete()
    return redirect("/") #asdsda
