from django.shortcuts import render, redirect
from .models import Empleados
# Create your views here.
def inicio_empleados(request):
    losempleados=Empleados.objects.all()
    return render(request,'gestionarEmpleados.html',{"misempleados":losempleados})

def registrarEmpleados(request):
    id=request.POST["txtid"]
    nombre=request.POST["txtnombre"]
    apellidos=request.POST["txtapellidos"]
    dni=request.POST["txtdni"]
    salario=request.POST["numsal"]
    feching=request.POST["datefec"]
    sexo=request.POST["txtsexo"]


    guardarEmpleado=Empleados.objects.create(
        id=id,nombre=nombre,apellidos=apellidos,dni=dni,salario=salario,feching=feching,sexo=sexo
    ) 
    return redirect ("/")

def seleccionarEmpleado(request,id):
    empleado=Empleados.objects.get(id=id)
    return render(request,"editarEmpleados.html",{"misempleados":empleado})


def editarEmpleados(request):
    id=request.POST["txtid"]
    nombre=request.POST["txtnombre"]
    apellidos=request.POST["txtapellidos"]
    dni=request.POST["txtdni"]
    salario=request.POST["numsal"]
    feching=request.POST["datefec"]
    sexo=request.POST["txtsexo"]
    empleado=Empleados.objects.get(id=id)
    empleado.nombre=nombre
    empleado.apellidos=apellidos
    empleado.dni=dni
    empleado.salario=salario
    empleado.feching=feching
    empleado.sexo=sexo
    empleado.save()
    return redirect("/") #dsf


def borrarEmpleados(request,id):
    empleado=Empleados.objects.get(id=id)
    empleado.delete()
    return redirect("/") #asdsda
