from tutorial.myreportlib import *

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Paragraph, SimpleDocTemplate, FrameBreak

style = getSampleStyleSheet()['Normal']


def header_footer(canvas, doc):
    # Save the state of our canvas so we can draw on it
    canvas.saveState()

    # Header
    header = Paragraph('This is a header.', style)
    w, h = header.wrap(doc.width, doc.topMargin)
    header.drawOn(canvas, doc.leftMargin, doc.height + doc.bottomMargin)

    # Footer
    footer = Paragraph('This is a footer.', style)
    w, h = footer.wrap(doc.width, doc.bottomMargin)
    footer.drawOn(canvas, doc.leftMargin, h)

    # Release the canvas
    canvas.restoreState()


text = 'Last time we looked at how to generate a very simple PDF using ReportLab and Django, ReportLab and Django – Part 1 – The Set Up and a Basic Example.  This time let’s make the PDF a little bit more interesting with some headers and footers.  ReportLab gives a pretty good amount of control when it comes to adding headers and footers to your PDF.  To start off let’s bring back the simple __init__ method we had from last time and add a header/footer method to it.' * 20

doc = SimpleDocTemplate(pdf_filename, pagesize=letter)
doc.build([Paragraph(text, style)],
          onFirstPage=header_footer,
          onLaterPages=header_footer)
