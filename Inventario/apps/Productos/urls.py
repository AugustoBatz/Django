from django.urls import path
from apps.Productos.views import *

urlpatterns = [


    path('crear/',CrearProducto.as_view(),name='CrearProducto'),
    path('inventario/',VerProductos.as_view(),name='Inventario')

]
