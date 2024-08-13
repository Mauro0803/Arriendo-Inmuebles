# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TipoUsuario(models.Model):
    tipo_usuario_id = models.AutoField(primary_key=True)
    tipo = models.CharField(unique=True, max_length=20)

    class Meta:
        managed = False
        db_table = 'tipo_usuario'


class Usuario(models.Model):
    rut = models.CharField(primary_key=True, max_length=20)
    nombre1 = models.CharField(max_length=20)
    nombre2 = models.CharField(max_length=20, blank=True, null=True)
    apellido1 = models.CharField(max_length=20)
    apellido2 = models.CharField(max_length=20, blank=True, null=True)
    direccion = models.CharField(max_length=20)
    telefono = models.CharField(max_length=15)
    correo = models.CharField(max_length=50)
    tipo_usuario = models.ForeignKey(TipoUsuario, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'usuario'
