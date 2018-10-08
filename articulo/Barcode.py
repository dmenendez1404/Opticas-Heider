from base64 import b64encode
from reportlab.lib import units
from reportlab.graphics import renderPM
from reportlab.graphics.barcode import *
from reportlab.graphics.shapes import Drawing

def get_barcode(value, width, barWidth = 0.05 * units.inch, fontSize = 30, humanReadable = True):
    barcode = createBarcodeDrawing('Code128', value = value, barWidth = barWidth, fontSize = fontSize, humanReadable = humanReadable)
    drawing_width = width
    barcode_scale = drawing_width / barcode.width
    drawing_height = barcode.height * barcode_scale
    drawing = Drawing(drawing_width, drawing_height)
    drawing.scale(barcode_scale, barcode_scale)
    drawing.add(barcode,name=value)

    return drawing

def get_image(codigo):
    barcode = get_barcode(value = codigo, width = 300)
    data = b64encode(renderPM.drawToString(barcode, fmt = 'PNG'))
    return data
