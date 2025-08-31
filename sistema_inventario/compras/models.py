from django.db import models
from django.conf import settings
from catalogo.models import Producto
from proveedores.models import Proveedor

class OrdenDeCompra(models.Model):
    """
    Representa una orden de compra a un proveedor.
    """
    ESTADO_CHOICES = [
        ('PENDIENTE', 'Pendiente'),
        ('PARCIALMENTE_RECIBIDA', 'Parcialmente Recibida'),
        ('COMPLETADA', 'Completada'),
        ('CANCELADA', 'Cancelada'),
    ]

    proveedor = models.ForeignKey(Proveedor, on_delete=models.PROTECT, related_name='ordenes_compra')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_entrega_esperada = models.DateField()
    estado = models.CharField(max_length=25, choices=ESTADO_CHOICES, default='PENDIENTE')
    total = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)

    def __str__(self):
        return f"OC-{self.id} a {self.proveedor.nombre} - {self.estado}"

    class Meta:
        verbose_name = "Orden de Compra"
        verbose_name_plural = "Órdenes de Compra"
        ordering = ['-fecha_creacion']

class DetalleOrdenDeCompra(models.Model):
    """
    Representa un ítem dentro de una orden de compra.
    """
    orden_compra = models.ForeignKey(OrdenDeCompra, on_delete=models.CASCADE, related_name='detalles')
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2, help_text="Costo del producto al momento de la orden")
    subtotal = models.DecimalField(max_digits=12, decimal_places=2)

    def save(self, *args, **kwargs):
        self.subtotal = self.cantidad * self.precio_unitario
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre} @ ${self.precio_unitario}"

    class Meta:
        verbose_name = "Detalle de Orden de Compra"
        verbose_name_plural = "Detalles de Órdenes de Compra"
        unique_together = ('orden_compra', 'producto')

# Los modelos para Recepcion y Devolucion se añadirán en los siguientes pasos
# para mantener este paso enfocado en las órdenes de compra.
