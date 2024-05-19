from django.db import models
from proveedor.models import Providers

class Products(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255 , verbose_name='Nombre')
    price = models.FloatField(verbose_name='Precio')
    stock = models.IntegerField(verbose_name='Cantidad en stock')
    image = models.ImageField(upload_to='product_images', verbose_name='Imagen')
    description = models.TextField(verbose_name='Descripción')
    proveedor = models.ForeignKey(Providers, on_delete=models.CASCADE, verbose_name='Proveedor')
    
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def _str_(self):
        return self.name