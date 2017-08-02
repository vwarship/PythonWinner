from reportlab.lib.pagesizes import LETTER
from reportlab.platypus import SimpleDocTemplate, Table, Image
from reportlab.lib import colors
from reportlab.lib.units import inch


logo = 'python-logo.png'
img = Image(logo)
new_width = 60
img.drawHeight = new_width * img.drawHeight / img.drawWidth
img.drawWidth = new_width

data = [[img, '01', '02', '03', '04'],
        [img, '11', '12', '13', '14'],
        [img, '21', '22', '23', '24'],
        [img, '31', '32', '33', '34']]

table = Table(data, colWidths=inch, rowHeights=inch,
              style=[('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
                     ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                     ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                     ])

doc = SimpleDocTemplate('test.pdf', pagesize=LETTER)
doc.build([table])
