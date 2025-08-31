from django.contrib import admin
from .models import Categoria, Producto

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    """
    Configuración de la administración para el modelo Categoria.
    """
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre',)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    """
    Configuración de la administración para el modelo Producto.
    """
    list_display = ('nombre', 'sku', 'categoria', 'precio_venta', 'stock', 'fecha_actualizacion')
    list_filter = ('categoria',)
    search_fields = ('nombre', 'sku')
    ordering = ('nombre',)
    list_per_page = 20
