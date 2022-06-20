from django.contrib import admin
from Tienda.models import Marcas, Ropa, Championes, Accesorios
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

@admin.register(Marcas)
class MarcasAdmin(admin.ModelAdmin):
    list_display = ['marcas_name', 'contacto_name', 'contacto_mail' , 'descripcion', 'activo']


class RopaResources(resources.ModelResource):
    list_display = ['ropa_name', 'ropa_marca', 'ropa_color', 'ropa_precio']
    
    class Meta:
        model = Ropa  

@admin.register(Ropa)
class RopaAdmin(ImportExportModelAdmin):
    resource_class = RopaResources
    list_display = ['ropa_name', 'ropa_marca', 'ropa_color', 'ropa_precio']


class ChampionesResources(resources.ModelResource):
    list_display = ['championes_name', 'championes_marca', 'championes_color', 'championes_precio']
    
    class Meta:
        model = Championes      

@admin.register(Championes)
class ChampionesAdmin(ImportExportModelAdmin):
    resource_class = ChampionesResources
    list_display = ['championes_name', 'championes_marca', 'championes_color', 'championes_precio']

class AccesoriosResources(resources.ModelResource):
    list_display = ['accesorio_name', 'accesorio_tipo', 'accesorio_marca', 'accesorio_precio']
    
    class Meta:
        model = Accesorios  


@admin.register(Accesorios)
class AccesoriosAdmin(ImportExportModelAdmin):
    resource_class = AccesoriosResources    
    list_display = ['accesorio_name', 'accesorio_tipo', 'accesorio_marca', 'accesorio_precio']