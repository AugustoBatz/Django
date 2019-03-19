from django.shortcuts import render,HttpResponseRedirect
from django.urls import reverse_lazy
from apps.Compras.forms import LoteForm,FacturaForm
from django.views.generic import CreateView
from apps.Compras.models import Lote

class CrearLote(CreateView):
    model =Lote
    template_name = 'Facturas/crearLote.html'
    form_class = LoteForm
    second_form_class=FacturaForm
    success_url = reverse_lazy('Clientes:VerClientes')
    def get_context_data(self, **kwargs):
        context=super(CrearLote,self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form']=self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2']=self.second_form_class(self.request.GET)
        return context
    def post(self,request,*args,**kwargs):
        self.object=self.get_object
        form=self.form_class(request.POST)
        form2=self.second_form_class(request.POST)
        if form.is_valid() and form2.is_valid():
            Lote=form.save(commit=False)
            Lote.facturacompra=form2.save()
            Lote.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form,form2=form2))
