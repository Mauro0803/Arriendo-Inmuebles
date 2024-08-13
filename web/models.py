from django.db import models

class TipoUsuario(models.Model):
    tipo_usuario_id = models.AutoField(primary_key=True)
    tipo = models.CharField(unique=True, max_length=20)

    class Meta:
        managed = False
        db_table = 'tipo_usuario'

class Usuario(models.Model):
    rut = models.CharField(primary_key=True, max_length=9)
    nombre1 = models.CharField(max_length=20)
    nombre2 = models.CharField(max_length=20, blank=True, null=True)
    apellido1 = models.CharField(max_length=20)
    apellido2 = models.CharField(max_length=20, blank=True, null=True)
    direccion = models.CharField(max_length=30)
    telefono = models.CharField(max_length=15)
    correo = models.CharField(max_length=50)
    tipo_usuario = models.ForeignKey(TipoUsuario, on_delete=models.DO_NOTHING, null=True, blank=True)
    # 1. ForeignKey (Relación Uno a Muchos):
    # Uso: Cuando un usuario pertenece a un solo tipo de usuario, pero un tipo de usuario puede estar asociado con muchos usuarios.
    # Ejemplo: Muchos usuarios pueden ser "Arrendador", pero el usuario SOLO puede ser "Arrendador"

    class Meta:
        managed = False
        db_table = 'usuario'



# El uso de ManyToManyField o OneToOneField depende de la relación entre las tablas Usuario y TipoUsuario. Vamos a analizar cuándo es más adecuado utilizar cada uno:


# Implementación Actual: Esto es lo que estás utilizando actualmente en tu modelo, y es apropiado si esta es la relación que deseas modelar.
# 2. OneToOneField (Relación Uno a Uno):
# Uso: Cuando cada usuario debe estar asociado exactamente con un solo tipo de usuario, y viceversa.
# Ejemplo: Si cada usuario tiene un tipo de usuario único, que no se comparte con ningún otro usuario.
# Implementación: Cambiarías el ForeignKey a OneToOneField en tu modelo de Usuario.
