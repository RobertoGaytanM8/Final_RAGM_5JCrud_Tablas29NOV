from django.urls import path
from encargado_app import views

urlpatterns = [
    path("",views.inicio_encargado,name="inicio_encargado"),
    path("registrarEncargados/",views.registrarEncargados,name="registrarEncargados"),
    path("seleccionarEncargados/<id>",views.seleccionarEncargados,name="seleccionarEncargados"),
    path("editarEncargados/",views.editarEncargados, name="editarEncargados"),
    path("borrarEncargados/<id>",views.borrarEncargados,name="borrarEncargados"),
    
]