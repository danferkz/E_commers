# Generated by Django 5.0.4 on 2024-05-24 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Providers',
            fields=[
                ('provider_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='Nombre')),
                ('phone', models.CharField(max_length=20, verbose_name='Telefono')),
                ('email', models.EmailField(max_length=254, verbose_name='Correo electronico')),
            ],
            options={
                'verbose_name': 'Proveedor',
                'verbose_name_plural': 'Proveedores',
                'ordering': ['name'],
            },
        ),
    ]
