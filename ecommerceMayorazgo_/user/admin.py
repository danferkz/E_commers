from django.contrib import admin
from .models import Users

# Register your models here.
admin.site.register(Users)
''''
    user_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo_electronico = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=15)
    tipo = models.CharField(max_length=20)
'''
class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'nombre', 'apellido', 'correo_electronico', 'contraseña', 'direccion', 'telefono', 'tipo')
    search_fields = ('nombre', 'apellido', 'correo_electronico', 'telefono')
    list_filter = ('tipo',)

