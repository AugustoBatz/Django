from django.shortcuts import render,redirect
from django.views.generic import ListView,CreateView,UpdateView
from apps.Cliente.forms import ClienteForm
from django.urls import reverse_lazy
# Create your views here.
from apps.Cliente.models import Cliente
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

def index(request):
    return render(request,'Cliente/VerClientes_Form.html')

def Cliente_edit(request,id_cliente):
    cliente=Cliente.objects.get(id=id_cliente)
    if request.method=='GET':
        form=ClienteForm(instance=cliente)
    else:
        form=ClienteForm(request.POST,instance=cliente)
        if form.is_valid():
            form.save()
        return redirect(VerClientes)
    return render(request,'Cliente/EditarCliente_Form.html',{'form':form})


def VerClientes(request):
    cliente=Cliente.objects.all()
    contexto={'Clientes':cliente}
    return render(request, 'Cliente/VerClientes_Form.html',contexto)

def CrearCliente(request):
    if request.method=='POST':
        form=ClienteForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(VerClientes)
    else:
        form = ClienteForm()
    return render(request,'Cliente/CrearCliente_Form.html',{'form':form})


class StaffRequiredMixin(object):
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request,*args,**kwargs)

class ClienteList(ListView):
    model=Cliente
    template_name ='Cliente/VerClientes_Form2.html'

@method_decorator(login_required,name='dispatch')
class ClienteCrear(CreateView):
    model=Cliente
    form_class = ClienteForm
    template_name = 'Cliente/CrearCliente_Form2.html'
    success_url = reverse_lazy('Clientes:VerClientes')

@method_decorator(login_required,name='dispatch')
class ClienteEditar(UpdateView):
    model=Cliente
    form_class = ClienteForm
    template_name = 'Cliente/EditarCliente_Form2.html'
    success_url = reverse_lazy('Clientes:VerClientes')