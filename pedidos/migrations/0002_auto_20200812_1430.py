# Generated by Django 3.1 on 2020-08-12 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0005_auto_20200812_1413'),
        ('pedidos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='item',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='productos.producto'),
        ),
    ]
