from django.db import models

# Create your models here.
class Facturaventa(models.Model):
    id = models.BigAutoField(primary_key=True)
    total = models.DecimalField(db_column='Total', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha', blank=True, null=True)  # Field name made lowercase.
    serie = models.CharField(db_column='Serie', max_length=45, blank=True, null=True)  # Field name made lowercase.
    numero = models.CharField(db_column='Numero', max_length=45, blank=True, null=True)  # Field name made lowercase.
    cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='Cliente_id')  # Field name made lowercase.
    resoluciones = models.ForeignKey('Resoluciones', models.DO_NOTHING, db_column='Resoluciones_id')  # Field name made lowercase.
    cantidad_prod = models.IntegerField(db_column='Cantidad_Prod', blank=True, null=True)  # Field name made lowercase.
    anulado = models.IntegerField(db_column='Anulado', blank=True, null=True)  # Field name made lowercase.
    usuarios = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='Usuarios_id')  # Field name made lowercase.
    #usuarios_id1 = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='Usuarios_id1', blank=True, null=True)  # Field name made lowercase.
    trans = models.DateTimeField(db_column='Trans', blank=True, null=True)  # Field name made lowercase.
    fechaanulado = models.DateTimeField(db_column='FechaAnulado', blank=True, null=True)  # Field name made lowercase.
    subtotal = models.DecimalField(db_column='SubTotal', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    descuento = models.DecimalField(db_column='Descuento', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FacturaVenta'
