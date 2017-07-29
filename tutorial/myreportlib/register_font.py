from tutorial.myreportlib import *

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import fonts
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Paragraph, SimpleDocTemplate

# 英文字体 Arial
# 建立字体的映射关系 registerFont => addMapping => tt2ps
pdfmetrics.registerFont(TTFont('Arial', 'Arial.ttf'))
pdfmetrics.registerFont(TTFont('Arial-Italic', 'Arial Italic.ttf'))
pdfmetrics.registerFont(TTFont('Arial-Bold', 'Arial Bold.ttf'))
pdfmetrics.registerFont(TTFont('Arial-BoldItalic', 'Arial Bold Italic.ttf'))

fonts.addMapping('arial', 0, 0, 'Arial')
fonts.addMapping('arial', 0, 1, 'Arial-Italic')
fonts.addMapping('arial', 1, 0, 'Arial-Bold')
fonts.addMapping('arial', 1, 1, 'Arial-BoldItalic')

arial_font_name = fonts.tt2ps('arial', 0, 0)
arial_font_name_i = fonts.tt2ps(arial_font_name, 0, 1)
arial_font_name_b = fonts.tt2ps(arial_font_name, 1, 0)
arial_font_name_bi = fonts.tt2ps(arial_font_name, 1, 1)

# 中文字体 宋体-简
# 正常、斜体、粗体等都在一个字体文件里，需要使用subfontIndex
pdfmetrics.registerFont(TTFont('Songti', 'Songti.ttc', subfontIndex=3))
pdfmetrics.registerFont(TTFont('Songti-Italic', 'Songti.ttc', subfontIndex=2))
pdfmetrics.registerFont(TTFont('Songti-Bold', 'Songti.ttc', subfontIndex=1))
pdfmetrics.registerFont(TTFont('Songti-BoldItalic', 'Songti.ttc', subfontIndex=0))

fonts.addMapping('songti', 0, 0, 'Songti')
fonts.addMapping('songti', 0, 1, 'Songti-Italic')
fonts.addMapping('songti', 1, 0, 'Songti-Bold')
fonts.addMapping('songti', 1, 1, 'Songti-BoldItalic')

songti_font_name = fonts.tt2ps('songti', 0, 0)
songti_font_name_i = fonts.tt2ps(songti_font_name, 0, 1)
songti_font_name_b = fonts.tt2ps(songti_font_name, 1, 0)
songti_font_name_bi = fonts.tt2ps(songti_font_name, 1, 1)

text = 'Hello World!'
text_cn = '您好!'

flowables = []

for font_name in [arial_font_name, arial_font_name_i, arial_font_name_b, arial_font_name_bi]:
    style = getSampleStyleSheet()['Normal']
    style.fontName = font_name
    flowables.append(Paragraph(text, style))

for font_name in [songti_font_name, songti_font_name_i, songti_font_name_b, songti_font_name_bi]:
    style = getSampleStyleSheet()['Normal']
    style.fontName = font_name
    flowables.append(Paragraph(text_cn, style))

doc = SimpleDocTemplate(pdf_filename, pagesize=letter)
doc.build(flowables)
