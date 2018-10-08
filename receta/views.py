from io import BytesIO

from django.http.response import HttpResponse
from django.shortcuts import render_to_response
from reportlab.lib.colors import (
    brown,
    white
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (
    Paragraph,
    Table,
    TableStyle
)
from reportlab.platypus import SimpleDocTemplate
from rest_framework import viewsets, status
from rest_framework.response import Response

from articulo.serializers import *


def recetas(request):
    return render_to_response('recetas.html')


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class RecetaViewSet(viewsets.ModelViewSet):
    queryset = Receta.objects.all()
    serializer_class = RecetaSerializer

    def list(self, request, **kwargs):
        try:

            recetas = query_recetas_by_args(**request.query_params)
            serializer = RecetaSerializer(recetas['items'], context={'request': request}, many=True)
            result = dict()
            result['data'] = serializer.data
            result['draw'] = recetas['draw']
            result['recordsTotal'] = recetas['total']
            result['recordsFiltered'] = recetas['count']

            return Response(result, status=status.HTTP_200_OK, template_name=None, content_type=None)

        except Exception as e:
            return Response(e, status=status.HTTP_404_NOT_FOUND, template_name=None, content_type=None)


def pdf_receta(request):
    response = HttpResponse(content_type='application/pdf')
    id = request.GET['id']
    receta = Receta.objects.get(pk=id)
    pdf_name = "receta " + str(receta.numero) + ".pdf"
    response['Content-Disposition'] = 'attachment; filename=%s' % pdf_name
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer,
                            pagesize=letter,
                            rightMargin=40,
                            leftMargin=40,
                            topMargin=60,
                            bottomMargin=18,
                            )
    # table header
    content = []
    styles = stylesheet()
    tb_fecha = [
        [Paragraph("FECHA", styles['default']),
         Paragraph(str(receta.fecha.day), styles['default']),
         Paragraph(str(receta.fecha.month), styles['center']),
         Paragraph(str(receta.fecha.year), styles['rigth'])],
        [Paragraph("RETIRA", styles['default']),
         Paragraph("  ", styles['default']),
         Paragraph("  ", styles['center']),
         Paragraph("  ", styles['rigth'])]
    ]
    tb = Table(tb_fecha)
    tb.setStyle(TableStyle(
        [
            ('GRID', (1, 0), (3, -1), 1, brown),
            ('BACKGROUND', (0, 0), (-1, 0), None)
        ]
    ))
    # banner = Image('../../venta/static/images/banner.png')
    tbl_data = [
        [Paragraph("Opticas Alemanas(LOGO)", styles['default']),
         Paragraph("Orden de trabajo", styles['title']),
         Paragraph(" ", styles['default'])
         ],
        [Paragraph(" ", styles['default']),
         Paragraph(str(receta.numero), styles['title'])],
        [Paragraph(" ", styles['default']),
         Paragraph(" ", styles['title']),
         tb]
    ]
    tb_header = Table(tbl_data)
    content.append(tb_header)
    pedido = Paragraph("Pedido a: ", styles['default'])
    content.append(pedido)
    cliente = Paragraph("Señor: " + receta.cliente.usuario.first_name + " " + receta.cliente.usuario.last_name,
                        styles['default'])
    content.append(cliente)
    direccion = Paragraph("Domicilio: ", styles['default'])
    content.append(direccion)
    tbl_data = [
        [Paragraph("Tel: " + receta.cliente.telefono, styles['default']),
         Paragraph("CI: " + receta.cliente.CI, styles['center']),
         Paragraph("E-mail: " + receta.cliente.usuario.email, styles['rigth'])]
    ]
    tb = Table(tbl_data)
    content.append(tb)
    content.append(Paragraph("MEDICIÓN", styles['center']))
    headings = ('', Paragraph("ESF.", styles['center']), Paragraph("CIL", styles['center']),
                Paragraph("EJE", styles['center']), Paragraph("PRISMA", styles['center']),
                Paragraph("DI.INT", styles['center']), Paragraph("ALT.", styles['center']))

    m_lejos_od = Medicion()
    m_lejos_oi = Medicion()
    m_cerca_od = Medicion()
    m_cerca_oi = Medicion()
    if receta.lente_cerca:
        m_lejos_od = receta.lente_cerca.cristalDer.medicion_lejos
        m_lejos_oi = receta.lente_cerca.cristalIzq.medicion_lejos
    if receta.lente_lejos:
        m_cerca_od = receta.lente_cerca.cristalDer.medicion_cerca
        m_cerca_oi = receta.lente_cerca.cristalIzq.medicion_cerca
    mediciones = [
        [Paragraph("Lejos OD.", styles['rigth']), Paragraph(str(m_lejos_od.esfera), styles['center']),
         Paragraph(str(m_lejos_od.cilindro), styles['center']),
         Paragraph(str(m_lejos_od.eje)+"º", styles['center']),
         Paragraph(str(m_lejos_od.prisma), styles['center']),
         Paragraph(str(0), styles['center']),
         Paragraph(str(m_lejos_od.altura), styles['center'])
         ],
        [Paragraph("OI.", styles['rigth']), Paragraph(str(m_lejos_oi.esfera), styles['center']),
         Paragraph(str(m_lejos_oi.cilindro), styles['center']),
         Paragraph(str(m_lejos_oi.eje)+"º", styles['center']),
         Paragraph(str(m_lejos_oi.prisma), styles['center']),
         Paragraph(str(0), styles['center']),
         Paragraph(str(m_lejos_oi.altura), styles['center'])
         ],
        [Paragraph("Cerca OD.", styles['rigth']), Paragraph(str(m_cerca_od.esfera), styles['center']),
         Paragraph(str(m_cerca_od.cilindro), styles['center']),
         Paragraph(str(m_cerca_od.eje)+"º", styles['center']),
         Paragraph(str(m_cerca_od.prisma), styles['center']),
         Paragraph(str(0), styles['center']),
         Paragraph(str(m_cerca_od.altura), styles['center'])
         ],
        [Paragraph("OI.", styles['rigth']), Paragraph(str(m_cerca_oi.esfera), styles['center']),
         Paragraph(str(m_cerca_oi.cilindro), styles['center']),
         Paragraph(str(m_cerca_oi.eje)+"º", styles['center']),
         Paragraph(str(m_cerca_oi.prisma), styles['center']),
         Paragraph(str(0), styles['center']),
         Paragraph(str(m_cerca_oi.altura), styles['center'])
         ],
    ]
    t = Table([headings] + mediciones)
    t.setStyle(TableStyle(
        [
            ('GRID', (0, 0), (6, 4), 1, brown),
            ('BACKGROUND', (0, 0), (-1, 0), None)
        ]
    ))
    content.append(t)
    if receta.lente_cerca:
        tbl_data = [
            [Paragraph("CERCA", styles['dist'])],
            [
             Paragraph("MATERIAL CRISTAL", styles['center']),
             Paragraph("MODELO", styles['center']),
             Paragraph("COLOR", styles['center'])],
            [
             Paragraph(receta.lente_cerca.cristalIzq.material_cristal.nombre, styles['center']),
             Paragraph(receta.lente_cerca.cristalIzq.modelo.nombre, styles['center']),
             Paragraph(receta.lente_cerca.cristalIzq.color.nombre, styles['center'])]
        ]
        tb = Table(tbl_data)
        content.append(tb)
        if receta.lente_cerca.cristalIzq.tratamientos.count()>0:
            tratamientos = [[Paragraph("TRATAMIENTOS CRISTAL", styles['center'])]]
            for t in receta.lente_cerca.cristalIzq.tratamientos.all():
                tratamientos.append([Paragraph(t.nombre, styles['center'])])
            tb = Table(tratamientos)
            content.append(tb)
        content.append(Paragraph('Armazón: '+receta.lente_cerca.nombre+" "+str(receta.lente_cerca.codigo), styles['default']))
        content.append(Paragraph('Obs: ' + receta.lente_cerca.descripcion, styles['default']))
    if receta.lente_lejos:
        tbl_data = [
            [Paragraph("LEJOS", styles['dist'])],
            [
             Paragraph("MATERIAL CRISTAL", styles['center']),
             Paragraph("MODELO", styles['center']),
             Paragraph("COLOR", styles['center'])],
            [
             Paragraph(receta.lente_lejos.cristalIzq.material_cristal.nombre, styles['center']),
             Paragraph(receta.lente_lejos.cristalIzq.modelo.nombre, styles['center']),
             Paragraph(receta.lente_lejos.cristalIzq.color.nombre, styles['center'])]
        ]
        tb = Table(tbl_data)
        content.append(tb)
        if receta.lente_lejos.cristalIzq.tratamientos.count()>0:
            tratamientos = [[Paragraph("TRATAMIENTOS CRISTAL", styles['center'])]]
            for t in receta.lente_lejos.cristalIzq.tratamientos.all():
                tratamientos.append([Paragraph(t.nombre, styles['center'])])
            tb = Table(tratamientos)
            content.append(tb)
        content.append(Paragraph('Armazón: ' + receta.lente_lejos.nombre + " " + str(receta.lente_lejos.codigo),
                                 styles['default']))
        content.append(Paragraph('Obs: ' + receta.lente_lejos.descripcion, styles['default']))
    content.append(Paragraph('Dr.: ' + receta.doctor.usuario.first_name+" "+ receta.doctor.usuario.last_name, styles['center']))
    doc.build(content)
    response.write(buffer.getvalue())
    buffer.close()
    return response

def stylesheet():
    styles = {
        'default': ParagraphStyle(
            'default',
            fontName='Times-Roman',
            fontSize=12,
            leading=18,
            leftIndent=0,
            rightIndent=0,
            firstLineIndent=0,
            alignment=TA_LEFT,
            spaceBefore=0,
            spaceAfter=0,
            bulletFontName='Times-Roman',
            bulletFontSize=10,
            bulletIndent=0,
            textColor=brown,
            backColor=None,
            wordWrap=None,
            borderWidth=0,
            borderPadding=0,
            borderColor=None,
            borderRadius=None,
            allowWidows=1,
            allowOrphans=0,
            textTransform=None,  # 'uppercase' | 'lowercase' | None
            endDots=None,
            splitLongWords=1,
        ),
    }
    styles['title'] = ParagraphStyle(
        'title',
        parent=styles['default'],
        fontName='Helvetica-Bold',
        fontSize=14,
        leading=18,
        alignment=TA_CENTER,
        textColor=brown,
        textTransform='uppercase',
    )
    styles['center'] = ParagraphStyle(name='center', parent=styles['default'], textColor=brown, alignment=TA_CENTER)
    styles['rigth'] = ParagraphStyle(name='right', parent=styles['default'], textColor=brown, alignment=TA_RIGHT)
    styles['dist'] = ParagraphStyle(name='dist', fontName='Helvetica-Bold', parent=styles['default'], textColor=white,
                                    backColor=brown, alignment=TA_CENTER)
    return styles
