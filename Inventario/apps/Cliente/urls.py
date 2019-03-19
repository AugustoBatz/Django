from django.urls import path
from apps.Cliente.views import ClienteList,ClienteCrear,ClienteEditar

urlpatterns = [
    path('verClientes/',ClienteList.as_view(),name='VerClientes'),
    path('crearCliente/',ClienteCrear.as_view(),name='CrearClientes'),
    path('editar/<int:pk>/', ClienteEditar.as_view(), name='EditarCliente'),


]
