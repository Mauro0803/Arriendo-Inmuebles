from django.db import models


class Comuna(models.Model):
    com_id = models.AutoField(primary_key=True)
    com_comuna = models.CharField(unique=True, max_length=20)

    class Meta:
        managed = False
        db_table = 'comuna'


class Tipo_Inmueble(models.Model):
    ti_id = models.AutoField(primary_key=True)
    ti_tipo = models.CharField(unique=True, max_length=20)

    class Meta:
        managed = False
        db_table = 'tipo_inmueble'


class Region(models.Model):
    reg_id = models.AutoField(primary_key=True)
    reg_region = models.CharField(unique=True, max_length=20)

    class Meta:
        managed = False
        db_table = 'region'


class Inmueble(models.Model):
    inm_id = models.AutoField(primary_key=True)
    inm_nombre = models.CharField(max_length=50)
    inm_descripcion = models.TextField(blank=True, null=True)
    inm_m2_construidos = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    inm_m2_totales = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    inm_estacionamientos = models.IntegerField(blank=True, null=True)
    inm_habitaciones = models.IntegerField(blank=True, null=True)
    inm_banos = models.IntegerField(blank=True, null=True)
    inm_direccion = models.CharField(max_length=30, blank=True, null=True)
    inm_precio = models.IntegerField(blank=True, null=True)
    fk_com = models.ForeignKey(Comuna, on_delete=models.DO_NOTHING, blank=True, null=True)
    fk_reg = models.ForeignKey(Region, on_delete=models.DO_NOTHING, blank=True, null=True)
    fk_ti = models.ForeignKey(Tipo_Inmueble, on_delete=models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inmueble'


class Tipo_Usuario(models.Model):
    tu_id = models.AutoField(primary_key=True)
    tu_tipo = models.CharField(unique=True, max_length=20)

    class Meta:
        managed = False
        db_table = 'tipo_usuario'


class Usuario(models.Model):
    usu_rut = models.CharField(primary_key=True, max_length=9)
    usu_nombre1 = models.CharField(max_length=20)
    usu_nombre2 = models.CharField(max_length=20, blank=True, null=True)
    usu_apellido1 = models.CharField(max_length=20)
    usu_apellido2 = models.CharField(max_length=20, blank=True, null=True)
    usu_direccion = models.CharField(max_length=30)
    usu_telefono = models.CharField(max_length=15)
    usu_correo = models.CharField(max_length=50)
    fk_tu = models.ForeignKey(Tipo_Usuario, on_delete=models.DO_NOTHING, blank=True, null=True)
    fk_inm = models.ForeignKey(Inmueble, on_delete=models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuario'