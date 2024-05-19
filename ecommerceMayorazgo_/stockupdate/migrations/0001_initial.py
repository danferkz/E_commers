# Generated by Django 5.0.4 on 2024-05-18 22:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('productos', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StockUpdates',
            fields=[
                ('update_id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID de actualización')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Fecha')),
                ('reason', models.TextField(verbose_name='Motivo')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.products', verbose_name='Producto')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.users', verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Actualización de stock',
                'verbose_name_plural': 'Actualizaciones de stock',
            },
        ),
    ]
