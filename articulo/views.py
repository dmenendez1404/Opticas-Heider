from django.shortcuts import render_to_response
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from articulo.models import *
from articulo.serializers import *


# Create your views here.
def index(request):
    return render_to_response('index.html')


def articulos(request):
    return render_to_response('articulos.html')


def addArticulo(request):
    return render_to_response('addArticulo.html')


def lentes(request):
    return render_to_response('lentes.html')


def lentesContacto(request):
    return render_to_response('lentes_contacto.html')


def cristalesGraduados(request):
    return render_to_response('cristales_graduados.html')


def gafaSol(request):
    return render_to_response('gafaSol.html')


def accesorios(request):
    return render_to_response('accesorios.html')


def graficos(request):
    return render_to_response('graficas.html')


#  Create ViewSets
class SucursalViewSet(viewsets.ModelViewSet):
    queryset = Sucursal.objects.all()
    serializer_class = SucursalSerializer


class MarcaViewSet(viewsets.ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer


class ColorViewSet(viewsets.ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer


class MedicionViewSet(viewsets.ModelViewSet):
    queryset = Medicion.objects.all()
    serializer_class = MedicionSerializer


class ModeloViewSet(viewsets.ModelViewSet):
    queryset = Modelo.objects.all()
    serializer_class = ModeloSerializer


class MaterialCristalViewSet(viewsets.ModelViewSet):
    queryset = MaterialCristal.objects.all()
    serializer_class = MaterialCristalSerializer


class TratamientoCristalViewSet(viewsets.ModelViewSet):
    queryset = TratamientoCristal.objects.all()
    serializer_class = TratamientoCristalSerializer


class TipoArmazonViewSet(viewsets.ModelViewSet):
    queryset = TipoArmazon.objects.all()
    serializer_class = TipoArmazonSerializer


class TipoMonturaViewSet(viewsets.ModelViewSet):
    queryset = TipoMontura.objects.all()
    serializer_class = TipoMonturaSerializer


class MaterialArmaduraViewSet(viewsets.ModelViewSet):
    queryset = MaterialArmadura.objects.all()
    serializer_class = MaterialArmaduraSerializer


class EspejueloViewSet(viewsets.ModelViewSet):
    queryset = EspejueloGraduado.objects.all()
    serializer_class = EspejueloGraduadoSerializer

    def list(self, request, **kwargs):
        try:
            esp = query_espejuelos_by_args(**request.query_params)
            serializer = EspejueloGraduadoSerializer(esp['items'], context={'request': request}, many=True)
            result = dict()
            result['data'] = serializer.data
            result['draw'] = esp['draw']
            result['recordsTotal'] = esp['total']
            result['recordsFiltered'] = esp['count']

            return Response(result, status=status.HTTP_200_OK, template_name=None, content_type=None)

        except Exception as e:
            return Response(e, status=status.HTTP_404_NOT_FOUND, template_name=None, content_type=None)


class MaterialSolViewSet(viewsets.ModelViewSet):
    queryset = MaterialSol.objects.all()
    serializer_class = MaterialSolSerializer


class ArticulosViewSet(viewsets.ModelViewSet):
    queryset = Articulo.objects.all()
    serializer_class = ArticuloSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

class AccesoriosViewSet(viewsets.ModelViewSet):
    queryset = Accesorio.objects.all()
    serializer_class = AccesorioSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def list(self, request, **kwargs):
        try:
            esp = query_accesorios_by_args(**request.query_params)
            serializer = AccesorioSerializer(esp['items'], context={'request': request}, many=True)
            result = dict()
            result['data'] = serializer.data
            result['draw'] = esp['draw']
            result['recordsTotal'] = esp['total']
            result['recordsFiltered'] = esp['count']

            return Response(result, status=status.HTTP_200_OK, template_name=None, content_type=None)

        except Exception as e:
            return Response(e, status=status.HTTP_404_NOT_FOUND, template_name=None, content_type=None)


class LentesContactoViewSet(viewsets.ModelViewSet):
    queryset = LenteContacto.objects.all()
    serializer_class = LenteContactoSerializer

    def list(self, request, **kwargs):
        try:
            esp = query_lenteContactos_by_args(**request.query_params)
            serializer = LenteContactoSerializer(esp['items'], context={'request': request}, many=True)
            result = dict()
            result['data'] = serializer.data
            result['draw'] = esp['draw']
            result['recordsTotal'] = esp['total']
            result['recordsFiltered'] = esp['count']

            return Response(result, status=status.HTTP_200_OK, template_name=None, content_type=None)

        except Exception as e:
            return Response(e, status=status.HTTP_404_NOT_FOUND, template_name=None, content_type=None)


class CristalesGraduadosViewSet(viewsets.ModelViewSet):
    queryset = CristalGraduado.objects.all()
    serializer_class = CristalGraduadoSerializer

    def list(self, request, **kwargs):
        try:
            esp = query_cristales_by_args(**request.query_params)
            serializer = CristalGraduadoSerializer(esp['items'], context={'request': request}, many=True)
            result = dict()
            result['data'] = serializer.data
            result['draw'] = esp['draw']
            result['recordsTotal'] = esp['total']
            result['recordsFiltered'] = esp['count']

            return Response(result, status=status.HTTP_200_OK, template_name=None, content_type=None)

        except Exception as e:
            return Response(e, status=status.HTTP_404_NOT_FOUND, template_name=None, content_type=None)


class GafaSolViewSet(viewsets.ModelViewSet):
    queryset = GafaSol.objects.all()
    serializer_class = GafaSolSerializer

    def list(self, request, **kwargs):
        try:
            esp = query_gafaSol_by_args(**request.query_params)
            serializer = GafaSolSerializer(esp['items'], context={'request': request}, many=True)
            result = dict()
            result['data'] = serializer.data
            result['draw'] = esp['draw']
            result['recordsTotal'] = esp['total']
            result['recordsFiltered'] = esp['count']

            return Response(result, status=status.HTTP_200_OK, template_name=None, content_type=None)

        except Exception as e:
            return Response(e, status=status.HTTP_404_NOT_FOUND, template_name=None, content_type=None)

from rest_framework.views import APIView;
from articulo.serializers import LoginSerializer
from django.contrib.auth import login as django_login, logout as django_logout
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        django_login(request, user)
        token, created = Token.objects.get_or_create(user = user)
        return Response({"token": token.key}, status = 200)

class Logout(APIView):
    authentication_classes = (TokenAuthentication,)

    def post(self, request):
        django_logout(request)
        return Response(status = 204 )