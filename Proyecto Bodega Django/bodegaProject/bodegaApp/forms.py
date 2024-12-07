from django import forms
from bodegaApp.models import Producto, Proveedor

#Clase para poder editar un producto
class ProductoRegistroForms(forms.Form):
    nombre = forms.CharField()
    categoria = forms.CharField()
    fecha_ingreso = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    precio = forms.IntegerField()
    sector = forms.CharField()
    stock = forms.IntegerField()

    nombre.widget.attrs['class'] = 'form-control'
    categoria.widget.attrs['class'] = 'form-control'
    fecha_ingreso.widget.attrs['class'] = 'form-control'
    precio.widget.attrs['class'] = 'form-control'
    sector.widget.attrs['class'] = 'form-control'
    stock.widget.attrs['class'] = 'form-control'


#Clase para registro de productos
class ProductoRegistroForms(forms.ModelForm):
    nombre = forms.CharField()
    categoria = forms.CharField()
    fecha_ingreso = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    precio = forms.IntegerField()
    sector = forms.CharField()
    stock = forms.IntegerField()

    nombre.widget.attrs['class'] = 'form-control'
    categoria.widget.attrs['class'] = 'form-control'
    fecha_ingreso.widget.attrs['class'] = 'form-control'
    precio.widget.attrs['class'] = 'form-control'
    sector.widget.attrs['class'] = 'form-control'
    stock.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Producto
        fields = '__all__'


#Clase para poder editar un proveedor
class ProveedorRegistroForms(forms.Form):
    nombre = forms.CharField()
    ruc = forms.CharField()
    correo = forms.CharField()
    direccion = forms.CharField()
    telefono = forms.CharField()
    producto = forms.CharField()

    nombre.widget.attrs['class'] = 'form-control'
    ruc.widget.attrs['class'] = 'form-control'
    correo.widget.attrs['class'] = 'form-control'
    direccion.widget.attrs['class'] = 'form-control'
    telefono.widget.attrs['class'] = 'form-control'
    producto.widget.attrs['class'] = 'form-control'


#Clase para registro de proveedores
class ProveedorRegistroForms(forms.ModelForm):
    nombre = forms.CharField()
    ruc = forms.CharField()
    correo = forms.CharField()
    direccion = forms.CharField()
    telefono = forms.CharField()
    producto = forms.CharField()

    nombre.widget.attrs['class'] = 'form-control'
    ruc.widget.attrs['class'] = 'form-control'
    correo.widget.attrs['class'] = 'form-control'
    direccion.widget.attrs['class'] = 'form-control'
    telefono.widget.attrs['class'] = 'form-control'
    producto.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Proveedor
        fields = '__all__'


