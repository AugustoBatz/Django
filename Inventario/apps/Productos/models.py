from django.db import models
from apps.Almacen.models import Presentacion1,Catalogo,Unidadmedida1
# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(db_column='Nombre', max_length=45, blank=True, null=True)  # Field name made lowercase.
    existencia = models.IntegerField(db_column='Existencia',default=0, blank=True, null=True)  # Field name made lowercase.
    marca = models.CharField(db_column='Marca', max_length=45, blank=True, null=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', unique=True,max_length=45, blank=True, null=True)  # Field name made lowercase.
    stockminimo = models.IntegerField(db_column='StockMinimo', blank=True, null=True)  # Field name made lowercase.
    ganancia = models.DecimalField(db_column='Ganancia', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    unidadmedida_1 = models.ForeignKey(Unidadmedida1, models.DO_NOTHING, db_column='UnidadMedida_1_id')  # Field name made lowercase.
    presentacion_1 = models.ForeignKey(Presentacion1, models.DO_NOTHING, db_column='Presentacion_1_id')  # Field name made lowercase.
    catalogo = models.ForeignKey(Catalogo, models.DO_NOTHING, db_column='Catalogo_id')  # Field name made lowercase.
    imagen = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Producto'
    def __str__(self):
        return '{}'.format(self.nombre)

