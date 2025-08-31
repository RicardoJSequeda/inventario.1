from django.db import models

class Proveedor(models.Model):
    """
    Representa un proveedor de productos.
    """
    nombre = models.CharField(max_length=200, unique=True, help_text="Nombre o razón social del proveedor")
    rfc = models.CharField(max_length=13, blank=True, null=True, unique=True, help_text="Registro Federal de Contribuyentes del proveedor")
    direccion = models.TextField(blank=True, null=True, help_text="Dirección física del proveedor")
    telefono = models.CharField(max_length=20, blank=True, null=True, help_text="Número de teléfono de contacto")
    email = models.EmailField(blank=True, null=True, help_text="Correo electrónico de contacto")
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"
        ordering = ['nombre']


class Cliente(models.Model):
    """
    Representa un cliente. Opcional según la solicitud inicial.
    """
    nombre = models.CharField(max_length=200, help_text="Nombre o razón social del cliente")
    rfc = models.CharField(max_length=13, blank=True, null=True, unique=True, help_text="Registro Federal de Contribuyentes del cliente")
    direccion = models.TextField(blank=True, null=True, help_text="Dirección de envío o fiscal del cliente")
    telefono = models.CharField(max_length=20, blank=True, null=True, help_text="Número de teléfono de contacto")
    email = models.EmailField(blank=True, null=True, help_text="Correo electrónico de contacto")
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ['nombre']
