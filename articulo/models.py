import time

from django.contrib.auth.models import User
from django.db import models
from django.db.models import Q
from model_utils import Choices

from articulo.Barcode import *

ORDER_COLUMN_CHOICES_RECETAS = Choices(
    ('0', 'numero'),
    ('1', 'fecha'),
    ('2', 'cliente'),
    ('3', 'doctor'),
    ('5', 'atendida'),
    ('6 ', 'sucursal'),
)

ORDER_COLUMN_CHOICES_VENTAS = Choices(
    ('0', 'id'),
    ('1', 'fecha'),
    ('2', 'sucursal'),
    ('3', 'cliente'),
    ('4', 'total'),
)

ORDER_COLUMN_CHOICES_COMPRAS = Choices(
    ('0', 'id'),
    ('1', 'fecha'),
    ('2', 'sucursal'),
    ('3', 'proveedor'),
    ('4', 'total'),
)

ORDER_COLUMN_CHOICES_ACCESORIOS = Choices(
    ('0', 'nombre'),
    ('1', 'sucursal'),
    ('2', 'codigo'),
    ('3', 'precio'),
    ('4', 'tipo'),
)
ORDER_COLUMN_CHOICES_CRISTALES = Choices(
    ('0', 'codigo'),
    ('1', 'nombre'),
    ('2', 'sucursal'),
    ('3', 'color'),
    ('4', 'modelo'),
    ('5', 'materialCristal'),
    ('6', 'precio'),
    ('7', 'cantidad'),
)

ORDER_COLUMN_CHOICES_LENTES = Choices(
    ('0', 'nombre'),
    ('1', 'sucursal'),
    ('2', 'codigo'),
    ('3', 'precio'),
    ('4', 'tipoArmazon'),
    ('5', 'materialArmadura'),
    ('6', 'calibre'),
    ('7', 'puente'),
    ('8', 'cristal'),
)
ORDER_COLUMN_CHOICES_GAFAS_SOL = Choices(
    ('0', 'nombre'),
    ('1', 'sucursal'),
    ('2', 'codigo'),
    ('3', 'precio'),
    ('4', 'tipoArmazon'),
    ('5', 'materialArmadura'),
    ('6', 'calibre'),
    ('7', 'puente'),
    ('8', 'cristal'),
)

ORDER_COLUMN_CHOICES_LENTES_CONTACTOS = Choices(
    ('0', 'nombre'),
    ('1', 'sucursal'),
    ('2', 'codigo'),
    ('3', 'precio'),
    ('4', 'marca'),
    ('5', 'color'),
)


# Create your models here.
class Sucursal(models.Model):
    nombre = models.CharField(max_length=75)
    direccion = models.CharField(max_length=150)

    def __str__(self):
        return self.nombre


class Articulo(models.Model):
    nombre = models.CharField(max_length=75, blank=True)
    sucursal = models.ForeignKey(Sucursal, related_name='articulos', blank=True)
    codigo = models.CharField(max_length=20, blank=True, null=True)
    descripcion = models.CharField(max_length=150, blank=True)
    precio = models.FloatField(blank=True, default=1)
    cantidad = models.IntegerField(default=1, blank=True)
    activo = models.BooleanField(blank=True)
    pendiente = models.BooleanField(blank=True,default=False)
    foto = models.ImageField(upload_to='articulos/', blank=True, default=' ', null=True)

    bar_code = models.CharField(max_length=10000, blank=True)

    def __str__(self):
        return self.nombre


class Medicion(models.Model):
    esfera = models.FloatField()
    cilindro = models.FloatField()
    eje = models.FloatField()
    prisma = models.FloatField()
    altura = models.FloatField()


class Marca(models.Model):
    nombre = models.CharField(max_length=75)
    descripcion = models.CharField(max_length=75)
    siglas = models.CharField(max_length=3)

    def __str__(self):
        return self.nombre


class Color(models.Model):
    nombre = models.CharField(max_length=50)
    siglas = models.CharField(max_length=3)

    def __str__(self):
        return self.nombre


class Modelo(models.Model):
    nombre = models.CharField(max_length=75)
    descripcion = models.CharField(max_length=75)
    siglas = models.CharField(max_length=3)

    def __str__(self):
        return self.nombre


class MaterialCristal(models.Model):
    nombre = models.CharField(max_length=75)
    descripcion = models.CharField(max_length=75)
    siglas = models.CharField(max_length=3)

    def __str__(self):
        return self.nombre


class TratamientoCristal(models.Model):
    nombre = models.CharField(max_length=75)
    descripcion = models.CharField(max_length=75)
    siglas = models.CharField(max_length=3)

    def __str__(self):
        return self.nombre


class CristalGraduado(Articulo):
    color = models.ForeignKey(Color, blank=True)
    modelo = models.ForeignKey(Modelo, blank=True)
    laboratorio = models.BooleanField(blank=True)
    material_cristal = models.ForeignKey(MaterialCristal, blank=True)
    tratamientos = models.ManyToManyField(TratamientoCristal, blank=True)
    medicion_cerca = models.ForeignKey(Medicion, related_name='medicion_cerca', blank=True, null=True)
    medicion_lejos = models.ForeignKey(Medicion, related_name='medicion_lejos', blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            cod = "CG-" + time.strftime("%Y%m%d%H%M%S")
            self.codigo = cod
            bar = get_image(cod)
            self.bar_code = bar
        super(CristalGraduado, self).save(args, kwargs)

    def __str__(self):
        return self.nombre


def query_cristales_by_args(**kwargs):
    draw = int(kwargs.get('draw', ['1'])[0])
    length = int(kwargs.get('length', ['10'])[0])
    start = int(kwargs.get('start', ['0'])[0])
    search_value = kwargs.get('search[value]', [''])[0]
    order_column = kwargs.get('order[0][column]', ['0'])[0]
    order = kwargs.get('order[0][dir]', ['asc'])[0]
    order_column = ORDER_COLUMN_CHOICES_CRISTALES[order_column]

    # django orm '-' -> desc
    if order == 'desc':
        order_column = '-' + order_column

    queryset = CristalGraduado.objects.all()
    total = queryset.count()

    if search_value:
        queryset = queryset.filter(Q(nombre__icontains=search_value) |
                                   Q(color__nombre__icontains=search_value) |
                                   Q(codigo__icontains=search_value))

    count = queryset.count()
    queryset = queryset.order_by(order_column)[start:start + length]
    return {
        'items': queryset,
        'count': count,
        'total': total,
        'draw': draw
    }


class TipoArmazon(models.Model):
    nombre = models.CharField(max_length=120)
    descripcion = models.CharField(max_length=250)

    def __str__(self):
        return self.nombre


class TipoMontura(models.Model):
    nombre = models.CharField(max_length=75)
    descripcion = models.CharField(max_length=250)

    def __str__(self):
        return self.nombre


class MaterialArmadura(models.Model):
    nombre = models.CharField(max_length=75)
    descripcion = models.CharField(max_length=250)

    def __str__(self):
        return self.nombre


class Espejuelo(Articulo):
    tipo_armazon = models.ForeignKey(TipoArmazon, blank=True)
    color = models.ForeignKey(Color, blank=True)
    marca = models.ForeignKey(Marca, blank=True)
    tipo_montura = models.ForeignKey(TipoMontura, blank=True)
    material_armadura = models.ForeignKey(MaterialArmadura, blank=True)
    calibre = models.IntegerField(blank=True)
    puente = models.IntegerField(blank=True)


class EspejueloGraduado(Espejuelo):
    cristalDer = models.ForeignKey(CristalGraduado, related_name="cristalDer", blank=True)
    cristalIzq = models.ForeignKey(CristalGraduado, related_name="cristalIzq", blank=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            cod = "L-" + time.strftime("%Y%m%d%H%M%S")
            self.codigo = cod
            bar = get_image(cod)
            self.bar_code = bar
        super(EspejueloGraduado, self).save()


def query_espejuelos_by_args(**kwargs):
    draw = int(kwargs.get('draw', ['1'])[0])
    length = int(kwargs.get('length', ['10'])[0])
    start = int(kwargs.get('start', ['0'])[0])
    search_value = kwargs.get('search[value]', [''])[0]
    order_column = kwargs.get('order[0][column]', ['0'])[0]
    order = kwargs.get('order[0][dir]', ['asc'])[0]
    order_column = ORDER_COLUMN_CHOICES_LENTES[order_column]

    # django orm '-' -> desc
    if order == 'desc':
        order_column = '-' + order_column

    queryset = EspejueloGraduado.objects.all()

    total = queryset.count()

    if search_value:
        queryset = queryset.filter(Q(codigo__icontains=search_value) |
                                   Q(nombre__icontains=search_value) |
                                   Q(calibre__icontains=search_value))

    count = queryset.count()

    queryset = queryset.order_by(order_column)[start:start + length]
    return {
        'items': queryset,
        'count': count,
        'total': total,
        'draw': draw
    }


class LenteContacto(Articulo):
    marca = models.ForeignKey(Marca)
    color = models.ForeignKey(Color)
    blando = models.BooleanField()
    gas_permeable = models.BooleanField()
    medicion = models.ForeignKey(Medicion)

    def save(self, *args, **kwargs):
        if not self.pk:
            cod = "LC-" + time.strftime("%Y%m%d%H%M%S")
            self.codigo = cod
            bar = get_image(cod)
            self.bar_code = bar
        super(LenteContacto, self).save(args, kwargs)


def query_lenteContactos_by_args(**kwargs):
    draw = int(kwargs.get('draw', ['1'])[0])
    length = int(kwargs.get('length', ['10'])[0])
    start = int(kwargs.get('start', ['0'])[0])
    search_value = kwargs.get('search[value]', [''])[0]
    order_column = kwargs.get('order[0][column]', ['0'])[0]
    order = kwargs.get('order[0][dir]', ['asc'])[0]
    order_column = ORDER_COLUMN_CHOICES_LENTES_CONTACTOS[order_column]

    # django orm '-' -> desc
    if order == 'desc':
        order_column = '-' + order_column

    queryset = LenteContacto.objects.all()
    total = queryset.count()

    if search_value:
        queryset = queryset.filter(Q(codigo__icontains=search_value) |
                                   Q(nombre__icontains=search_value) |
                                   Q(marca__nombre__icontains=search_value))

    count = queryset.count()
    queryset = queryset.order_by(order_column)[start:start + length]
    return {
        'items': queryset,
        'count': count,
        'total': total,
        'draw': draw
    }


class MaterialSol(models.Model):
    material = models.CharField(max_length=75)

    def __str__(self):
        return self.material


class Accesorio(Articulo):
    tipo = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.tipo

    def save(self, *args, **kwargs):
        if not self.pk:
            cod = "A-" + time.strftime("%Y%m%d%H%M%S")
            self.codigo = cod
            bar = get_image(cod)
            self.bar_code = bar
        super(Accesorio, self).save()


def query_accesorios_by_args(**kwargs):
    draw = int(kwargs.get('draw', ['1'])[0])
    length = int(kwargs.get('length', ['10'])[0])
    start = int(kwargs.get('start', ['0'])[0])
    search_value = kwargs.get('search[value]', [''])[0]
    order_column = kwargs.get('order[0][column]', ['0'])[0]
    order = kwargs.get('order[0][dir]', ['asc'])[0]
    order_column = ORDER_COLUMN_CHOICES_ACCESORIOS[order_column]

    # django orm '-' -> desc
    if order == 'desc':
        order_column = '-' + order_column

    queryset = Accesorio.objects.all()
    total = queryset.count()

    if search_value:
        queryset = queryset.filter(Q(codigo__icontains=search_value) |
                                   Q(nombre__icontains=search_value) |
                                   Q(tipo__icontains=search_value))

    count = queryset.count()
    queryset = queryset.order_by(order_column)[start:start + length]
    return {
        'items': queryset,
        'count': count,
        'total': total,
        'draw': draw
    }


class GafaSol(Articulo):
    tipo_armazon = models.ForeignKey(TipoArmazon, blank=True)
    tipo_montura = models.ForeignKey(TipoMontura, blank=True)
    color = models.ForeignKey(Color, blank=True)
    marca = models.ForeignKey(Marca, blank=True)
    material_armadura = models.ForeignKey(MaterialArmadura, blank=True)
    material_sol = models.ForeignKey(MaterialSol, blank=True)

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        if not self.pk:
            cod = "GS-" + time.strftime("%Y%m%d%H%M%S")
            self.codigo = cod
            bar = get_image('My_Barcode')
        super(GafaSol, self).save(args, kwargs)


def query_gafaSol_by_args(**kwargs):
    draw = int(kwargs.get('draw', ['1'])[0])
    length = int(kwargs.get('length', ['10'])[0])
    start = int(kwargs.get('start', ['0'])[0])
    search_value = kwargs.get('search[value]', [''])[0]
    order_column = kwargs.get('order[0][column]', ['0'])[0]
    order = kwargs.get('order[0][dir]', ['asc'])[0]
    order_column = ORDER_COLUMN_CHOICES_GAFAS_SOL[order_column]

    # django orm '-' -> desc
    if order == 'desc':
        order_column = '-' + order_column

    queryset = GafaSol.objects.all()
    total = queryset.count()

    if search_value:
        queryset = queryset.filter(Q(codigo__icontains=search_value) |
                                   Q(nombre__icontains=search_value))

    count = queryset.count()
    queryset = queryset.order_by(order_column)[start:start + length]
    return {
        'items': queryset,
        'count': count,
        'total': total,
        'draw': draw
    }


class Persona(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    sucursal = models.ForeignKey(Sucursal)
    fecha_nacimiento = models.DateField()
    CI = models.CharField(max_length=15)
    telefono = models.CharField(max_length=11)


class Doctor(Persona):
    codigo = models.IntegerField()
    cargo = models.CharField(max_length=15)
    foto = models.ImageField(upload_to='doctores/', null=True)


class Cliente(Persona):
    diagnostico = models.CharField(max_length=50)
    observaciones = models.CharField(max_length=75)
    foto = models.ImageField(upload_to='clientes/', null=True)


class Venta(models.Model):
    sucursal = models.ForeignKey(Sucursal)
    cliente = models.ForeignKey(Cliente, related_name='ventas')
    fecha = models.DateField()
    articulos = models.ManyToManyField(Articulo, related_name='ventas', blank=True)
    subtotal = models.FloatField()
    descuento = models.FloatField()
    total = models.FloatField()


def query_ventas_by_args(**kwargs):
    draw = int(kwargs.get('draw', ['1'])[0])
    length = int(kwargs.get('length', ['10'])[0])
    start = int(kwargs.get('start', ['0'])[0])
    search_value = kwargs.get('search[value]', [''])[0]
    order_column = kwargs.get('order[0][column]', ['0'])[0]
    order = kwargs.get('order[0][dir]', ['asc'])[0]
    order_column = ORDER_COLUMN_CHOICES_VENTAS[order_column]
    # django orm '-' -> desc
    if order == 'desc':
        order_column = '-' + order_column

    queryset = Venta.objects.all()

    total = queryset.count()

    if search_value:
        queryset = queryset.filter(Q(total__icontains=search_value) |
                                   Q(fecha__icontains=search_value) |
                                   Q(cliente__usuario__first_name__icontains=search_value))

    count = queryset.count()
    queryset = queryset.order_by(order_column)[start:start + length]
    return {
        'items': queryset,
        'count': count,
        'total': total,
        'draw': draw
    }


class Receta(models.Model):
    sucursal = models.ForeignKey(Sucursal)
    doctor = models.ForeignKey(Doctor)
    cliente = models.ForeignKey(Cliente)
    numero = models.IntegerField()
    fecha = models.DateField()
    atendida = models.BooleanField()
    insitucion = models.CharField(max_length=50)
    lente_cerca = models.ForeignKey(EspejueloGraduado, related_name='lente_cerca_receta', blank=True, null=True)
    lente_lejos = models.ForeignKey(EspejueloGraduado, related_name='lente_lejos_receta', blank=True, null=True)
    lente_contacto = models.ForeignKey(LenteContacto, related_name='lente_contacto_receta', blank=True, null=True)
    venta = models.ForeignKey(Venta, related_name='recetas', blank=True, null=True)


def query_recetas_by_args(**kwargs):
    draw = int(kwargs.get('draw', ['1'])[0])
    length = int(kwargs.get('length', ['10'])[0])
    start = int(kwargs.get('start', ['0'])[0])
    search_value = kwargs.get('search[value]', [''])[0]
    order_column = kwargs.get('order[0][column]', ['0'])[0]
    order = kwargs.get('order[0][dir]', ['asc'])[0]
    order_column = ORDER_COLUMN_CHOICES_RECETAS[order_column]
    cliente = int(kwargs.get('cliente', ['0'])[0])
    # django orm '-' -> desc
    if order == 'desc':
        order_column = '-' + order_column

    queryset = Receta.objects.all()

    if cliente != 0:
        cliente = Cliente.objects.get(pk=cliente)
        queryset = queryset.filter(Q(atendida=False) & Q(cliente__CI__iexact=cliente.CI))
        print(queryset.count)

    total = queryset.count()

    if search_value:
        queryset = queryset.filter(Q(cliente__usuario__first_name__contains=search_value) |
                                   Q(doctor__usuario__first_name__contains=search_value) |
                                   Q(numero__exact=search_value))

    count = queryset.count()
    queryset = queryset.order_by(order_column)[start:start + length]
    return {
        'items': queryset,
        'count': count,
        'total': total,
        'draw': draw
    }


class Proveedor(models.Model):
    sucursal = models.ForeignKey(Sucursal, blank=True)
    articulos = models.ManyToManyField(Articulo, related_name='proveedores', blank=True)
    nombre = models.CharField(max_length=20, blank=True)
    apellidos = models.CharField(max_length=50, blank=True)
    fecha_nacimiento = models.DateField(blank=True)
    CI = models.CharField(max_length=15, blank=True)
    direccion = models.CharField(max_length=150, blank=True)
    telefono = models.CharField(max_length=11, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    activo = models.BooleanField()
    foto = models.ImageField(upload_to='proveedores/', null=True)


def query_proveedores_by_args(**kwargs):
    activo = kwargs.get('activo', [''])[0]
    queryset = None

    if activo:
        queryset = Proveedor.objects.filter(activo=activo)
    else:
        queryset = Proveedor.objects.all()

    count = queryset.count()
    return {
        'items': queryset,
        'count': count
    }


class Compra(models.Model):
    sucursal = models.ForeignKey(Sucursal)
    proveedor = models.ForeignKey(Proveedor, related_name='compras')
    fecha = models.DateField()
    articulos = models.ManyToManyField(Articulo, verbose_name='articulo_compra', related_name='compras', blank=True)
    subtotal = models.FloatField()
    descuento = models.FloatField()
    total = models.FloatField()


def query_compras_by_args(**kwargs):
    draw = int(kwargs.get('draw', ['1'])[0])
    length = int(kwargs.get('length', ['10'])[0])
    start = int(kwargs.get('start', ['0'])[0])
    search_value = kwargs.get('search[value]', [''])[0]
    order_column = kwargs.get('order[0][column]', ['0'])[0]
    order = kwargs.get('order[0][dir]', ['asc'])[0]
    order_column = ORDER_COLUMN_CHOICES_COMPRAS[order_column]
    # django orm '-' -> desc
    if order == 'desc':
        order_column = '-' + order_column

    queryset = Compra.objects.all()

    total = queryset.count()

    if search_value:
        queryset = queryset.filter(Q(proveedor__usuario__first_name__contains=search_value) |
                                   Q(total__exact=search_value) |
                                   Q(fecha__exact=search_value))

    count = queryset.count()
    queryset = queryset.order_by(order_column)[start:start + length]
    return {
        'items': queryset,
        'count': count,
        'total': total,
        'draw': draw
    }

    class Articulo_compra(models.Model):
        articulo = models.ForeignKey(Articulo)
        compra = models.ForeignKey(Compra, related_name='compras')
        precio = models.FloatField()
