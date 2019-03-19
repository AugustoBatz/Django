from django.db import models
from apps.Proveedores.models import Proveedor
from apps.Productos.models import Producto

class Facturacompra(models.Model):
    id = models.BigAutoField(primary_key=True)
    serie = models.CharField(db_column='Serie', max_length=45, blank=True, null=True)  # Field name made lowercase.
    numero = models.IntegerField(db_column='Numero', blank=True, null=True)  # Field name made lowercase.
    total = models.DecimalField(db_column='Total', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    proveedor = models.ForeignKey(Proveedor, models.DO_NOTHING, db_column='Proveedor_id')  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha', blank=True, null=True)  # Field name made lowercase.
    total_factura = models.DecimalField(db_column='Total_Factura', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    anulado = models.IntegerField(db_column='Anulado', blank=True, null=True)  # Field name made lowercase.
    cantidad_prod = models.IntegerField(db_column='Cantidad_Prod', blank=True, null=True)  # Field name made lowercase.
    #usuarios = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='Usuarios_id')  # Field name made lowercase.
   # usuarios_id1 = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='Usuarios_id1', blank=True, null=True)  # Field name made lowercase.
    trans = models.DateTimeField(db_column='Trans', blank=True, null=True)  # Field name made lowercase.
    fechaanulado = models.DateTimeField(db_column='FechaAnulado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FacturaCompra'


class Lote(models.Model):
    id = models.BigAutoField(primary_key=True)
    nolote = models.IntegerField(db_column='NoLote', blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha', blank=True, null=True)  # Field name made lowercase.
    cantidad = models.IntegerField(db_column='Cantidad', blank=True, null=True)  # Field name made lowercase.
    costounitario = models.DecimalField(db_column='CostoUnitario', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    producto = models.ForeignKey(Producto, models.DO_NOTHING, db_column='Producto_id')  # Field name made lowercase.
    costototal = models.DecimalField(db_column='CostoTotal', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    disponible = models.IntegerField(db_column='Disponible', blank=True, null=True)  # Field name made lowercase.
    ganancia = models.DecimalField(db_column='Ganancia', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    preciounitario = models.DecimalField(db_column='PrecioUnitario', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    preciototal = models.DecimalField(db_column='PrecioTotal', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    facturacompra = models.ForeignKey(Facturacompra, models.DO_NOTHING, db_column='FacturaCompra_id')  # Field name made lowercase.
    cantidadi = models.IntegerField(db_column='Cantidadi', blank=True, null=True)  # Field name made lowercase.
    descuento_maximo = models.DecimalField(db_column='Descuento_Maximo', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    anulado = models.IntegerField(db_column='Anulado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Lote'

