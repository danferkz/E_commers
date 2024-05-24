from django.db import models
from provider.models import Providers
from simple_history.models import HistoricalRecords

#modelo de categorias
class Categories(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nombre')
    
    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['name']
    
    def _str_(self):
        return self.name


class Products(models.Model):
    price_type_choices = (
        ('Unitario', 'Unitario'),
        ('media-docena', 'Media docena'),
        ('docena', 'Docena')
        
    )
    
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255 , verbose_name='Nombre')
    category= models.ForeignKey(Categories, on_delete=models.CASCADE,related_name='get_products',verbose_name='Categoría')
    price = models.CharField( max_length=50, choices=price_type_choices, default='Unitario', verbose_name='Tipo de precio')
      
    stock = models.IntegerField(verbose_name='Cantidad en stock')
    image = models.ImageField(upload_to='products', default='imagen_default.png', verbose_name='Imagen', blank=True, null=True)
    description = models.TextField(verbose_name='Descripción')
    proveedor = models.ForeignKey(Providers, on_delete=models.CASCADE, verbose_name='Proveedor')
    history = HistoricalRecords()
    
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['name']

    def _str_(self):
        return self.name
