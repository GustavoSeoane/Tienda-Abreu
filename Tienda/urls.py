from django.urls import path
from Tienda.views import crear_accesorios, listar_accesorios, listar_ropa, crear_ropa, search_ropa, listar_championes, crear_championes, crear_accesorios, detalle_ropa, detalle_championes, detalle_accesorios

urlpatterns = [
    path('listar-ropa/', listar_ropa, name = 'listar_ropa'),
    path('crear-ropa/', crear_ropa, name = 'crear_ropa'),
    path('search-ropa/', search_ropa, name = 'search_ropa'),
    path('detalle-ropa/<int:pk>/', detalle_ropa, name = 'detalle_ropa'),      
    path('listar-championes/', listar_championes, name = 'listar_championes'),
    path('crear-championes/', crear_championes, name = 'crear_championes'),
    path('detalle-championes/<int:pk>/', detalle_championes, name = 'detalle_championes'),  
    path('listar-accesorios/', listar_accesorios, name = 'listar_accesorios'),
    path('crear-accesorios/', crear_accesorios, name = 'crear_accesorios'),
    path('detalle-accesorios/<int:pk>/', detalle_accesorios, name = 'detalle_accesorios'),   
]