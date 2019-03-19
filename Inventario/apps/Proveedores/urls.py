from django.urls import path
from apps.Proveedores.views import  *

urlpatterns = [
    path('verProveedores/',ProveedoresList.as_view(),name='VerProveedores'),
    path('crearCliente/',ProveedorCreate.as_view(),name='CrearProveedor'),
    path('editar/<int:pk>/', ProveedorEdit.as_view(), name='EditarProveedor'),


]
