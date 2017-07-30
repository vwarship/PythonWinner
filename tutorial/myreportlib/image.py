from tutorial.myreportlib import *

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Image

text = 'Hello World!'

style = getSampleStyleSheet()['Normal']

logo = 'python-logo.png'
img1 = Image(logo)

# 等比例缩放
new_width = 8 * inch
img2 = Image(logo)
img2.drawHeight = new_width * img2.drawHeight / img2.drawWidth
img2.drawWidth = new_width

flowables = []
flowables.append(img1)
flowables.append(img2)
flowables.append(Spacer(1, 20))
flowables.append(Paragraph(text, style))

doc = SimpleDocTemplate(pdf_filename, pagesize=letter)
doc.build(flowables)
