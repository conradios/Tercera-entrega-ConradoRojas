from django.shortcuts import render
from .forms import ProductoForm
from django.http import HttpResponse

# Create your views here.

def Productos(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)

        print(form)

        if (form.is_valid()):
            info = form.cleaned_data

            Productos = Productos(nombre=info['nombre'],
                                  marca=info['marca'],
                                  descripcion=info['descripcion'],
                                  precio=info['precio'])
            
            Productos.save()

            return render(request, 'Productos.html')
        
    else:
        form = ProductoForm()

    return render(request, 'Productos.html', {'form': form})


def buscar (request):

    if request.GET["produ"]:

        producto = request.GET["produ"]
    
        productos = Productos.objects.filter(nombre__icontains=producto)

        return render(request, "busqueda_producto.html", {"articulos": productos, "query":producto})

    else:

        mensaje = "No introduciste un texto valido"

    return HttpResponse(mensaje)