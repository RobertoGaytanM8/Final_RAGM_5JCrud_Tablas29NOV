from django.urls import path
from empleados_app import views

urlpatterns = [
    path("",views.inicio_empleados,name="inicio_empleados"),
    path("registrarEmpleados/",views.registrarEmpleados,name="registrarEmpleados"),
    path("seleccionarEmpleado/<id>",views.seleccionarEmpleado,name="seleccionarEmpleado"),
    path("editarEmpleados/",views.editarEmpleados, name="editarEmpleados"),
    path("borrarEmpleados/<id>",views.borrarEmpleados,name="borrarEmpleados"),
    
]