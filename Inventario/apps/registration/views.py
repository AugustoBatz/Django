
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import UserCreateFormWithEmail
from django import forms
class SignUpview(CreateView):
    form_class = UserCreateFormWithEmail

    template_name = 'registration/signup.html'
    def get_success_url(self):
        return reverse_lazy('login')+'?register'
    def get_form(self, form_class=None):
        form=super(SignUpview,self).get_form()
        #modificar en tiempo real
        form.fields['username'].widget=forms.TextInput(attrs={'class':'form-control mb-2','placeholder':'Nombre de usuario'} )
        form.fields['email'].widget=forms.EmailInput(attrs={'class':'form-control mb-2','placeholder':'Dirección de Correo'} )
        form.fields['password1'].widget=forms.PasswordInput(attrs={'class':'form-control mb-2','placeholder':'Contraseña'} )
        form.fields['password2'].widget=forms.PasswordInput(attrs={'class':'form-control mb-2','placeholder':'Repita Contraseña '} )

        return form
# Create your views here.
