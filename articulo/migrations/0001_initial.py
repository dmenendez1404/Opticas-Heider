# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-07 04:12
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=75)),
                ('codigo', models.CharField(blank=True, max_length=12, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=150)),
                ('precio', models.FloatField(blank=True, default=1)),
                ('cantidad', models.IntegerField(blank=True, default=1)),
                ('activo', models.BooleanField()),
                ('pendiente', models.BooleanField()),
                ('foto', models.ImageField(blank=True, upload_to='articulos/')),
                ('bar_code', models.ImageField(blank=True, upload_to='articulos/barcodes/')),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('siglas', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=75)),
                ('descripcion', models.CharField(max_length=75)),
                ('siglas', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='MaterialArmadura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=75)),
                ('descripcion', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='MaterialCristal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=75)),
                ('descripcion', models.CharField(max_length=75)),
                ('siglas', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='MaterialSol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material', models.CharField(max_length=75)),
            ],
        ),
        migrations.CreateModel(
            name='Medicion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('esfera', models.FloatField()),
                ('cilindro', models.FloatField()),
                ('eje', models.FloatField()),
                ('prisma', models.FloatField()),
                ('altura', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Modelo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=75)),
                ('descripcion', models.CharField(max_length=75)),
                ('siglas', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_nacimiento', models.DateField()),
                ('CI', models.CharField(max_length=15)),
                ('telefono', models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=20)),
                ('apellidos', models.CharField(blank=True, max_length=50)),
                ('fecha_nacimiento', models.DateField(blank=True)),
                ('CI', models.CharField(blank=True, max_length=15)),
                ('direccion', models.CharField(blank=True, max_length=150)),
                ('telefono', models.CharField(blank=True, max_length=11)),
                ('email', models.EmailField(blank=True, max_length=100)),
                ('activo', models.BooleanField()),
                ('foto', models.ImageField(null=True, upload_to='proveedores/')),
            ],
        ),
        migrations.CreateModel(
            name='Receta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
                ('fecha', models.DateField()),
                ('atendida', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=75)),
                ('direccion', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='TipoArmazon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=120)),
                ('descripcion', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='TipoMontura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=75)),
                ('descripcion', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='TratamientoCristal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=75)),
                ('descripcion', models.CharField(max_length=75)),
                ('siglas', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('subtotal', models.FloatField()),
                ('descuento', models.FloatField()),
                ('total', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Accesorio',
            fields=[
                ('articulo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='articulo.Articulo')),
                ('tipo', models.CharField(blank=True, max_length=50)),
            ],
            bases=('articulo.articulo',),
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('persona_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='articulo.Persona')),
                ('diagnostico', models.CharField(max_length=50)),
                ('observaciones', models.CharField(max_length=75)),
                ('foto', models.ImageField(null=True, upload_to='clientes/')),
            ],
            bases=('articulo.persona',),
        ),
        migrations.CreateModel(
            name='CristalGraduado',
            fields=[
                ('articulo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='articulo.Articulo')),
                ('laboratorio', models.BooleanField()),
                ('color', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='articulo.Color')),
                ('material_cristal', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='articulo.MaterialCristal')),
                ('medicion_cerca', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='medicion_cerca', to='articulo.Medicion')),
                ('medicion_lejos', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='medicion_lejos', to='articulo.Medicion')),
                ('modelo', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='articulo.Modelo')),
                ('tratamientos', models.ManyToManyField(blank=True, to='articulo.TratamientoCristal')),
            ],
            bases=('articulo.articulo',),
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('persona_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='articulo.Persona')),
                ('codigo', models.IntegerField()),
                ('cargo', models.CharField(max_length=15)),
                ('foto', models.ImageField(null=True, upload_to='doctores/')),
            ],
            bases=('articulo.persona',),
        ),
        migrations.CreateModel(
            name='Espejuelo',
            fields=[
                ('articulo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='articulo.Articulo')),
                ('calibre', models.IntegerField(blank=True)),
                ('puente', models.IntegerField(blank=True)),
            ],
            bases=('articulo.articulo',),
        ),
        migrations.CreateModel(
            name='GafaSol',
            fields=[
                ('articulo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='articulo.Articulo')),
                ('color', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='articulo.Color')),
                ('marca', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='articulo.Marca')),
                ('material_armadura', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='articulo.MaterialArmadura')),
                ('material_sol', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='articulo.MaterialSol')),
                ('tipo_armazon', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='articulo.TipoArmazon')),
                ('tipo_montura', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='articulo.TipoMontura')),
            ],
            bases=('articulo.articulo',),
        ),
        migrations.CreateModel(
            name='LenteContacto',
            fields=[
                ('articulo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='articulo.Articulo')),
                ('blando', models.BooleanField()),
                ('gas_permeable', models.BooleanField()),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articulo.Color')),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articulo.Marca')),
                ('medicion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articulo.Medicion')),
            ],
            bases=('articulo.articulo',),
        ),
        migrations.AddField(
            model_name='venta',
            name='articulos',
            field=models.ManyToManyField(related_name='ventas', to='articulo.Articulo'),
        ),
        migrations.AddField(
            model_name='venta',
            name='sucursal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articulo.Sucursal'),
        ),
        migrations.AddField(
            model_name='receta',
            name='sucursal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articulo.Sucursal'),
        ),
        migrations.AddField(
            model_name='receta',
            name='venta',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='recetas', to='articulo.Venta'),
        ),
        migrations.AddField(
            model_name='proveedor',
            name='articulos',
            field=models.ManyToManyField(blank=True, related_name='proveedores', to='articulo.Articulo'),
        ),
        migrations.AddField(
            model_name='proveedor',
            name='sucursal',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='articulo.Sucursal'),
        ),
        migrations.AddField(
            model_name='persona',
            name='sucursal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articulo.Sucursal'),
        ),
        migrations.AddField(
            model_name='persona',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='articulo',
            name='sucursal',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='articulos', to='articulo.Sucursal'),
        ),
        migrations.CreateModel(
            name='EspejueloGraduado',
            fields=[
                ('espejuelo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='articulo.Espejuelo')),
                ('cristalDer', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='cristalDer', to='articulo.CristalGraduado')),
                ('cristalIzq', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='cristalIzq', to='articulo.CristalGraduado')),
            ],
            bases=('articulo.espejuelo',),
        ),
        migrations.AddField(
            model_name='venta',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ventas', to='articulo.Cliente'),
        ),
        migrations.AddField(
            model_name='receta',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articulo.Cliente'),
        ),
        migrations.AddField(
            model_name='receta',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articulo.Doctor'),
        ),
        migrations.AddField(
            model_name='receta',
            name='lente_contacto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lente_contacto_receta', to='articulo.LenteContacto'),
        ),
        migrations.AddField(
            model_name='espejuelo',
            name='color',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='articulo.Color'),
        ),
        migrations.AddField(
            model_name='espejuelo',
            name='marca',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='articulo.Marca'),
        ),
        migrations.AddField(
            model_name='espejuelo',
            name='material_armadura',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='articulo.MaterialArmadura'),
        ),
        migrations.AddField(
            model_name='espejuelo',
            name='tipo_armazon',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='articulo.TipoArmazon'),
        ),
        migrations.AddField(
            model_name='espejuelo',
            name='tipo_montura',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='articulo.TipoMontura'),
        ),
        migrations.AddField(
            model_name='receta',
            name='lente_cerca',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lente_cerca_receta', to='articulo.EspejueloGraduado'),
        ),
        migrations.AddField(
            model_name='receta',
            name='lente_lejos',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lente_lejos_receta', to='articulo.EspejueloGraduado'),
        ),
    ]
