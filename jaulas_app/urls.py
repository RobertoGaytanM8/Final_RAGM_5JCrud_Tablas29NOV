from django.urls import path
from jaulas_app import views

urlpatterns = [
    path("",views.inicio_jaulas,name="inicio_jaulas"),
    path("registrarJaula/",views.registrarJaula,name="registrarJaula"),
    path("seleccionarJaulas/<id>",views.seleccionarJaulas,name="seleccionarJaulas"),
    path("editarJaula/",views.editarJaula, name="editarJaula"),
    path("borrarJaulas/<id>",views.borrarJaulas,name="borrarJaulas"),
    
]