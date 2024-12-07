"""
URL configuration for bodegaProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from bodegaApp.views import index, productosData, productoRegistro, proveedoresData, proveedorRegistro, eliminarProductos, eliminarProveedores, editarProducto, editarProveedor, logsData

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")), # Todas las urls de autenticación
    path("", index, name="home"),
    path("usuarios/", include("bodegaApp.urls")),
    path('productos/', productosData, name='productosData'),
    path('proveedor/', proveedoresData, name='proveedoresData'),
    path('nuevoProducto/', productoRegistro, name='productoRegistro'),
    path('nuevoProveedor/', proveedorRegistro, name='proveedorRegistro'),
    path('eliminarProducto/<int:id>', eliminarProductos, name='eliminarProductos'),
    path('eliminarProveedor//<int:id>', eliminarProveedores, name='eliminarProveedores'),
    path('editarProducto/<int:id>', editarProducto, name='editarProducto'),
    path('editarProveedor/<int:id>', editarProveedor, name='editarProveedor'),
    path('logs/', logsData, name='logsData'),
]   
