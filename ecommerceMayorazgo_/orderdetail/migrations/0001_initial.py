# Generated by Django 5.0.4 on 2024-05-18 22:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('orders', '0001_initial'),
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderDetails',
            fields=[
                ('order_detail_id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID de detalle de orden')),
                ('quantity', models.PositiveIntegerField(verbose_name='Cantidad')),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Precio unitario')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.orders', verbose_name='Orden')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.products', verbose_name='Producto')),
            ],
            options={
                'verbose_name': 'Detalle de orden',
                'verbose_name_plural': 'Detalles de orden',
            },
        ),
    ]
