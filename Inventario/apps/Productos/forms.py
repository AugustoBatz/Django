from django import forms
from apps.Productos.models import Producto
from apps.Almacen.forms import UnidadForm


class ProductoForm(forms.ModelForm):
    class Meta:
        model=Producto
        fields=[
            'nombre',
            'marca',
            'codigo',
            'stockminimo',
            'ganancia',
            'unidadmedida_1',
            'presentacion_1',
            'catalogo',




        ]
        labels={
            'nombre':'Nombre',
            'marca':'Marca',
            'codigo': 'Codigo',
            'stockminimo':'Stock Minimo',
            'unidadmedida_1':'Unidad',
            'presentacion_1':'Presentación',
            'catalogo': 'Categoría',
            'ganancia':'Ganancia',

        }
        widgets={
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'marca':forms.TextInput(attrs={'class':'form-control'}),
            'codigo':forms.TextInput(attrs={'class':'form-control'}),

            #'gananacia':forms.DecimalField(attrs={'class':'form-control'}),

        }
