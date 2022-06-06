from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from Tienda.models import Marcas, Ropa, Championes, Accesorios
from Tienda.forms import ropa_forms,championes_forms
# Create your views here.

def listar_ropa(request):
    list_ropa = Ropa.objects.all()
    context = {'list_ropa' : list_ropa }
    return render (request, 'listar_ropa.html', context = context)

def crear_ropa(request):
    if request.method == 'GET':
        form = ropa_forms()
        context = {'form' : form}
        return render(request, 'crear_ropa.html', context=context )
    else:  
        form = ropa_forms(request.POST)
        if form.is_valid():
            new_ropa = Ropa.objects.create(
                ropa_name = form.cleaned_data['ropa_name'],
                ropa_color = form.cleaned_data['ropa_color'],
                ropa_marca = form.cleaned_data['ropa_marca'],
                ropa_precio = form.cleaned_data['ropa_precio'],
            )
            context = {'new_ropa' : new_ropa}
        return render(request, 'crear_ropa.html', context=context )


def search_ropa(request):
    print(request.GET)
    busquedaRopa = Ropa.objects.filter( ropa_name__icontains = request.GET['search'])
    context = {'busquedaRopa':busquedaRopa}
    return render(request, 'search-ropa.html', context = context)


def upload(request):
    return render(request, 'upload.html')

def listar_championes(request):
    list_championes = Championes.objects.all()
    context = {'list_championes' : list_championes }
    return render (request, 'listar_championes.html', context = context)

def crear_championes(request):
    if request.method == 'GET':
        form = championes_forms()
        context = {'form' : form}
        return render(request, 'crear_championes.html', context=context )
    else:  
        form = championes_forms(request.POST)
        if form.is_valid():
            new_championes = Championes.objects.create(
                championes_name = form.cleaned_data['championes_name'],
                championes_color = form.cleaned_data['championes_color'],
                championes_marca = form.cleaned_data['championes_marca'],
                championes_precio = form.cleaned_data['championes_precio'],
            )
            context = {'new_championes' : new_championes}
        return render(request, 'crear_championes.html', context=context )  