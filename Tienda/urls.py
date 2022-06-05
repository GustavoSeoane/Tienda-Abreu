from django.urls import path
from Tienda.views import listar_ropa, crear_ropa, listar_championes, crear_championes

urlpatterns = [
    path('listar-ropa/', listar_ropa, name = 'listar_ropa'),
    path('crear-ropa/', crear_ropa, name = 'crear_ropa'),    
    path('listar-championes/', listar_championes, name = 'listar_championes'),
    path('crear-championes/', crear_championes, name = 'crear_championes'),
]