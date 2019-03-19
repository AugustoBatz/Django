from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView
from apps.FacturaVenta.models import Facturaventa

# Create your views here.
class CrearFactura(CreateView):
    model=Facturaventa
    template_name = 'Facturas/CrearFacturaVenta.html'