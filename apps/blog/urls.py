from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='index'),
    path("generales/", generales, name="generales"),
    path("programacion/", programacion, name="programacion"),
    path("tutoriales/", tutoriales, name="tutoriales"),
    path("videojuegos/", videojegos, name="videojuegos"),
    path("tecnologia/", tecnologia, name="tecnologia"),
    path("<slug:slug>/",detallePost, name="detalle_post")

]
