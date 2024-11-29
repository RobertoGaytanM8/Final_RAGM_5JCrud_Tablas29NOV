from django.urls import path
from perros_app import views

urlpatterns = [
    path("",views.inicio_perros,name="inicio_perros"),
    path("registrarPerro/",views.registrarPerro,name="registrarPerro"),
    path("seleccionarPerro/<codigo>",views.seleccionarPerro,name="seleccionarPerro"),
    path("editarPerro/",views.editarPerro, name="editarPerro"),
    path("borrarPerro/<codigo>",views.borrarPerro,name="borrarPerro"),
    
]