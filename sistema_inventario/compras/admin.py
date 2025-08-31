from django.contrib import admin
from .models import OrdenDeCompra, DetalleOrdenDeCompra

class DetalleOrdenDeCompraInline(admin.TabularInline):
    """
    Permite la edición de los detalles de la orden de compra
    directamente en la vista de la orden de compra.
    """
    model = DetalleOrdenDeCompra
    extra = 1  # Número de formularios extra para añadir nuevos detalles
    autocomplete_fields = ['producto']  # Facilita la búsqueda de productos
    readonly_fields = ('subtotal',)

@admin.register(OrdenDeCompra)
class OrdenDeCompraAdmin(admin.ModelAdmin):
    """
    Configuración de la administración para el modelo OrdenDeCompra.
    """
    list_display = ('id', 'proveedor', 'fecha_creacion', 'estado', 'total')
    list_filter = ('estado', 'fecha_creacion', 'proveedor')
    search_fields = ('id', 'proveedor__nombre')
    date_hierarchy = 'fecha_creacion'
    ordering = ('-fecha_creacion',)
    inlines = [DetalleOrdenDeCompraInline]
    readonly_fields = ('total',)

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)
        # Recalcular el total de la orden después de guardar los detalles
        orden = form.instance
        total = sum(detalle.subtotal for detalle in orden.detalles.all())
        orden.total = total
        orden.save()

# No es necesario registrar DetalleOrdenDeCompra por separado
# ya que se gestiona a través del inline en OrdenDeCompraAdmin.
