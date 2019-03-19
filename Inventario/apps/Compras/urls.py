from django.urls import path
from apps.Compras.views import *

urlpatterns = [
    path('verClientes/',CrearLote.as_view(),name='Compras'),


]
