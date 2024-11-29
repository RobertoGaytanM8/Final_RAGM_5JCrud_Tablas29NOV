from django.urls import path
from adoptantes_app import views

urlpatterns = [
    path("",views.inicio_vistaa,name="inicio_vistaa"),
    path("registrarAdoptante/",views.registrarAdoptante,name="registrarAdoptante"),
    path("seleccionarAdoptante/<id>",views.seleccionarAdoptante,name="seleccionarAdoptante"),
    path("editarAdoptante/",views.editarAdoptante, name="editarAdoptante"),
    path("borrarAdoptante/<id>",views.borrarAdoptante,name="borrarAdoptante"),
    
]