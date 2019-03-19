from django import forms
from apps.FacturaVenta.models import Facturaventa


class FacturaForm(forms.ModelForm):
    class Meta:
        model=Facturaventa
        fields=[
            'total',
            'fecha',
            'serie',
            'numero',
            #'cliente',
            #'resoluciones',
            'cantidad_prod',
            'anulado',
            #'usuarios',
            'trans',
            'fechaanulado',
            'subtotal',
            'descuento',
        ]
        labels={
            'total':'Total',
            'fecha':'Fecha',
            'serie':'Serie',
            'numero':'Número',
            #'cliente':'Cliente',
            #'resoluciones':'Resolución',
            'cantidad_prod':'Cantidad',
            'anulado':'Anulado',
            #'usuarios':'Usuario',
            'trans':'Tranaccion',
            'fechaanulado':'FechaAnulado',
            'subtotal':'SubTotal',
            'descuento':'Descuento',
        }
        widgets={
            'total':forms.DecimalField(attrs={'class':'form-control'}),
            'fecha':forms.DateTimeField(attrs={'class':'form-control'}),
            'serie':forms.TextInput(attrs={'class':'form-control'}),
            'numero':forms.NumberInput(attrs={'class':'form-control'}),
            # 'cliente',
            # 'resoluciones',
            'cantidad_prod':forms.NumberInput(attrs={'class':'form-control'}),
            'anulado':forms.BooleanField(attrs={'class':'form-control'}),
            # 'usuarios',
            'trans':forms.DateTimeField(attrs={'class':'form-control'}),
            'fechaanulado':forms.DateTimeField(attrs={'class':'form-control'}),
            'subtotal':forms.DecimalField(attrs={'class':'form-control'}),
            'descuento':forms.DecimalField(attrs={'class':'form-control'}),
        }