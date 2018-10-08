from django.shortcuts import render_to_response
from rest_framework import viewsets, status, views
from rest_framework.parsers import *
from rest_framework.response import Response

from articulo.serializers import *

def proveedores(request):
    return render_to_response('proveedores.html')

class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer

    def list(self, request, **kwargs):
        try:
            prov = query_proveedores_by_args(**request.query_params)
            serializer = ProveedorSerializer(prov['items'], context={'request': request}, many=True)
            result = dict()
            result['data'] = serializer.data
            result['recordsTotal'] = prov['count']

            return Response(result, status=status.HTTP_200_OK, template_name=None, content_type=None)

        except Exception as e:
            return Response(e, status=status.HTTP_404_NOT_FOUND, template_name=None, content_type=None)


#class ImageView(viewa.APIView):

  #parser_classes = (MultiPartParser, FormParser)

  #def post(self, request, *args, **kwargs):

    #file_serializer = ProveedorSerializer(data=request.data)
    #if file_serializer.is_valid():
     # file_serializer.save()
     # return Response(file_serializer.data, status=status.HTTP_201_CREATED)
    #else:
      #return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)