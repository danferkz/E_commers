from django.db import models
from user.models import Users
from product.models import Products

# Create your models here.
class StockUpdates(models.Model):
    update_id = models.AutoField(primary_key=True, verbose_name="ID de actualización")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Fecha")
    reason = models.TextField(verbose_name="Motivo")
    user = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name="Usuario")
    product = models.ForeignKey(Products, on_delete=models.CASCADE, verbose_name="Producto")
    
    
    class Meta:
        verbose_name = 'Actualización de stock'
        verbose_name_plural = 'Actualizaciones de stock'
        ordering = ['date', 'product', 'user']

    def _str_(self):
        return self.name  