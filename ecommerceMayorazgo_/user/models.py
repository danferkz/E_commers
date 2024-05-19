from django.db import models

# Create your models here.
class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name="Nombre")
    last_name = models.CharField(max_length=100, verbose_name="Apellido")
    email = models.EmailField(unique=True, verbose_name="Correo electrónico")
    password = models.CharField(max_length=100, verbose_name="Contraseña")
    address = models.CharField(max_length=255, verbose_name="Dirección")
    phone = models.CharField(max_length=15, verbose_name="Teléfono")
    type = models.CharField(max_length=20, verbose_name="Tipo")
    
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def _str_(self):
        return self.name     