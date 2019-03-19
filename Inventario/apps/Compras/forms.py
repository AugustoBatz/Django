from django import forms
from apps.Compras.models import Lote,Facturacompra
from django.forms.models import inlineformset_factory


class LoteForm(forms.ModelForm):
    class Meta:
        model=Lote
        fields=[
            'cantidad',
            'costounitario',
            'producto',
            'costototal',
            'ganancia',
            'preciounitario',
            'preciototal',
           # 'facturacompra',

        ]
        labels={
            'cantidad':'Cantidad',
            'costounitario':'Costo Unitario',
            'producto':'Producto',
            'costototal':'Costo Total',
            'ganancia':'Ganancia',
            'preciounitario':'Precio Unitario',
            'preciototal':'Precio Total',
          #  'facturacompra':'Factura Compra',

        }
        widgets={
            #'cantidad':forms.IntegerField(attrs={'class':'form-control'}),
            #'costounitario':forms.DecimalField(attrs={'class':'form-control'}),
            #'costototal':forms.DecimalField(attrs={'class':'form-control'}),
            #'ganancia':forms.DecimalField(attrs={'class':'form-control'}),
            #'preciounitario':forms.DecimalField(attrs={'class':'form-control'}),
            #'preciototal':forms.DecimalField(attrs={'class':'form-control '}),
        }

class FacturaForm(forms.ModelForm):
    class Meta:
        model=Facturacompra
        fields=[
            'serie',
            'numero',
            'total',
            'proveedor',
            'fecha',
            'cantidad_prod',
        ]
        labels={
            'serie':'Serie',
            'numero':'Número',
            'total':'Total',
            'proveedor':'Proveedor',
            'fecha':'Fecha',
        }
        widgets={
            'serie':forms.TextInput(attrs={'class':'form-control'}),
            'numero':forms.NumberInput(attrs={'class':'form-control'}),
            'nit':forms.TextInput(attrs={'class':'form-control'}),
           # 'total':forms.DecimalField(attrs={'class':'form-control'}),
            'fecha':forms.DateTimeInput(attrs={'class':'form-control'}),

        }

LoteFormSet = inlineformset_factory(Facturacompra, Lote, form=LoteForm, extra=4)
