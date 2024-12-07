from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from rest_framework.reverse import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from bodegaApp.models import Producto, Proveedor, Log
from bodegaApp.forms import ProductoRegistroForms, ProveedorRegistroForms

from django.urls import reverse
from django.http import HttpResponseRedirect


# Create your views here.
class SignUpView(SuccessMessageMixin, CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
    success_message = "¡Usuario creado exitosamente!"


@login_required
def index(request):
    return render(request, template_name="index.html")


def productosData(request):
    productos = Producto.objects.all()
    data = {'productos': productos}
    return render(request, 'tabla_productos.html', data)

def proveedoresData(request):
    proveedores = Proveedor.objects.all()
    data = {'proveedores': proveedores}
    return render(request, 'tabla_proveedores.html', data)

def productoRegistro(request):
    form = ProductoRegistroForms()

    if request.method == 'POST':
        form = ProductoRegistroForms(request.POST)
        if form.is_valid():
            producto = form.save()
            # Registrar el log
            Log.objects.create(event_type='ADD_PRODUCT', descripcion=f'Producto ID: {producto.id} | Producto: {producto.nombre} | Categoria: {producto.categoria} | Sector: {producto.sector} | Stock: {producto.stock} | Fecha de ingreso: {producto.fecha_ingreso} | Precio: ${producto.precio}')
            return HttpResponseRedirect(reverse('productosData'))
    data = {'form': form,
            'titulo':'Añadir Producto'
            } #Paso el formulario a la plantilla
    return render(request, 'añadir_producto.html', data)


def proveedorRegistro(request):
    form = ProveedorRegistroForms()

    if request.method == 'POST':
        form = ProveedorRegistroForms(request.POST)
        if form.is_valid():
            proveedor = form.save()
            # Registrar el log
            Log.objects.create(event_type='ADD_PROVIDER', descripcion=f'Proveedor ID: {proveedor.id} | Proveedor: {proveedor.nombre} | RUC: {proveedor.ruc} | Correo: {proveedor.correo} | Dirección: {proveedor.direccion} | Teléfono: {proveedor.telefono} | Productos: {proveedor.producto}')
            return HttpResponseRedirect(reverse('proveedoresData'))
    data = {'form': form,
            'title': 'Añadir Proveedor'}
    return render(request, 'añadir_proveedor.html', data)


def dashboard_bodeguero(request):
    productos = Producto.objects.all()  # Obtenemos todos los productos
    proveedores = Proveedor.objects.all()  # Obtenemos todos los proveedores

    return render(request, 'dashboard_bodeguero.html', {
        'productos': productos,
        'proveedores': proveedores,
    })

def eliminarProductos(request, id):
    #Buscar el producto dentro de la base de datos con el id
    producto = Producto.objects.get(id=id)
    producto.delete()
    # Registrar el log
    Log.objects.create(event_type='DELETE_PRODUCT', descripcion=f'Producto ID: {producto.id} | Producto eliminado: {producto.nombre} | Categoria: {producto.categoria} | Sector: {producto.sector} | Stock: {producto.stock} | Fecha de ingreso: {producto.fecha_ingreso} | Precio: ${producto.precio}')
    return HttpResponseRedirect(reverse('productosData'))

def eliminarProveedores(request, id):
    #Buscar el proveedor dentro de la base de datos con el id
    proveedor = Proveedor.objects.get(id=id)
    proveedor.delete()
    # Registrar el log
    Log.objects.create(event_type='DELETE_PROVIDER', descripcion=f'Proveedor ID: {proveedor.id} | Proveedor eliminado: {proveedor.nombre} | RUC: {proveedor.ruc} | Correo: {proveedor.correo} | Dirección: {proveedor.direccion} | Teléfono: {proveedor.telefono} | Productos: {proveedor.producto}')
    return HttpResponseRedirect(reverse('proveedoresData'))

def editarProducto(request, id):
    #Buscar el producto dentro de la base de datos con el id
    producto = Producto.objects.get(id=id)
    form = ProductoRegistroForms(instance=producto)

    if request.method == 'POST':
        form = ProductoRegistroForms(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            # Registrar el log
            Log.objects.create(event_type='EDIT_PRODUCT', descripcion=f'Producto ID: {producto.id} | Producto actual: {producto.nombre} | Categoria actual: {producto.categoria} | Sector actual: {producto.sector} | Stock actual: {producto.stock} | Fecha de ingreso: {producto.fecha_ingreso} | Precio actual: ${producto.precio}' )
            return HttpResponseRedirect(reverse('productosData'))
    data = {'form': form,
            'titulo': 'Editar Producto'} #Paso el formulario a la plantilla
    return render(request, 'añadir_producto.html', data)


def editarProveedor(request, id):
    #Buscar el proveedor dentro de la base de datos con el id
    proveedor = Proveedor.objects.get(id=id)
    form = ProveedorRegistroForms(instance=proveedor)

    if request.method == 'POST':
        form = ProveedorRegistroForms(request.POST, instance=proveedor)
        if form.is_valid():
            form.save()
            # Registrar el log
            Log.objects.create(event_type='EDIT_PROVIDER', descripcion=f'Proveedor ID: {proveedor.id} | Proveedor editado: {proveedor.nombre} | RUC Proveedor: {proveedor.ruc} | Correo Proveedor: {proveedor.correo} | Dirección Proveedor: {proveedor.direccion} | Teléfono Proveedor: {proveedor.telefono} | Productos: {proveedor.producto}')
            return HttpResponseRedirect(reverse('proveedoresData'))
    data = {'form': form,
            'title': 'Editar Proveedor'}
    return render(request, 'añadir_proveedor.html', data)

def logsData(request):
    logs = Log.objects.all().order_by('-created_at')
    data = {'logs':logs}
    return render(request, 'tabla_logs.html', data)
