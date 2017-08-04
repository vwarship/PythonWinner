from enum import Enum

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import StyleSheet1, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib import fonts
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import LETTER
from reportlab.platypus import Paragraph, SimpleDocTemplate, Table, TableStyle, FrameBreak


class Font(object):
    class Name(Enum):
        Heiti = 'Heiti'
        Songti = 'Songti'

    @classmethod
    def register_font(cls):
        # 宋体-简
        # 正常、斜体、粗体等都在一个字体文件里，需要使用subfontIndex
        pdfmetrics.registerFont(TTFont('Songti', 'Songti.ttc', subfontIndex=3))
        pdfmetrics.registerFont(TTFont('Songti-Italic', 'Songti.ttc', subfontIndex=2))
        pdfmetrics.registerFont(TTFont('Songti-Bold', 'Songti.ttc', subfontIndex=1))
        pdfmetrics.registerFont(TTFont('Songti-BoldItalic', 'Songti.ttc', subfontIndex=0))

        # 黑体-简
        pdfmetrics.registerFont(TTFont('Heiti', 'STHeiti Light.ttc'))
        pdfmetrics.registerFont(TTFont('Heiti-Bold', 'STHeiti Medium.ttc'))

    @classmethod
    def add_mapping(cls):
        fonts.addMapping(Font.Name.Songti.value, 0, 0, 'Songti')
        fonts.addMapping(Font.Name.Songti.value, 0, 1, 'Songti-Italic')
        fonts.addMapping(Font.Name.Songti.value, 1, 0, 'Songti-Bold')
        fonts.addMapping(Font.Name.Songti.value, 1, 1, 'Songti-BoldItalic')

        fonts.addMapping(Font.Name.Heiti.value, 0, 0, 'Heiti')
        fonts.addMapping(Font.Name.Heiti.value, 1, 0, 'Heiti-Bold')

    @classmethod
    def get_font_name(cls, font_name):
        return fonts.tt2ps(font_name.value, 0, 0)

    @classmethod
    def get_font_name_bold(cls, font_name):
        return fonts.tt2ps(font_name.value, 1, 0)


Font.register_font()
Font.add_mapping()


class Report(object):
    _table_style = TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
        ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),  # 表头加浅灰底色
    ])

    def __init__(self, filename, pagesize=LETTER):
        self.filename = filename
        self.pagesize = pagesize
        self.width, self.height = self.pagesize
        self.header = ''
        self.footer = ''

        self._base_font_name = Font.get_font_name(Font.Name.Heiti)
        self._base_font_name_bold = Font.get_font_name_bold(Font.Name.Heiti)

        style_sheet = self.get_style_sheet()
        self._style_table_header = style_sheet['TableHeader']
        self._style_table_body = style_sheet['TableBody']
        self._style_header = style_sheet['Header']
        self._style_footer = style_sheet['Footer']

        self._doc = SimpleDocTemplate(filename,
                                      rightMargin=inch / 2,
                                      leftMargin=inch / 2,
                                      topMargin=inch / 2,
                                      bottomMargin=inch / 2,
                                      pagesize=pagesize)
        self._flowables = []

    def get_style_sheet(self):
        stylesheet = StyleSheet1()

        stylesheet.add(ParagraphStyle(name='Normal', fontName=self._base_font_name, fontSize=10, leading=12))
        stylesheet.add(ParagraphStyle(name='BodyText', parent=stylesheet['Normal'], spaceBefore=6))
        stylesheet.add(ParagraphStyle(name='Title', parent=stylesheet['Normal'], fontName=self._base_font_name_bold,
                                      fontSize=18, leading=22, alignment=TA_CENTER, spaceAfter=6), alias='title')
        stylesheet.add(ParagraphStyle(name='TableHeader', parent=stylesheet['Normal'], fontName=self._base_font_name_bold,
                                      alignment=TA_CENTER))
        stylesheet.add(ParagraphStyle(name='TableBody', parent=stylesheet['Normal'], alignment=TA_CENTER))
        stylesheet.add(ParagraphStyle(name='Header', parent=stylesheet['Normal'], fontName=self._base_font_name_bold,
                                      fontSize=18, leading=22, textColor=colors.green, alias='header'))
        stylesheet.add(ParagraphStyle(name='Footer', parent=stylesheet['Normal'],
                                      textColor=colors.green, alias='footer'))

        return stylesheet

    def _header_footer(self, canvas, doc):
        # Save the state of our canvas so we can draw on it
        canvas.saveState()

        canvas.setStrokeColor(colors.orange)
        canvas.setLineWidth(0.5)

        # Header
        header = Paragraph(self.header, self._style_header)
        w, h = header.wrap(doc.width, doc.topMargin)
        header.drawOn(canvas, doc.leftMargin, doc.height + doc.bottomMargin)
        canvas.line(doc.leftMargin, self.height-doc.topMargin, self.width-doc.rightMargin, self.height-doc.topMargin)

        # Footer
        footer_format = '{} 页面{}'
        footer_text = footer_format.format(self.footer, doc.page)
        footer = Paragraph(footer_text, self._style_footer)
        w, h = footer.wrap(doc.width, doc.bottomMargin)
        footer.drawOn(canvas, doc.leftMargin, h)
        canvas.line(doc.leftMargin, doc.bottomMargin, self.width-doc.rightMargin, doc.bottomMargin)

        # Release the canvas
        canvas.restoreState()

    def write_table(self, header, data, col_widths, table_style=_table_style):
        if not header and not data:
            return None

        data_header = [[Paragraph(cell, self._style_table_header) for cell in header]]
        data_body = [[Paragraph(cell, self._style_table_body) for cell in row] for row in data]

        data = data_header
        data.extend(data_body)

        table = Table(data=data, colWidths=col_widths, style=table_style)
        self._flowables.append(table)

    def pagination(self):
        self._flowables.append(FrameBreak())

    def build(self):
        self._doc.build(self._flowables, onFirstPage=self._header_footer, onLaterPages=self._header_footer)
