from django.shortcuts import get_object_or_404, redirect, render
import requests
from .models import Usuarios
from .form import UsuariosForm

# Create your views here.


def home(request):
    usuarios = Usuarios.objects.order_by('nome')

    return render(request, 'lista/home.html', {'usuarios': usuarios})


def create(request):
    form = UsuariosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('url_home')
 
    return render(request, 'lista/create.html', {'form': form})


def edit(request, pk):
    user = Usuarios.objects.get(pk=pk)

    form = UsuariosForm(request.POST or None, instance=user)
    if form.is_valid():
        form.save()
        return redirect('url_home')
 
    return render(request, 'lista/edit.html', {'form': form})


def delete(request, pk):
    user = Usuarios.objects.get(pk=pk)
    user.delete()
    return redirect('url_home')






