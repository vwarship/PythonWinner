from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import mm, inch
from reportlab.platypus import Paragraph, SimpleDocTemplate, FrameBreak

from tutorial.myreportlib import *


class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        canvas.Canvas.__init__(self, *args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        """add page info to each page (page x of y)"""
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_number(num_pages)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

    def draw_page_number(self, page_count):
        # Change the position of this to wherever you want the page number to be
        self.drawRightString(211 * mm, 15 * mm + (0.2 * inch),
                             "Page %d of %d" % (self._pageNumber, page_count))


text_page1 = 'Hello World!'
text_page2 = 'How are you.'

style = getSampleStyleSheet()['Normal']

flowables = []
flowables.append(Paragraph(text_page1, style))
flowables.append(FrameBreak())
flowables.append(Paragraph(text_page2, style))

doc = SimpleDocTemplate(pdf_filename, pagesize=letter)
doc.build(flowables, canvasmaker=NumberedCanvas)
