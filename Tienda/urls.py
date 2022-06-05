from django.urls import path
from Tienda.views import listar_ropa, crear_ropa

urlpatterns = [
    path('listar-ropa/', listar_ropa, name = 'listar_ropa'),
    path('crear-ropa/', crear_ropa, name = 'crear_ropa')    
]