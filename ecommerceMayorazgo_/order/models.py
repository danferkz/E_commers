from django.db import models
from user.models import Users

# Create your models here.
class Orders(models.Model):
    order_id = models.AutoField(primary_key=True, verbose_name='ID de orden')
    date_of_purchase = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de compra')
    order_status = models.CharField(max_length=20, verbose_name='Estado de la orden')
    user = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name='Usuario')
    
    class Meta:
        verbose_name = 'Orden'
        verbose_name_plural = 'Ordenes'

    def _str_(self):
        return self.name     