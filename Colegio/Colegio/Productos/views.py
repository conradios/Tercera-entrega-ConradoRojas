from django.shortcuts import render
from .forms import ProductoForm
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




