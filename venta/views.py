from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template.loader import render_to_string
from django.http import HttpResponse
from articulo.models import Accesorio, GafaSol, EspejueloGraduado, LenteContacto, CristalGraduado
from rest_framework import viewsets
from rest_framework import viewsets, status
from rest_framework.response import Response
from articulo.serializers import *
from datetime import datetime
from rest_framework.decorators import list_route, detail_route

class VentaViewSet(viewsets.ModelViewSet):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer

    def list(self, request, **kwargs):
        try:
            esp = query_ventas_by_args(**request.query_params)
            serializer = VentaSerializer(esp['items'], context={'request': request}, many=True)
            result = dict()
            result['data'] = serializer.data
            result['draw'] = esp['draw']
            result['recordsTotal'] = esp['total']
            result['recordsFiltered'] = esp['count']

            return Response(result, status=status.HTTP_200_OK, template_name=None, content_type=None)

        except Exception as e:
            return Response(e, status=status.HTTP_404_NOT_FOUND, template_name=None, content_type=None)

    # @detail_route(methods=['get'], url_name='pormes', url_path='pormes')
    # def pormes(self, request, **kwargs):
    #     fecha = datetime.today()
    #     Mes = kwargs['pk']
    #     Anno = fecha.year
    #     ventas = Venta.objects.filter(fecha__year=Anno)
    #     ventas = ventas.filter(fecha__month=Mes)
    #     result = VentaSerializer(ventas, context={'request': request}, many=True)
    #     return Response(result.data, status=status.HTTP_200_OK, template_name=None, content_type=None)

    @detail_route(methods=['get'], url_name='ventasEnAnnoActual', url_path='ventasEnAnnoActual')
    def ventasEnAnnoActual(self, request, **kwargs):
        kwarg = kwargs['pk']
        fecha = datetime.today()
        AnnoActual = fecha.year
        MesActual = fecha.month

        ventasDeAnnoActual = Venta.objects.filter(fecha__lte=fecha,fecha__year=AnnoActual)
        ventas = VentaSerializer(ventasDeAnnoActual, context={'request': request}, many=True)

        # Rellenando con cero el total de ventas en cada mes para luego calcularlas
        totalesPorMes = {}
        for mes in range(1, MesActual + 1):
            totalesPorMes[mes] = 0

        sumaTotal = 0

        for venta in ventas.data:
            fechaVenta = venta['fecha']
            mesVenta = fechaVenta[5:7]
            mes = int(mesVenta)
            total = venta['total']
            totalesPorMes[mes] += total
            sumaTotal += total

        return Response({'sumaTotal':sumaTotal,'totalesPorMes':totalesPorMes,'mesActual':MesActual,'annoActual':AnnoActual}, status=status.HTTP_200_OK, template_name=None, content_type=None)

    @detail_route(methods=['get'], url_name='ventasPorAnno', url_path='ventasPorAnno')
    def ventasPorAnno(self, request, **kwargs):
        kwarg = kwargs['pk']
        fecha = datetime.today()
        annoActual = fecha.year

        ventasAll = Venta.objects.filter(fecha__lte=fecha)
        ventas = VentaSerializer(ventasAll, context={'request': request}, many=True)

        totalesPorAnno = {}
        sumaTotal = 0
        annoMenor = annoActual

        # Rellenando con ceros la suma por annos del arreglo
        for venta in ventas.data:
            fechaVenta = venta['fecha']
            annoVenta = fechaVenta[0:4]
            anno = int(annoVenta)
            totalesPorAnno[anno] = 0
            if(annoMenor > anno):
                annoMenor = anno

        # LLenando las posiciones de los annos con sus totales de venta
        for venta in ventas.data:
            fechaVenta = venta['fecha']
            annoVenta = fechaVenta[0:4]
            anno = int(annoVenta)
            total = venta['total']
            totalesPorAnno[anno] += total
            sumaTotal += total

        return Response(
            {'sumaTotal': sumaTotal, 'totalesPorAnno': totalesPorAnno, 'annoActual': annoActual, 'annoMenor':annoMenor},
            status=status.HTTP_200_OK, template_name=None, content_type=None)


def addVentas(request):
    return render_to_response('addVenta.html')

def ventas(request):
    return render_to_response('ventas.html')


