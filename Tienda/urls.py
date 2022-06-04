from django.urls import path
from Tienda.views import listar_ropa

urlpatterns = [
    path('', listar_ropa, name = 'listar_ropa')
]