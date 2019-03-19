from django.db import models

class Catalogo(models.Model):
    categoria = models.CharField(db_column='Categoria', max_length=45,unique=True, blank=False, null=False)  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'Catalogo'
    def __str__(self):
        return '{}'.format(self.categoria)

class Presentacion1(models.Model):
    presentacion = models.TextField(db_column='Presentacion', max_length=45,unique=True, blank=False, null=False)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Presentacion_1'
    def __str__(self):
        return '{}'.format(self.presentacion)

class Unidadmedida1(models.Model):
    medida = models.TextField(db_column='Medida', max_length=45, unique=True,blank=False, null=False)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UnidadMedida_1'

    def __str__(self):
        return '{}'.format(self.medida)

