from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, DeleteView
from django.views.generic.edit import UpdateView
from django.urls import reverse
from Tienda.models import Marcas, Ropa, Championes, Accesorios
from Tienda.forms import ropa_forms,championes_forms, accesorios_forms

from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class listar_ropa(ListView):
    model = Ropa
    template_name = 'listar_ropa.html'

class crear_ropa(LoginRequiredMixin,CreateView):
    model = Ropa
    template_name = 'crear_ropa.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('detalle_ropa', kwargs = {'pk':self.object.pk})

def detalle_ropa(request, pk):
    try:
        ropa = Ropa.objects.get(id=pk)
        context = {'ropa' : ropa}
        return render(request, 'detalle_ropa.html', context=context)
    except:
        context = {'error': 'Lamentablemente no hemos podido encontrar el detalle solicitado'}
        return render(request, 'detalle_ropa.html', context=context)

class delete_ropa(LoginRequiredMixin,DeleteView):
    model = Ropa
    template_name = 'borrar_ropa.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('listar_ropa')

class ropa_actualizar(LoginRequiredMixin,UpdateView):
    model = Ropa
    template_name = 'update_ropa.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('detalle_ropa', kwargs = {'pk':self.object.pk})

def search_ropa(request):
    print(request.GET)
    palabra_busqueda = request.GET['search']
    busquedaRopa = Ropa.objects.filter( ropa_name__icontains = palabra_busqueda)
    if busquedaRopa.exists():
        context = {'busquedaRopa':busquedaRopa}
    else:
        context = {'errors': f'Lamentablemente no contamos con {palabra_busqueda} en stock.'}
    return render(request, 'search-ropa.html', context = context)

def upload(request):
    return render(request, 'upload.html')

class listar_championes(ListView):
    model = Championes
    template_name = 'listar_championes.html'

class crear_championes(LoginRequiredMixin,CreateView):
    model = Championes
    template_name = 'crear_championes.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('detalle_championes', kwargs = {'pk':self.object.pk})

def detalle_championes(request, pk):
    try:
        championes = Championes.objects.get(id=pk)
        context = {'championes' : championes}
        return render(request, 'detalle_championes.html', context=context)
    except:
        context = {'error': 'Lamentablemente no hemos podido encontrar el detalle solicitado'}
        return render(request, 'detalle_championes.html', context=context)

class delete_championes(LoginRequiredMixin,DeleteView):
    model = Championes
    template_name = 'borrar_championes.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('listar_championes')

class championes_actualizar(LoginRequiredMixin,UpdateView):
    model = Championes
    template_name = 'update_championes.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('detalle_championes', kwargs = {'pk':self.object.pk})

class listar_accesorios(ListView):
    model = Accesorios
    template_name = 'listar_accesorios.html'

class crear_accesorios(LoginRequiredMixin,CreateView):
    model = Accesorios
    template_name = 'crear_accesorio.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('detalle_accesorios', kwargs = {'pk':self.object.pk})

def detalle_accesorios(request, pk):
    try:
        accesorios = Accesorios.objects.get(id=pk)
        context = {'accesorios' : accesorios}
        return render(request, 'detalle_accesorios.html', context=context)
    except:
        context = {'error': 'Lamentablemente no hemos podido encontrar el detalle solicitado'}
        return render(request, 'detalle_accesorios.html', context=context)

class delete_accesorios(LoginRequiredMixin,DeleteView):
    model = Accesorios
    template_name = 'borrar_accesorios.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('listar_accesorios')

class accesorios_actualizar(LoginRequiredMixin,UpdateView):
    model = Accesorios
    template_name = 'update_accesorios.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('detalle_accesorios', kwargs = {'pk':self.object.pk})

   