from django.db import models

class Proveedor(models.Model):
    nombrev = models.CharField(db_column='NombreV', max_length=45, blank=True, null=True)  # Field name made lowercase.
    representante = models.CharField(db_column='Representante', max_length=45, blank=True, null=True)  # Field name made lowercase.
    nit = models.CharField(db_column='Nit', max_length=45, blank=True, null=True)  # Field name made lowercase.
    direccion = models.CharField(db_column='Direccion', max_length=200, blank=True, null=True)  # Field name made lowercase.
    numero = models.IntegerField(db_column='Numero', blank=True, null=True)  # Field name made lowercase.
    correo = models.CharField(db_column='Correo', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Proveedor'