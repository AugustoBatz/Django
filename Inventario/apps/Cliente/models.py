from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombrec = models.CharField(db_column='NombreC', max_length=45, blank=False, null=False)  # Field name made lowercase.
    apellido = models.CharField(db_column='Apellido', max_length=45, blank=False, null=False)  # Field name made lowercase.
    nit = models.CharField(db_column='Nit', max_length=45, blank=False, null=False)  # Field name made lowercase.
    direccion = models.CharField(db_column='Direccion', max_length=200, blank=False, null=False)  # Field name made lowercase.
    numero = models.IntegerField(db_column='Numero', blank=False, null=False)  # Field name made lowercase.
    correo = models.CharField(db_column='Correo', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Cliente'


