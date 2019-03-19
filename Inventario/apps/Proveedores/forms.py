from apps.Proveedores.models import Proveedor
from django import forms

class ProveedorForm(forms.ModelForm):
    class Meta:
        model=Proveedor
        fields=[
            'nombrev',
            'representante',
            'nit',
            'direccion',
            'numero',
            'correo',
        ]
        labels={
            'nombrev':'Proveedor',
            'representante':'Representante',
            'nit': 'Nit',
            'direccion':'Dirección',
            'numero':'Número',
            'correo':'Correo',
        }
        widgets={
            'nombrev':forms.TextInput(attrs={'class':'form-control'}),
            'representante':forms.TextInput(attrs={'class':'form-control'}),
            'nit':forms.TextInput(attrs={'class':'form-control'}),
            'direccion':forms.TextInput(attrs={'class':'form-control'}),
            'numero':forms.TextInput(attrs={'class':'form-control'}),
            'correo':forms.EmailInput(attrs={'class':'form-control '}),
        }
