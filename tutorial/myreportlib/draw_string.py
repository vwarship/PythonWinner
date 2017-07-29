from tutorial.myreportlib import *

from reportlab.pdfgen import canvas


c = canvas.Canvas(pdf_filename)
c.drawString(100, 600, "Hello World")
c.showPage()
c.save()
