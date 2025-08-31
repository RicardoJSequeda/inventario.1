from django.contrib import admin
from .models import Proveedor, Cliente

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    """
    Configuración de la administración para el modelo Proveedor.
    """
    list_display = ('nombre', 'rfc', 'telefono', 'email')
    search_fields = ('nombre', 'rfc')
    ordering = ('nombre',)

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    """
    Configuración de la administración para el modelo Cliente.
    """
    list_display = ('nombre', 'rfc', 'telefono', 'email')
    search_fields = ('nombre', 'rfc')
    ordering = ('nombre',)
