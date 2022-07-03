from django.shortcuts import render,redirect

from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import authenticate, login, logout

from users.forms import User_registration_form

from django.urls import reverse

from django.views.generic import DetailView, UpdateView
from users.models import User_profile
# Create your views here.

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                context = {'message':f'Bienvenido {username}.'}
                return render(request, 'index.html', context=context)
            else:
                context = {'errors':'No hay ningun usuarios registrado con esas credenciales'}
                form = AuthenticationForm()
                return render(request, 'auth/login.html',context=context)
        else:
            errors = form.errors
            form = AuthenticationForm()
            context = {'errors':errors,'form':form}
            return render(request, 'auth/login.html',context=context)
    else:
        form = AuthenticationForm()
        context = {'form':form}
        return render(request, 'auth/login.html',context=context)

def logout_view(request):
    logout(request)
    return redirect('index')

def register_view(request):
    if request.method == 'POST':
        form = User_registration_form(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            login(request, user)
            context = {'message':f'Usuario creado satisfactoriamente. Bienvenido {username}'}
            return render(request, 'index.html',context = context)
        else:
            errors = form.errors
            form = User_registration_form()
            context = {'errors':errors, 'form':form}
            return render(request,'auth/register.html',context = context)
    else:
        form = User_registration_form()
        context = {'form':form}
        return render(request,'auth/register.html',context = context)

class Detail_user_profile(DetailView):
    model = User_profile
    template_name= 'auth/detail_user_profile.html'

class Update_user_profile(UpdateView):
    model = User_profile
    template_name = 'auth/update_user_profile.html'
    fields = ['phone', 'profile_imagen']

    def get_success_url(self):
        return reverse('detail_user_profile', kwargs = {'pk':self.object.pk})

