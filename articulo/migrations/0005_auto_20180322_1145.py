# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-22 15:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articulo', '0004_auto_20180304_2325'),
    ]

    operations = [
        migrations.AddField(
            model_name='receta',
            name='insitucion',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='compra',
            name='articulos',
            field=models.ManyToManyField(blank=True, null=True, related_name='compras', to='articulo.Articulo', verbose_name='articulo_compra'),
        ),
    ]
