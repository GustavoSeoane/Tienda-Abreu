from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.edit import UpdateView
from django.urls import reverse
from Tienda.models import Marcas, Ropa, Championes, Accesorios
from Tienda.forms import ropa_forms,championes_forms, accesorios_forms
# Create your views here.

class listar_ropa(ListView):
    model = Ropa
    template_name = 'listar_ropa.html'

def crear_ropa(request):
    if request.method == 'GET':
        form = ropa_forms()
        context = {'form' : form}
        return render(request, 'crear_ropa.html', context=context )
    else:  
        form = ropa_forms(request.POST, request.FILES)
        if form.is_valid():
            new_ropa = Ropa.objects.create(
                ropa_name = form.cleaned_data['ropa_name'],
                ropa_color = form.cleaned_data['ropa_color'],
                ropa_marca = form.cleaned_data['ropa_marca'],
                ropa_precio = form.cleaned_data['ropa_precio'],
                ropa_imagen = form.cleaned_data['ropa_imagen'],
            )
            context = {'new_ropa' : new_ropa}
        else:
            context = {'errors' : form.errors}
        return render(request, 'crear_ropa.html', context=context )

def detalle_ropa(request, pk):
    try:
        ropa = Ropa.objects.get(id=pk)
        context = {'ropa' : ropa}
        return render(request, 'detalle_ropa.html', context=context)
    except:
        context = {'error': 'Lamentablemente no hemos podido encontrar el detalle solicitado'}
        return render(request, 'detalle_ropa.html', context=context)

def delete_ropa(request, pk):
    try:
        if request.method == 'GET':
            ropa = Ropa.objects.get(id=pk)
            context = {'ropa':ropa}
        else:
            ropa = Ropa.objects.get(id=pk)
            ropa.delete()
            context = {'message':'Prenda eliminada correctamente'}
    
        return render(request, 'borrar_ropa.html', context=context)
    
    except:
        context = {'error':'El producto no existe'}
        return render(request, 'borrar_ropa.html', context=context)

class ropa_actualizar(UpdateView):
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
        form = championes_forms(request.POST, request.FILES)
        if form.is_valid():
            new_championes = Championes.objects.create(
                championes_name = form.cleaned_data['championes_name'],
                championes_color = form.cleaned_data['championes_color'],
                championes_marca = form.cleaned_data['championes_marca'],
                championes_precio = form.cleaned_data['championes_precio'],
                championes_imagen = form.cleaned_data['championes_imagen'],
            )
            context = {'new_championes' : new_championes}
        else:
            context = {'errors' : form.errors}
        return render(request, 'crear_championes.html', context=context )  

def detalle_championes(request, pk):
    try:
        championes = Championes.objects.get(id=pk)
        context = {'championes' : championes}
        return render(request, 'detalle_championes.html', context=context)
    except:
        context = {'error': 'Lamentablemente no hemos podido encontrar el detalle solicitado'}
        return render(request, 'detalle_championes.html', context=context)

def delete_championes(request, pk):
    try:
        if request.method == 'GET':
            championes = Championes.objects.get(id=pk)
            context = {'championes':championes}
        else:
            championes = Championes.objects.get(id=pk)
            championes.delete()
            context = {'message' : 'Champion eliminado correctamente!!!'}
        
        return render(request, 'borrar_championes.html', context=context)
    
    except:
        context = {'error': 'El producto que desea borrar no existe en la base, contactese con el adminsitrador'}
        return render(request, 'borrar_championes.html', context=context)

class championes_actualizar(UpdateView):
    model = Championes
    template_name = 'update_championes.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('detalle_championes', kwargs = {'pk':self.object.pk})

def listar_accesorios(request):
    list_accesorios = Accesorios.objects.all()
    context = {'list_accesorios' : list_accesorios }
    return render (request, 'listar_accesorios.html', context = context)

def crear_accesorios(request):
    if request.method == 'GET':
        form = accesorios_forms()
        context = {'form' : form}
        return render(request, 'crear_accesorio.html', context=context )
    else:  
        form = accesorios_forms(request.POST, request.FILES)
        if form.is_valid():
            new_accesorio = Accesorios.objects.create(
                accesorio_name = form.cleaned_data['accesorio_name'],
                accesorio_tipo = form.cleaned_data['accesorio_tipo'],
                accesorio_marca = form.cleaned_data['accesorio_marca'],
                accesorio_precio = form.cleaned_data['accesorio_precio'],
                accesorio_imagen = form.cleaned_data['accesorio_imagen'],
            )
            context = {'new_accesorio' : new_accesorio}
        else:
            context = {'errors' : form.errors}        
        return render(request, 'crear_accesorio.html', context=context )

def detalle_accesorios(request, pk):
    try:
        accesorios = Accesorios.objects.get(id=pk)
        context = {'accesorios' : accesorios}
        return render(request, 'detalle_accesorios.html', context=context)
    except:
        context = {'error': 'Lamentablemente no hemos podido encontrar el detalle solicitado'}
        return render(request, 'detalle_accesorios.html', context=context)

def delete_accesorios(request, pk):
    try:
        if request.method == 'GET':
            accesorios = Accesorios.objects.get(id=pk)
            context = {'accesorios':accesorios}
        else:
            accesorios = Accesorios.objects.get(id=pk)
            accesorios.delete()
            context = {'message' : 'Accesorio eliminado correctamente!!!'}
        
        return render(request, 'borrar_accesorios.html', context=context)
    
    except:
        context = {'error': 'El producto que desea borrar no existe en la base, contactese con el adminsitrador'}
        return render(request, 'borrar_accesorios.html', context=context)

class accesorios_actualizar(UpdateView):
    model = Accesorios
    template_name = 'update_accesorios.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('detalle_accesorios', kwargs = {'pk':self.object.pk})

   