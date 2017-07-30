from reportlab.lib.pagesizes import LETTER
from reportlab.platypus import SimpleDocTemplate, Table
from reportlab.lib import colors
from reportlab.lib.units import inch

data = [['00', '01', '02', '03', '04'],
        ['10', '11', '12', '13', '14'],
        ['20', '21', '22', '23', '24'],
        ['30', '31', '32', '33', '34']]

table = Table(data, colWidths=inch, rowHeights=inch,
              style=[('GRID', (0, 0), (-1, -1), 0.5, colors.grey),  # 画网格的线
                     ('INNERGRID', (2, 0), (-1, 1), 1, colors.green),  # 画网格里的线
                     ('ALIGN', (0, 0), (0, -1), 'CENTER'),
                     ('VALIGN', (0, 0), (0, -1), 'MIDDLE'),
                     ('BOX', (0, 0), (1, -1), 2, colors.red),   # 画外框的线
                     ('BOX', (2, 0), (-1, -1), 2, colors.black),
                     ('LINEABOVE', (1, 2), (-2, 2), 1, colors.blue),    # 上面画线
                     ('LINEBEFORE', (2, 1), (2, -2), 1, colors.pink),   # 左边画线
                     ('TEXTCOLOR', (-1, 0), (-1, -1), colors.red),  # 文本颜色
                     ('BACKGROUND', (0, 0), (0, 1), colors.red),    # 背景颜色
                     ('BACKGROUND', (1, 1), (1, 2), colors.green),
                     ('BACKGROUND', (2, 2), (2, 3), colors.blue),
                     ])

doc = SimpleDocTemplate('test.pdf', pagesize=LETTER)
doc.build([table])
