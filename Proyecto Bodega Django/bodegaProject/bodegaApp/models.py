from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    categoria = models.CharField(max_length=100)
    fecha_ingreso = models.DateField()
    precio = models.IntegerField()
    sector = models.CharField(max_length=50)
    stock = models.IntegerField()

class Proveedor(models.Model):
    nombre = models.CharField(max_length=50)
    ruc = models.CharField(max_length=12)
    correo = models.EmailField()
    direccion = models.CharField(max_length=80)
    telefono = models.CharField(max_length=50)
    producto = models.CharField(max_length=50)

class Log(models.Model):
    EVENT_CHOICES = [
        ('ADD_PRODUCT','Agregar Producto'),
        ('ADD_PROVIDER','Agregar Proveedor'),
        ('DELETE_PRODUCT', 'Eliminar Producto'),
        ('DELETE_PROVIDER', 'Eliminar Proveedor'),
        ('EDIT_PRODUCT', 'Editar Producto'),
        ('EDIT_PROVIDER', 'Editar Proveedor'),
    ]

    event_type = models.CharField(max_length=20, choices=EVENT_CHOICES)
    descripcion = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_event_type_display()} - {self.created_at}"