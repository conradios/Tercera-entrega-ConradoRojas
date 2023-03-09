from django.shortcuts import render
from django.template import loader

def base(request):

    return render(request, 'base.html', context={})

def nosotros(request):

    return render(request, 'nosotros.html', context={})

def busqueda_producto(request):
    return render(request, "busqueda_producto.html", context={})
