from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch

from tutorial.myreportlib import *


PAGE_HEIGHT, PAGE_WIDTH = LETTER
styles = getSampleStyleSheet()

Title = "Hello world"
pageinfo = "platypus example"


def myFirstPage(canvas, doc):
   canvas.saveState()
   canvas.setFont('Times-Bold',16)
   canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-108, Title)
   canvas.setFont('Times-Roman',9)
   canvas.drawString(inch, 0.75 * inch, "First Page / %s" % pageinfo)
   canvas.restoreState()


def myLaterPages(canvas, doc):
    canvas.saveState()
    canvas.setFont('Times-Roman', 9)
    canvas.drawString(inch, 0.75 * inch, "Page %d %s" % (doc.page, pageinfo))
    canvas.restoreState()


def go():
    doc = SimpleDocTemplate(pdf_filename)
    Story = [Spacer(1, 2 * inch)]
    style = styles["Normal"]
    for i in range(100):
        bogustext = ("This is Paragraph number %s.  " % i) * 20
        p = Paragraph(bogustext, style)
        Story.append(p)
        Story.append(Spacer(1, 0.2 * inch))
    doc.build(Story, onFirstPage=myFirstPage, onLaterPages=myLaterPages)

go()
