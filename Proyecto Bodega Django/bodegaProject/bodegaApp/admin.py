from django.contrib import admin
from bodegaApp.models import Producto, Proveedor

# Register your models here.
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id','nombre','categoria','fecha_ingreso','precio','sector','stock')

class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('id','nombre','ruc','correo','direccion','telefono','producto')


admin.site.register(Producto, ProductoAdmin)
admin.site.register(Proveedor, ProveedorAdmin)