from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template.loader import render_to_string
from django.http import HttpResponse
from articulo.models import Compra
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework import viewsets
from articulo.serializers import *

class CompraViewSet(viewsets.ModelViewSet):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer

    def list(self, request, **kwargs):
        try:
            esp = query_compras_by_args(**request.query_params)
            serializer = CompraSerializer(esp['items'], context={'request': request}, many=True)
            result = dict()
            result['data'] = serializer.data
            result['draw'] = esp['draw']
            result['recordsTotal'] = esp['total']
            result['recordsFiltered'] = esp['count']

            return Response(result, status=status.HTTP_200_OK, template_name=None, content_type=None)

        except Exception as e:
            return Response(e, status=status.HTTP_404_NOT_FOUND, template_name=None, content_type=None)


def addCompra(request):
    return render_to_response('addCompra.html')

def compras(request):
    return render_to_response('compras.html')

def addLente(request):
    return render_to_response('addArticulo.html')



# Create your views here.
