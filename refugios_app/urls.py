from django.urls import path
from refugios_app import views

urlpatterns = [
    path("",views.inicio_refugios,name="inicio_refugios"),
    path("registrarRefugio/",views.registrarRefugio,name="registrarRefugio"),
    path("seleccionarRefugio/<id>",views.seleccionarRefugio,name="seleccionarRefugio"),
    path("editarRefugio/",views.editarRefugio, name="editarRefugio"),
    path("borrarRefugio/<id>",views.borrarRefugio,name="borrarRefugio"),
    
]