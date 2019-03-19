from django.urls import path
from apps.Almacen.views import input

urlpatterns = [

    path('crearAlmacen/',input,name='CrearAlmacen'),




]
