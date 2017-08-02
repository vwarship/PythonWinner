from reportlab.pdfgen import canvas

from tutorial.myreportlib import *


c = canvas.Canvas(pdf_filename)
c.drawString(100, 600, "Hello World")
c.showPage()
c.save()
