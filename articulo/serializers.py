from rest_framework import serializers, exceptions
from .models import *
from django.contrib.auth import authenticate


class SucursalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sucursal
        fields = ('url', 'id', 'nombre', 'direccion')


class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = ('url',
                  'id',
                  'nombre',
                  'siglas',
                  'descripcion')


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ('url',
                  'id',
                  'siglas',
                  'nombre')


class MedicionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicion
        fields = ('url',
                  'id',
                  'esfera',
                  'cilindro',
                  'eje',
                  'prisma',
                  'altura',
                  )


class ArticuloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articulo
        fields = ('url',
                  'id',
                  'activo',
                  'nombre',
                  'sucursal',
                  'codigo',
                  'descripcion',
                  'precio',
                  'cantidad')


class LenteContactoSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super(LenteContactoSerializer, self).__init__(*args, **kwargs)
        request = kwargs['context']['request']
        if request.method != 'PUT' and request.method != 'POST':
            self.fields['sucursal'] = SucursalSerializer()
            self.fields['medicion'] = MedicionSerializer()
            self.fields['color'] = ColorSerializer()
            self.fields['marca'] = MarcaSerializer()

    class Meta:
        model = LenteContacto
        fields = ('url',
                  'id',
                  'activo',
                  'pendiente',
                  'nombre',
                  'sucursal',
                  'codigo',
                  'descripcion',
                  'precio',
                  'cantidad',
                  'foto',
                  'bar_code',
                  'marca',
                  'color',
                  'blando',
                  'gas_permeable',
                  'medicion')


class ModeloSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Modelo
        fields = ('url', 'id',
                  'nombre',
                  'descripcion',
                  'siglas'
                  )


class MaterialCristalSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaterialCristal
        fields = (
            'url',
            'id',
            'nombre',
            'descripcion')


class TratamientoCristalSerializer(serializers.ModelSerializer):
    class Meta:
        model = TratamientoCristal
        fields = (
            'url',
            'id',
            'nombre',
            'siglas',
            'descripcion')


class CristalGraduadoSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super(CristalGraduadoSerializer, self).__init__(*args, **kwargs)
        request = kwargs['context']['request']
        if request.method != 'PUT' and request.method != 'POST':
            self.fields['sucursal'] = SucursalSerializer()
            self.fields['material_cristal'] = MaterialCristalSerializer()
            self.fields['tratamientos'] = TratamientoCristalSerializer(many=True)
            self.fields['modelo'] = ModeloSerializer()
            self.fields['color'] = ColorSerializer()
            self.fields['medicion_cerca'] = MedicionSerializer()
            self.fields['medicion_lejos'] = MedicionSerializer()

    class Meta:
        model = CristalGraduado
        fields = ('url',
                  'id',
                  'nombre',
                  'activo',
                  'pendiente',
                  'sucursal',
                  'codigo',
                  'descripcion',
                  'precio',
                  'cantidad',
                  'foto',
                  'bar_code',
                  'modelo',
                  'color',
                  'laboratorio',
                  'material_cristal',
                  'tratamientos',
                  'medicion_cerca',
                  'medicion_lejos'
                  )


class TipoArmazonSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoArmazon
        fields = ('url',
                  'id',
                  'nombre',
                  'descripcion')


class TipoMonturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoMontura
        fields = ('url',
                  'id',
                  'nombre',
                  'descripcion')


class MaterialArmaduraSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaterialArmadura
        fields = ('url',
                  'id',
                  'nombre',
                  'descripcion')


class EspejueloGraduadoSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super(EspejueloGraduadoSerializer, self).__init__(*args, **kwargs)
        request = kwargs['context']['request']
        if request.method != 'PUT' and request.method != 'POST':
            self.fields['sucursal'] = SucursalSerializer()
            self.fields['material_armadura'] = MaterialArmaduraSerializer()
            self.fields['tipo_armazon'] = TipoArmazonSerializer()
            self.fields['tipo_montura'] = TipoMonturaSerializer()
            self.fields['color'] = ColorSerializer()
            self.fields['marca'] = MarcaSerializer()
            self.fields['cristalIzq'] = CristalGraduadoSerializer(context={'request': request})
            self.fields['cristalDer'] = CristalGraduadoSerializer(context={'request': request})

    class Meta:
        model = EspejueloGraduado
        fields = (
            'url',
            'id',
            'nombre',
            'pendiente',
            'activo',
            'sucursal',
            'codigo',
            'descripcion',
            'precio',
            'cantidad',
            'foto',
            'bar_code',
            'tipo_armazon',
            'color',
            'tipo_montura',
            'material_armadura',
            'calibre',
            'puente',
            'cristalDer',
            'cristalIzq',
            'marca',
            'lente_cerca_receta',
            'lente_lejos_receta'
        )


class MaterialSolSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaterialSol
        fields = ('url',
                  'id',
                  'material')


class GafaSolSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super(GafaSolSerializer, self).__init__(*args, **kwargs)
        request = kwargs['context']['request']
        if request.method != 'PUT' and request.method != 'POST':
            self.fields['sucursal'] = SucursalSerializer()
            self.fields['material_armadura'] = MaterialArmaduraSerializer()
            self.fields['tipo_armazon'] = TipoArmazonSerializer()
            self.fields['tipo_montura'] = TipoMonturaSerializer()
            self.fields['color'] = ColorSerializer()
            self.fields['material_sol'] = MaterialSolSerializer()
            self.fields['marca'] = MarcaSerializer()

    class Meta:
        model = GafaSol
        fields = ('url',
                  'id',
                  'activo',
                  'nombre',
                  'sucursal',
                  'codigo',
                  'descripcion',
                  'precio',
                  'cantidad',
                  'marca',
                  'foto',
                  'bar_code',
                  'tipo_armazon',
                  'color',
                  'tipo_montura',
                  'material_armadura',
                  'material_sol')


class AccesorioSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super(AccesorioSerializer, self).__init__(*args, **kwargs)
        request = kwargs['context']['request']
        if request.method != 'PUT' and request.method != 'POST':
            self.fields['sucursal'] = SucursalSerializer()

    class Meta:
        model = Accesorio
        fields = ('url',
                  'id',
                  'activo',
                  'nombre',
                  'sucursal',
                  'codigo',
                  'descripcion',
                  'precio',
                  'cantidad',
                  'foto',
                  'bar_code',
                  'tipo')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'id',
                  'first_name',
                  'last_name',
                  'username',
                  'password',
                  'email',
                  'is_staff',
                  'is_active',
                  'date_joined')


class DoctorSerializer(serializers.ModelSerializer):
    usuario = UserSerializer()
    sucursal = SucursalSerializer()

    class Meta:
        model = Doctor
        fields = ('url', 'id',
                  'codigo',
                  'cargo',
                  'usuario',
                  'sucursal',
                  'fecha_nacimiento',
                  'CI',
                  'telefono'
                  )


class ClienteSerializer(serializers.ModelSerializer):
    usuario = UserSerializer()
    sucursal = SucursalSerializer()

    class Meta:
        model = Cliente
        fields = ('url', 'id',
                  'observaciones',
                  'diagnostico',
                  'usuario',
                  'sucursal',
                  'fecha_nacimiento',
                  'CI',
                  'telefono'
                  )


class RecetaSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super(RecetaSerializer, self).__init__(*args, **kwargs)
        request = kwargs['context']['request']
        if request.method != 'PUT' and request.method != 'POST':
            self.fields['sucursal'] = SucursalSerializer()
            self.fields['cliente'] = ClienteSerializer()
            self.fields['doctor'] = DoctorSerializer()
            self.fields['lente_cerca'] = EspejueloGraduadoSerializer(context={'request': request})
            self.fields['lente_lejos'] = EspejueloGraduadoSerializer(context={'request': request})
            self.fields['lente_contacto'] = LenteContactoSerializer(context={'request': request})

    class Meta:
        model = Receta
        fields = ('url', 'id',
                  'numero',
                  'doctor',
                  'cliente',
                  'sucursal',
                  'fecha',
                  'lente_lejos',
                  'lente_cerca',
                  'lente_contacto',
                  'atendida'
                  )


class ProveedorSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super(ProveedorSerializer, self).__init__(*args, **kwargs)
        request = kwargs['context']['request']
        if request.method != 'PUT' and request.method != 'POST':
            self.fields['sucursal'] = SucursalSerializer()
            self.fields['articulos'] = ArticuloSerializer(many=True)

    class Meta:
        model = Proveedor
        fields = ('url', 'id',
                  'nombre',
                  'apellidos',
                  'activo',
                  'telefono',
                  'sucursal',
                  'fecha_nacimiento',
                  'CI',
                  'email',
                  'direccion',
                  'foto',
                  'articulos'
                  )


class VentaSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super(VentaSerializer, self).__init__(*args, **kwargs)
        request = kwargs['context']['request']
        if request.method != 'PUT' and request.method != 'POST':
            self.fields['sucursal'] = SucursalSerializer(context={'request': request})
            self.fields['cliente'] = ClienteSerializer(context={'request': request})
            self.fields['articulos'] = ArticuloSerializer(context={'request': request}, many=True)
            self.fields['recetas'] = RecetaSerializer(context={'request': request}, many=True)

    class Meta:
        model = Venta
        fields = ('url',
                  'id',
                  'sucursal',
                  'cliente',
                  'fecha',
                  'articulos',
                  'recetas',
                  'total',
                  'subtotal',
                  'descuento'
                  )


class CompraSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super(CompraSerializer, self).__init__(*args, **kwargs)
        request = kwargs['context']['request']
        if request.method != 'PUT' and request.method != 'POST':
            self.fields['sucursal'] = SucursalSerializer(context={'request': request})
            self.fields['proveedor'] = ProveedorSerializer(context={'request': request})
            self.fields['articulos'] = ArticuloSerializer(context={'request': request}, many=True)

    class Meta:
        model = Compra
        fields = ('url',
                  'id',
                  'sucursal',
                  'proveedor',
                  'fecha',
                  'articulos',
                  'total',
                  'subtotal',
                  'descuento'
                  )


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get("username", "")
        password = data.get("password", "")
        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    data["user"] = user
                else:
                    msg = "Usuario inactivo"
                    raise exceptions.ValidationError(msg)
            else:
                msg = "No existe el usuario"
                raise exceptions.ValidationError(msg)
        else:
            msg = "Incorrecto"
            raise exceptions.ValidationError(msg)
        return data
