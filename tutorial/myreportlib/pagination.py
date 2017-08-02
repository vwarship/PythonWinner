from tutorial.myreportlib import *

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Paragraph, SimpleDocTemplate, FrameBreak

text_page1 = 'Hello World!'
text_page2 = 'How are you.'

style = getSampleStyleSheet()['Normal']

flowables = []
flowables.append(Paragraph(text_page1, style))
flowables.append(FrameBreak())
flowables.append(Paragraph(text_page2, style))

doc = SimpleDocTemplate(pdf_filename, pagesize=letter)
doc.build(flowables)
