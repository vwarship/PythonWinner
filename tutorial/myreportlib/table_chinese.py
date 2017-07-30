import copy

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib import fonts
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Paragraph, SimpleDocTemplate, Table, TableStyle

pdfmetrics.registerFont(TTFont('Heiti', 'STHeiti Light.ttc'))
pdfmetrics.registerFont(TTFont('Heiti-Bold', 'STHeiti Medium.ttc'))

fonts.addMapping('heiti', 0, 0, 'Heiti')
fonts.addMapping('heiti', 1, 0, 'Heiti-Bold')

heiti_font_name = fonts.tt2ps('heiti', 0, 0)
heiti_font_name_b = fonts.tt2ps(heiti_font_name, 1, 0)

style = copy.deepcopy(getSampleStyleSheet()['Normal'])
style.fontName = heiti_font_name
style.alignment = TA_CENTER

style_bold = copy.deepcopy(getSampleStyleSheet()['Normal'])
style_bold.fontName = heiti_font_name_b
style_bold.alignment = TA_CENTER

data = [['股票代码', '股票名称', '调研机构'],
        ['000981', '银亿股份', '证券时报 ‖ 每日经济新闻 ‖ 21世纪经济报道 ‖ 东方财富网 ‖ 大众证券报 ‖ 中国经营报 ‖ 华夏时报 ‖ 时代周刊 ‖ 新闻晨报 ‖ 宁波日报 ‖ 宁波晚报 ‖ 东南商报 ‖ 金陵晚报 ‖ 扬子晚报 ‖ 现代快报 ‖ 人民网 ‖ 网易 ‖ 中国新闻网 ‖ 财联社 ‖ 盖世汽车 ‖ 汽车之家 ‖ 汽车与配件 ‖ 荣格工业 ‖ 汽车经营与服务 ‖ 汽车通讯社 ‖ 买车大师 ‖ 猫扑网 ‖ 环球汽车网 ‖ 上海汽车报 ‖ 汽车财经报 ‖ 汽车之友 ‖ 汽车导购 ‖ 驾修杂志 ‖ 车讯 ‖ 中国汽车报 ‖ 乐居网 ‖ 三六五网'],
        ['600887', '伊利股份', 'Point72 Asset Management ‖ 挪威银行'],
        ['300097', '智云股份', '招商证券 ‖ 长江养老保险东兴证券 ‖ 光证资管'],
        ['300142', '沃森生物', '东吴证券'],
        ['300072', '三聚环保', '荷宝投资管理集团 ‖ 西京投资管理(香港)有限公司 ‖ 行健资产管理有限公司 ‖ KB Asset Management ‖ 中央再保险股份有限公司 ‖ 挪威银行上海代表处 ‖ 中国国际金融股份有限公司 ‖ 中银基金管理有限公司 ‖ 国泰人寿保险有限责任公司 ‖ American Century Investments ‖ 太平洋资产管理有限责任公司'],
        ['000333', '美的集团', '瑞银资产 ‖ 摩根资管 ‖ 才华资本 ‖ 景顺长城 ‖ 兰馨亚洲 ‖ 未来资产 ‖ 宝盈基金 ‖ 千合资本 ‖ 汇添富基金 ‖ 信诚基金 ‖ 新华基金 ‖ 兴全基金 ‖ 泰康资产 ‖ 风和资产 ‖ 华恒投资 ‖ 大和投资 ‖ 交银施罗德 ‖ 景林资产 ‖ 华安基金 ‖ 复星投资 ‖ 国泰金控 ‖ 中环资产 ‖ 弘鼎资本 ‖ 海富通基金 ‖ 惠理基金 ‖ 上海行知创业 ‖ 复华投信 ‖ 野村投资 ‖ 马来西亚国家银行 ‖ 中国人保 ‖ 瀚伦投资 ‖ 第一北京公司 ‖ 纳静资产 ‖ 毕盛投资 ‖ 银河投资 ‖ 泰达宏利基金 ‖ 长城财富资产 ‖ 中海基金 ‖ 华商基金 ‖ 中邮基金 ‖ 华泰资管 ‖ 嘉实基金 ‖ 华中资本 ‖ 富国基金 ‖ 紫金保险 ‖ 国联人寿 ‖ 清和泉资本 ‖ 信达证券 ‖ 中信资管 ‖ 国投瑞银 ‖ 财通证券 ‖ 安信信托 ‖ Wells Fargo ‖ UG Investment ‖ Matthews Asia ‖ American Century Investments ‖ Meritz Asset Management ‖ Baring Asset Management ‖ Credit Suisse PB & Wealth Mgmt ‖ Point72 Asset Management ‖ Bosvalen Asset Management ‖ CQS (Hong Kong) Ltd. ‖ Deepwater Capital ‖ Deutsche Asset Management Asia Ltd ‖ Giant Redwood Assets ‖ Miura Global Management ‖ Morgan Stanley Investment Management (SNG) ‖ Optimas Capital Limited ‖ Comgest Far East Ltd ‖ Invesco Hong Kong Limited ‖ Invesco Trimark Investments ‖ Wellington Global Investment Management Company Ltd ‖ Canada Pension Plan Investment Board ‖ Pictet Asia Ltd ‖ 弘尚资产'],
        ]

data_header = [[Paragraph(cell, style_bold) for cell in row] for row in data[:1]]
data_body = [[Paragraph(cell, style) for cell in row] for row in data[1:]]

data2 = data_header
data2.extend(data_body)

table = Table(data2, colWidths=[60, 60, 400])

# 画表格的线
table.setStyle(TableStyle([
    ('ALIGN',(0,0),(-1,-1),'CENTER'),
    ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
    ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
    ('BOX', (0,0), (-1,-1), 0.25, colors.black),
    ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),  # 表头加浅灰底色
]))

doc = SimpleDocTemplate('test.pdf',pagesize=letter)
doc.build([table])
