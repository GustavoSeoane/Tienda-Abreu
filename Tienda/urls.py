from django.urls import path
from Tienda.views import crear_accesorios, listar_accesorios, listar_ropa, crear_ropa, search_product, listar_championes, crear_championes, crear_accesorios, detalle_ropa, detalle_championes, detalle_accesorios, delete_ropa, delete_championes, delete_accesorios, ropa_actualizar, championes_actualizar, accesorios_actualizar

urlpatterns = [
    path('listar-ropa/', listar_ropa.as_view(), name = 'listar_ropa'),
    path('crear-ropa/', crear_ropa.as_view(), name = 'crear_ropa'),
    path('search-product/', search_product, name = 'search_product'),
    path('detalle-ropa/<int:pk>/', detalle_ropa, name = 'detalle_ropa'),
    path('delete-ropa/<int:pk>/', delete_ropa.as_view(), name = 'delete_ropa'),
    path('update-ropa/<int:pk>/', ropa_actualizar.as_view(), name = 'ropa_actualizar'),      
    path('listar-championes/', listar_championes.as_view(), name = 'listar_championes'),
    path('crear-championes/', crear_championes.as_view(), name = 'crear_championes'),
    path('detalle-championes/<int:pk>/', detalle_championes, name = 'detalle_championes'),
    path('delete-championes/<int:pk>/', delete_championes.as_view(), name = 'delete_championes'),
    path('update-championes/<int:pk>/', championes_actualizar.as_view(), name = 'championes_actualizar'),   
    path('listar-accesorios/', listar_accesorios.as_view(), name = 'listar_accesorios'),
    path('crear-accesorios/', crear_accesorios.as_view(), name = 'crear_accesorios'),
    path('detalle-accesorios/<int:pk>/', detalle_accesorios, name = 'detalle_accesorios'),
    path('delete-accesorios/<int:pk>/', delete_accesorios.as_view(), name = 'delete_accesorios'),
    path('update-accesorios/<int:pk>/', accesorios_actualizar.as_view(), name = 'accesorios_actualizar'),     
]