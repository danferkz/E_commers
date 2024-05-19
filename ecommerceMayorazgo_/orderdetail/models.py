from django.db import models
from orders.models import Orders
from productos.models import Products

# Create your models here.
class OrderDetails(models.Model):
    order_detail_id = models.AutoField(primary_key=True, verbose_name='ID de detalle de orden')
    quantity = models.PositiveIntegerField(verbose_name='Cantidad')
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio unitario')
    order = models.ForeignKey(Orders, on_delete=models.CASCADE, verbose_name='Orden')
    product = models.ForeignKey(Products, on_delete=models.CASCADE, verbose_name='Producto')
    
    class Meta:
        verbose_name = 'Detalle de orden'
        verbose_name_plural = 'Detalles de orden'

    def _str_(self):
        return self.name     