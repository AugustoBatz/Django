"""Inventario URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


urlpatterns = [

    path('admin/', admin.site.urls),
    path('Clientes/',include(('apps.Cliente.urls','Clientes'))),
    path('Proveedores/',include(('apps.Proveedores.urls','Proveedores'))),
    path('Almacen/',include(('apps.Almacen.urls','Almacen'))),
    path('Productos/',include(('apps.Productos.urls','Productos'))),
    path('Compras/',include(('apps.Compras.urls','Compras'))),
    #path('', LoginView.as_view(template_name='index.html'), name="login"),
    #path('exit', LogoutView.as_view(), name="logout"),
    #path('usuario/registrar/',RegistrarUsuario.as_view(),name="usuario"),
    #path('reset/password_reset/',PasswordResetView.as_view(template_name='registration/password_reset_form.html',
    #email_template_name='registration/password_reset_email.html'),name='password_reset'),
    #path('reset/password_reset_done/',
     #    PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name="password_reset_done"),
    #path('reset/<slug:uidb64>/<slug:token>)/', PasswordResetConfirmView.as_view(
      #  template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    #path('reset/done/', PasswordResetCompleteView.as_view(
       # template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
    #path auth
    path('accounts/',include('django.contrib.auth.urls')),
    path('accounts/',include('apps.registration.urls')),

]
