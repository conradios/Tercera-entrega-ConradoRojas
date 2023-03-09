from django import forms

class ProductoForm(forms.Form):    
    nombre = forms.CharField(label='Nombre', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Nombre'})) 
    marca = forms.CharField(label='Marca', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Marca'}))
    descripcion = forms.EmailField(label='Descripcion', max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Descripcion'}))
    precio = forms.CharField(label='Precio', widget=forms.TextInput(attrs={'placeholder': 'Precio'}))
    

