# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-05 04:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articulo', '0003_compra'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='proveedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='compras', to='articulo.Proveedor'),
        ),
    ]
