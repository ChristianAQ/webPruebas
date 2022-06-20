from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, User


class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField("Nombre",max_length=35, null=True, blank=True)
    ap1 = models.CharField("Apellido 1",max_length=35, null=True, blank=True)
    ap2 = models.CharField("Apellido 2", max_length=35, null=True, blank=True)
    email = models.CharField("Email",max_length=25)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.PROTECT)  # requerido desde django 2.0

    def __str__(self):
        return '%s,%s,%s,%s,%s,%s' % (self.id, self.nombre, self.ap1, self.ap2, self.email, self.user)


class Registrado(models.Model):
    id = models.AutoField(primary_key=True)
    telefono = models.TextField("Telefono", null=True, blank=True)
    fecha_registro = models.DateField("Fecha Registro", null=True, blank=True)
    usuario = models.ForeignKey(Usuario, null=True, blank=True, on_delete=models.PROTECT)

    def __str__(self):
        return '%s,%s,%s,%s' % (
        self.id, self.historial, self.fecha_registro, self.usuario)


class Admin(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Registrado, null=True, blank=True, on_delete=models.PROTECT)

    def __str__(self):
        return '%s,%s' % (
        self.id, self.usuario)


class PerfilSocial(models.Model):
    id = models.AutoField(primary_key=True)
    historial_ventas= models.TextField("Historial Ventas", null=True, blank=True)
    historial_compras= models.TextField("Historial Ventas", null=True, blank=True)
    fecha_creacion = models.DateField("Fecha Creación", null=True, blank=True)
    # reseñas
    nombre = models.ForeignKey(Registrado, null=True, blank=True, on_delete=models.PROTECT)

    def __str__(self):
        return '%s,%s,%s,%s' % (
        self.nMatricula, self.historial_ventas, self.historial_compras, self.fecha_fabricacion)

class Ventas(models.Model):
    id = models.AutoField(primary_key=True)
    factura = models.DecimalField("Factura", null=True, blank=True, max_digits=5, decimal_places=2)
    usuario = models.ForeignKey(Usuario, null=True, blank=True, on_delete=models.PROTECT)
    perfilsocial = models.ForeignKey(PerfilSocial, null=True, blank=True, on_delete=models.PROTECT)
    def __str__(self):
        return '%s,%s,%s,%s' % (
        self.id, self.factura, self.usuario, self.autor)

class Compras(models.Model):
    id = models.AutoField(primary_key=True)
    factura = models.DecimalField("Factura", null=True, blank=True, max_digits=5, decimal_places=2)
    usuario = models.ForeignKey(Usuario, null=True, blank=True, on_delete=models.PROTECT)
    perfilsocial = models.ForeignKey(PerfilSocial, null=True, blank=True, on_delete=models.PROTECT)
    def __str__(self):
        return '%s,%s,%s,%s' % (
        self.id, self.factura, self.usuario, self.autor)


class Compras(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.TextField("Descripción", null=True, blank=True)
    precio = models.DecimalField("Precio", null=True, blank=True, max_digits=5, decimal_places=2)
    #imagenes
    usuario = models.ForeignKey(Usuario, null=True, blank=True, on_delete=models.PROTECT)
    perfilsocial = models.ForeignKey(PerfilSocial, null=True, blank=True, on_delete=models.PROTECT)
    def __str__(self):
        return '%s,%s,%s,%s' % (
        self.id, self.factura, self.usuario, self.autor)
