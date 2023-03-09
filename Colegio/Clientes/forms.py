from django import forms

class ClienteForm(forms.Form):    
    nombre = forms.CharField(label='Nombre', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Nombre'})) 
    apellido = forms.CharField(label='Apellido', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Apellido'}))
    email = forms.EmailField(label='Email', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    direccion = forms.CharField(label='Direccion', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Direccion'}))
