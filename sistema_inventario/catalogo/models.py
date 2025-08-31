from django.db import models

class Categoria(models.Model):
    """
    Representa una categoría de productos en el inventario.
    """
    nombre = models.CharField(max_length=100, unique=True, help_text="Nombre de la categoría")
    descripcion = models.TextField(blank=True, null=True, help_text="Descripción de la categoría")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"


class Producto(models.Model):
    """
    Representa un producto en el inventario.
    """
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT,
        related_name='productos',
        help_text="Categoría a la que pertenece el producto"
    )
    sku = models.CharField(max_length=50, unique=True, help_text="Stock Keeping Unit (SKU) del producto")
    nombre = models.CharField(max_length=200, help_text="Nombre del producto")
    descripcion = models.TextField(blank=True, null=True, help_text="Descripción detallada del producto")
    precio_costo = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text="Precio de costo del producto"
    )
    precio_venta = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text="Precio de venta al público del producto"
    )
    stock = models.PositiveIntegerField(default=0, help_text="Cantidad de unidades en stock")
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombre} ({self.sku})"

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ['nombre']
