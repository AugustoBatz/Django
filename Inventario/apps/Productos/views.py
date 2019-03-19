from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView,UpdateView
from apps.Productos.models import Producto
from apps.Almacen.models import Unidadmedida1
from apps.Productos.forms import ProductoForm
# Create your views here.
class CrearProducto(CreateView):
    model = Producto
    form_class =ProductoForm
    template_name = 'Producto/CrearProducto.html'
    success_url = reverse_lazy('Productos:Inventario')

class VerProductos(ListView):
    model = Producto
    template_name = 'Producto/Inventario.html'
