# Generated by Django 2.1.7 on 2019-03-10 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Facturacompra',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('serie', models.CharField(blank=True, db_column='Serie', max_length=45, null=True)),
                ('numero', models.IntegerField(blank=True, db_column='Numero', null=True)),
                ('total', models.DecimalField(blank=True, db_column='Total', decimal_places=2, max_digits=10, null=True)),
                ('fecha', models.DateTimeField(blank=True, db_column='Fecha', null=True)),
                ('total_factura', models.DecimalField(blank=True, db_column='Total_Factura', decimal_places=2, max_digits=10, null=True)),
                ('anulado', models.IntegerField(blank=True, db_column='Anulado', null=True)),
                ('cantidad_prod', models.IntegerField(blank=True, db_column='Cantidad_Prod', null=True)),
                ('trans', models.DateTimeField(blank=True, db_column='Trans', null=True)),
                ('fechaanulado', models.DateTimeField(blank=True, db_column='FechaAnulado', null=True)),
            ],
            options={
                'db_table': 'FacturaCompra',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Lote',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nolote', models.IntegerField(blank=True, db_column='NoLote', null=True)),
                ('fecha', models.DateTimeField(blank=True, db_column='Fecha', null=True)),
                ('cantidad', models.IntegerField(blank=True, db_column='Cantidad', null=True)),
                ('costounitario', models.DecimalField(blank=True, db_column='CostoUnitario', decimal_places=2, max_digits=10, null=True)),
                ('costototal', models.DecimalField(blank=True, db_column='CostoTotal', decimal_places=2, max_digits=10, null=True)),
                ('disponible', models.IntegerField(blank=True, db_column='Disponible', null=True)),
                ('ganancia', models.DecimalField(blank=True, db_column='Ganancia', decimal_places=2, max_digits=10, null=True)),
                ('preciounitario', models.DecimalField(blank=True, db_column='PrecioUnitario', decimal_places=2, max_digits=10, null=True)),
                ('preciototal', models.DecimalField(blank=True, db_column='PrecioTotal', decimal_places=2, max_digits=10, null=True)),
                ('cantidadi', models.IntegerField(blank=True, db_column='Cantidadi', null=True)),
                ('descuento_maximo', models.DecimalField(blank=True, db_column='Descuento_Maximo', decimal_places=2, max_digits=10, null=True)),
                ('anulado', models.IntegerField(blank=True, db_column='Anulado', null=True)),
            ],
            options={
                'db_table': 'Lote',
                'managed': False,
            },
        ),
    ]