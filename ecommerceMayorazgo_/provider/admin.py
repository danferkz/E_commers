from django.contrib import admin
from . models import Providers

# Register your models here.
admin.site.register(Providers)
''''
    provider_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255 , verbose_name='Nombre')
    tefono = models.CharField(max_length=20 , verbose_name='Telefono')
    correo = models.EmailField(verbose_name='Correo electronico')
'''

class ProviderAdmin(admin.ModelAdmin):
    list_display = ('provider_id', 'nombre', 'telefono', 'correo')
    search_fields = ('nombre', 'telefono', 'correo')
    list_filter = ('nombre',)