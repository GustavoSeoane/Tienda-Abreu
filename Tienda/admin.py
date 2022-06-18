from django.contrib import admin
from Tienda.models import Marcas, Ropa, Championes, Accesorios

# Register your models here.

@admin.register(Marcas)
class MarcasAdmin(admin.ModelAdmin):
    list_display = ['name', 'activo']

@admin.register(Ropa)
class RopaAdmin(admin.ModelAdmin):
    list_display = ['ropa_name', 'ropa_marca', 'ropa_color', 'ropa_precio']

@admin.register(Championes)
class ChampionesAdmin(admin.ModelAdmin):
    list_display = ['championes_name', 'championes_marca', 'championes_color', 'championes_precio']

@admin.register(Accesorios)
class AccesoriosAdmin(admin.ModelAdmin):
    list_display = ['accesorio_name', 'accesorio_tipo', 'accesorio_marca', 'accesorio_precio']