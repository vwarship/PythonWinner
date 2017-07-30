import copy
from enum import Enum

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import StyleSheet1, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib import fonts
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

_base_font_name = Font.get_font_name(Font.Name.Heiti)
_base_font_name_bold = Font.get_font_name_bold(Font.Name.Heiti)


def get_style_sheet():
    stylesheet = StyleSheet1()

    stylesheet.add(ParagraphStyle(name='Normal', fontName=_base_font_name, fontSize=10, leading=12))
    stylesheet.add(ParagraphStyle(name='BodyText', parent=stylesheet['Normal'], spaceBefore=6))
    stylesheet.add(ParagraphStyle(name='Title', parent=stylesheet['Normal'], fontName=_base_font_name_bold,
                                  fontSize=18, leading=22, alignment=TA_CENTER, spaceAfter=6), alias='title')
    stylesheet.add(ParagraphStyle(name='TableHeader', parent=stylesheet['Normal'], fontName=_base_font_name_bold,
                                  alignment=TA_CENTER))
    stylesheet.add(ParagraphStyle(name='TableBody', parent=stylesheet['Normal'], alignment=TA_CENTER))

    return stylesheet


_style_sheet = get_style_sheet()
_style_sheet_table_header = _style_sheet['TableHeader']
_style_sheet_table_body = _style_sheet['TableBody']


class Report(object):
    _table_style = TableStyle([
        ('ALIGN',(0,0),(-1,-1),'CENTER'),
        ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
        ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
        ('BOX', (0,0), (-1,-1), 0.25, colors.black),
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),  # 表头加浅灰底色
    ])

    def __init__(self, filename, pagesize=LETTER):
        self._doc = SimpleDocTemplate(filename, pagesize=pagesize)
        self._flowables = []

    def write_table(self, header, data, col_widths, table_style=_table_style):
        if not header and not data:
            return None

        data_header = [[Paragraph(cell, _style_sheet_table_header) for cell in header]]
        data_body = [[Paragraph(cell, _style_sheet_table_body) for cell in row] for row in data]

        data = data_header
        data.extend(data_body)

        table = Table(data=data, colWidths=col_widths, style=table_style)
        self._flowables.append(table)

    def pagination(self):
        self._flowables.append(FrameBreak())

    def build(self):
        self._doc.build(self._flowables)
