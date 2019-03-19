from django import forms
from apps.Cliente.models import Cliente


class ClienteForm(forms.ModelForm):
    class Meta:
        model=Cliente
        fields=[
            'nombrec',
            'apellido',
            'nit',
            'direccion',
            'numero',
            'correo',
        ]
        labels={
            'nombrec':'Nombre',
            'apellido':'Apellido',
            'nit': 'Nit',
            'direccion':'Dirección',
            'numero':'Número',
            'correo':'Correo',
        }
        widgets={
            'nombrec':forms.TextInput(attrs={'class':'form-control'}),
            'apellido':forms.TextInput(attrs={'class':'form-control'}),
            'nit':forms.TextInput(attrs={'class':'form-control'}),
            'direccion':forms.TextInput(attrs={'class':'form-control'}),
            'numero':forms.TextInput(attrs={'class':'form-control'}),
            'correo':forms.EmailInput(attrs={'class':'form-control '}),
        }
