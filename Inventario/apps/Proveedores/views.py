from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView
from apps.Proveedores.forms import ProveedorForm
from apps.Proveedores.models import Proveedor
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy

class StaffRequiredMixin(object):
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request,*args,**kwargs)

class ProveedoresList(ListView):
    model=Proveedor
    template_name ='Proveedor/VerProveedores.html'

@method_decorator(login_required,name='dispatch')
class ProveedorCreate(CreateView):
    model=Proveedor
    form_class = ProveedorForm
    template_name = 'Proveedor/CrearProveedor.html'
    success_url = reverse_lazy('Proveedores:VerProveedores')

@method_decorator(login_required,name='dispatch')
class ProveedorEdit(UpdateView):
    model=Proveedor
    form_class = ProveedorForm
    template_name = 'Proveedor/EditarProveedor.html'
    success_url = reverse_lazy('Proveedores:VerProveedores')