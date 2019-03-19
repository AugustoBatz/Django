from django.shortcuts import render,redirect
from django.http import HttpResponse
from apps.Almacen.forms import CatalogoForm,UnidadForm,PresentacionForm
from apps.Almacen.models import Catalogo,Presentacion1,Unidadmedida1

# Create your views here.


def input(request):
    catalogo = Catalogo.objects.all()
    prese=Presentacion1.objects.all()
    unidad=Unidadmedida1.objects.all()
    if request.method == 'POST':
        submitted = request.POST.get('form_id', '')

        if submitted == 'Unidad':
            # Get the Form1 instance
            my_demographics = UnidadForm(request.POST)  # DemographicForm=UNidadForm
            if my_demographics.is_valid():
                my_demographics.save()
                return redirect('Almacen:CrearAlmacen')
            else:
                my_diagnosis = CatalogoForm()
                Pres = PresentacionForm()

        elif submitted == 'Catalogo':
            my_diagnosis = CatalogoForm(request.POST)
            if my_diagnosis.is_valid():
                my_diagnosis.save()
                return redirect('Almacen:CrearAlmacen')
            else:
                my_demographics = UnidadForm()
                Pres = PresentacionForm()

            # here you should redirect
        elif submitted == 'Presentacion':
# Get the Form2 instance
            Pres = PresentacionForm(request.POST)
            if Pres.is_valid():
                Pres.save()
                return redirect('Almacen:CrearAlmacen')
            else:
                my_demographics = UnidadForm()
                my_diagnosis = CatalogoForm()
                # here you should redirect

        else:
            raise ValueError('Eror aca')

    else:

        Pres = PresentacionForm()
        my_demographics = UnidadForm()
        my_diagnosis = CatalogoForm()

    return render(request, 'Almacen/CrearAlmacen.html',
              {'frm': my_demographics, 'frm_d': my_diagnosis, 'Catalogo': catalogo,
               'frm_c': Pres,'prese':prese,'unidad':unidad})

