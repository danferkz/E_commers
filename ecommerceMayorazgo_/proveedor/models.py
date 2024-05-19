from django.db import models
#from productos.models import Product

# Create your models here.
class Providers(models.Model):
    provider_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255 , verbose_name='Nombre')
    phone = models.CharField(max_length=20 , verbose_name='Telefono')
    email = models.EmailField(verbose_name='Correo electronico')
    #product = models.OneToOneField(Product, on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'

    def _str_(self):
        return self.name 