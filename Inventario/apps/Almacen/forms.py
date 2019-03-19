from django import forms
from apps.Almacen.models import Catalogo,Presentacion1,Unidadmedida1


class CatalogoForm(forms.ModelForm):
    class Meta:
        model=Catalogo
        fields=[
            'categoria',

        ]
        labels={
            'Categoria':'Categoria',
        }
        widgets={
            'Categoria':forms.TextInput(attrs={'class':'form-control'}),

        }

class UnidadForm(forms.ModelForm):
    class Meta:
        model=Unidadmedida1
        fields=[
            'medida',

        ]
        labels={
            'medida':'Unidad',
        }
        widgets={
            'medida':forms.TextInput(attrs={'class':'form-control'}),

        }
class PresentacionForm(forms.ModelForm):
    class Meta:
        model=Presentacion1
        fields=[
            'presentacion',

        ]
        labels={
            'presentacion':'Presentación',
        }
        widgets={
            'presentacion':forms.TextInput(attrs={'class':'form-control'}),

        }
