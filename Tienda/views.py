from django.shortcuts import render
from Tienda.models import Marcas, Ropa, Championes, Accesorios
# Create your views here.

def listar_ropa(request):
    list_ropa = Ropa.objects.all()
    context = {'list_ropa' : list_ropa }
    return render (request, 'listar_ropa.html', context = context)


def upload(request):
    return render(request, 'upload.html')