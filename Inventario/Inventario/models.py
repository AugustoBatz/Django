# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Catalogo(models.Model):
    categoria = models.CharField(db_column='Categoria', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Catalogo'


class Cliente(models.Model):
    nombrec = models.CharField(db_column='NombreC', max_length=45, blank=True, null=True)  # Field name made lowercase.
    apellido = models.CharField(db_column='Apellido', max_length=45, blank=True, null=True)  # Field name made lowercase.
    nit = models.CharField(db_column='Nit', max_length=45, blank=True, null=True)  # Field name made lowercase.
    direccion = models.CharField(db_column='Direccion', max_length=200, blank=True, null=True)  # Field name made lowercase.
    numero = models.IntegerField(db_column='Numero', blank=True, null=True)  # Field name made lowercase.
    correo = models.CharField(db_column='Correo', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Cliente'


class Cuentas(models.Model):
    id = models.IntegerField(primary_key=True)
    inventario = models.DecimalField(db_column='Inventario', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    compras = models.DecimalField(db_column='Compras', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ventas = models.DecimalField(db_column='Ventas', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Cuentas'


class Facturacompra(models.Model):
    id = models.BigAutoField(primary_key=True)
    serie = models.CharField(db_column='Serie', max_length=45, blank=True, null=True)  # Field name made lowercase.
    numero = models.IntegerField(db_column='Numero', blank=True, null=True)  # Field name made lowercase.
    total = models.DecimalField(db_column='Total', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    proveedor = models.ForeignKey('Proveedor', models.DO_NOTHING, db_column='Proveedor_id')  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha', blank=True, null=True)  # Field name made lowercase.
    total_factura = models.DecimalField(db_column='Total_Factura', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    anulado = models.IntegerField(db_column='Anulado', blank=True, null=True)  # Field name made lowercase.
    cantidad_prod = models.IntegerField(db_column='Cantidad_Prod', blank=True, null=True)  # Field name made lowercase.
  #  usuarios = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='Usuarios_id')  # Field name made lowercase.
   # usuarios_id1 = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='Usuarios_id1', blank=True, null=True)  # Field name made lowercase.
    trans = models.DateTimeField(db_column='Trans', blank=True, null=True)  # Field name made lowercase.
    fechaanulado = models.DateTimeField(db_column='FechaAnulado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FacturaCompra'


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
    usuarios_id1 = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='Usuarios_id1', blank=True, null=True)  # Field name made lowercase.
    trans = models.DateTimeField(db_column='Trans', blank=True, null=True)  # Field name made lowercase.
    fechaanulado = models.DateTimeField(db_column='FechaAnulado', blank=True, null=True)  # Field name made lowercase.
    subtotal = models.DecimalField(db_column='SubTotal', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    descuento = models.DecimalField(db_column='Descuento', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FacturaVenta'


class Lote(models.Model):
    id = models.BigAutoField(primary_key=True)
    nolote = models.IntegerField(db_column='NoLote', blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha', blank=True, null=True)  # Field name made lowercase.
    cantidad = models.IntegerField(db_column='Cantidad', blank=True, null=True)  # Field name made lowercase.
    costounitario = models.DecimalField(db_column='CostoUnitario', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='Producto_id')  # Field name made lowercase.
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


class Loteventa(models.Model):
    id = models.BigAutoField(primary_key=True)
    nolote = models.IntegerField(db_column='NoLote', blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha', blank=True, null=True)  # Field name made lowercase.
    cantidad = models.IntegerField(db_column='Cantidad', blank=True, null=True)  # Field name made lowercase.
    preciounitario = models.DecimalField(db_column='PrecioUnitario', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    preciototal = models.DecimalField(db_column='PrecioTotal', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='Producto_id')  # Field name made lowercase.
    facturaventa = models.ForeignKey(Facturaventa, models.DO_NOTHING, db_column='FacturaVenta_id')  # Field name made lowercase.
    costounitario = models.DecimalField(db_column='CostoUnitario', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    costototal = models.DecimalField(db_column='CostoTotal', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    descuento_maximo = models.DecimalField(db_column='Descuento_Maximo', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    anulado = models.IntegerField(db_column='Anulado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LoteVenta'


class Notacredito(models.Model):
    facturacompra = models.ForeignKey(Facturacompra, models.DO_NOTHING, db_column='FacturaCompra_id', blank=True, null=True)  # Field name made lowercase.
    usuarios = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='Usuarios_id')  # Field name made lowercase.
    no_nota = models.CharField(db_column='No Nota', max_length=45, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fecha = models.DateTimeField(db_column='Fecha', blank=True, null=True)  # Field name made lowercase.
    proveedor = models.ForeignKey('Proveedor', models.DO_NOTHING, db_column='Proveedor_id')  # Field name made lowercase.
    total = models.DecimalField(db_column='Total', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NotaCredito'


class Presentacion1(models.Model):
    presentacion = models.CharField(db_column='Presentacion', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Presentacion_1'


class Producto(models.Model):
    nombre = models.CharField(db_column='Nombre', max_length=45, blank=True, null=True)  # Field name made lowercase.
    existencia = models.IntegerField(db_column='Existencia', blank=True, null=True)  # Field name made lowercase.
    marca = models.CharField(db_column='Marca', max_length=45, blank=True, null=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=45, blank=True, null=True)  # Field name made lowercase.
    stockminimo = models.IntegerField(db_column='StockMinimo', blank=True, null=True)  # Field name made lowercase.
    ganancia = models.DecimalField(db_column='Ganancia', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    unidadmedida_1 = models.ForeignKey('Unidadmedida1', models.DO_NOTHING, db_column='UnidadMedida_1_id')  # Field name made lowercase.
    presentacion_1 = models.ForeignKey(Presentacion1, models.DO_NOTHING, db_column='Presentacion_1_id')  # Field name made lowercase.
    catalogo = models.ForeignKey(Catalogo, models.DO_NOTHING, db_column='Catalogo_id')  # Field name made lowercase.
    imagen = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Producto'


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


class Resoluciones(models.Model):
    serie = models.CharField(db_column='Serie', max_length=45)  # Field name made lowercase.
    rangoi = models.IntegerField(db_column='RangoI')  # Field name made lowercase.
    nor = models.CharField(db_column='NoR', max_length=30)  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.
    incremento = models.IntegerField(db_column='INCREMENTO')  # Field name made lowercase.
    rangof = models.IntegerField(db_column='RangoF')  # Field name made lowercase.
    activo = models.IntegerField(db_column='Activo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Resoluciones'


class Unidadmedida1(models.Model):
    medida = models.CharField(db_column='Medida', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UnidadMedida_1'


class Usuarios(models.Model):
    nombre = models.CharField(db_column='Nombre', max_length=45, blank=True, null=True)  # Field name made lowercase.
    apellido = models.CharField(db_column='Apellido', max_length=45, blank=True, null=True)  # Field name made lowercase.
    usuario = models.CharField(db_column='Usuario', max_length=45, blank=True, null=True)  # Field name made lowercase.
    contraseña = models.CharField(db_column='Contraseña', max_length=45, blank=True, null=True)  # Field name made lowercase.
    privilegios = models.CharField(db_column='Privilegios', max_length=45, blank=True, null=True)  # Field name made lowercase.
    dpi = models.IntegerField(db_column='DPI', blank=True, null=True)  # Field name made lowercase.
    activo = models.IntegerField(db_column='Activo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Usuarios'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
