from winner.utils.reportlib_util import Report
from winner.utils.datetime_util import get_current_date_str


header = ['股票代码', '股票名称', '调研机构']
data = [['000981', '银亿股份', '证券时报 ‖ 每日经济新闻 ‖ 21世纪经济报道 ‖ 东方财富网 ‖ 大众证券报 ‖ 中国经营报 ‖ 华夏时报 ‖ 时代周刊 ‖ 新闻晨报 ‖ 宁波日报 ‖ 宁波晚报 ‖ 东南商报 ‖ 金陵晚报 ‖ 扬子晚报 ‖ 现代快报 ‖ 人民网 ‖ 网易 ‖ 中国新闻网 ‖ 财联社 ‖ 盖世汽车 ‖ 汽车之家 ‖ 汽车与配件 ‖ 荣格工业 ‖ 汽车经营与服务 ‖ 汽车通讯社 ‖ 买车大师 ‖ 猫扑网 ‖ 环球汽车网 ‖ 上海汽车报 ‖ 汽车财经报 ‖ 汽车之友 ‖ 汽车导购 ‖ 驾修杂志 ‖ 车讯 ‖ 中国汽车报 ‖ 乐居网 ‖ 三六五网'],
        ['600887', '伊利股份', 'Point72 Asset Management ‖ 挪威银行'],
        ['300097', '智云股份', '招商证券 ‖ 长江养老保险东兴证券 ‖ 光证资管'],
        ['300142', '沃森生物', '东吴证券'],
        ['300072', '三聚环保', '荷宝投资管理集团 ‖ 西京投资管理(香港)有限公司 ‖ 行健资产管理有限公司 ‖ KB Asset Management ‖ 中央再保险股份有限公司 ‖ 挪威银行上海代表处 ‖ 中国国际金融股份有限公司 ‖ 中银基金管理有限公司 ‖ 国泰人寿保险有限责任公司 ‖ American Century Investments ‖ 太平洋资产管理有限责任公司'],
        ['000333', '美的集团', '瑞银资产 ‖ 摩根资管 ‖ 才华资本 ‖ 景顺长城 ‖ 兰馨亚洲 ‖ 未来资产 ‖ 宝盈基金 ‖ 千合资本 ‖ 汇添富基金 ‖ 信诚基金 ‖ 新华基金 ‖ 兴全基金 ‖ 泰康资产 ‖ 风和资产 ‖ 华恒投资 ‖ 大和投资 ‖ 交银施罗德 ‖ 景林资产 ‖ 华安基金 ‖ 复星投资 ‖ 国泰金控 ‖ 中环资产 ‖ 弘鼎资本 ‖ 海富通基金 ‖ 惠理基金 ‖ 上海行知创业 ‖ 复华投信 ‖ 野村投资 ‖ 马来西亚国家银行 ‖ 中国人保 ‖ 瀚伦投资 ‖ 第一北京公司 ‖ 纳静资产 ‖ 毕盛投资 ‖ 银河投资 ‖ 泰达宏利基金 ‖ 长城财富资产 ‖ 中海基金 ‖ 华商基金 ‖ 中邮基金 ‖ 华泰资管 ‖ 嘉实基金 ‖ 华中资本 ‖ 富国基金 ‖ 紫金保险 ‖ 国联人寿 ‖ 清和泉资本 ‖ 信达证券 ‖ 中信资管 ‖ 国投瑞银 ‖ 财通证券 ‖ 安信信托 ‖ Wells Fargo ‖ UG Investment ‖ Matthews Asia ‖ American Century Investments ‖ Meritz Asset Management ‖ Baring Asset Management ‖ Credit Suisse PB & Wealth Mgmt ‖ Point72 Asset Management ‖ Bosvalen Asset Management ‖ CQS (Hong Kong) Ltd. ‖ Deepwater Capital ‖ Deutsche Asset Management Asia Ltd ‖ Giant Redwood Assets ‖ Miura Global Management ‖ Morgan Stanley Investment Management (SNG) ‖ Optimas Capital Limited ‖ Comgest Far East Ltd ‖ Invesco Hong Kong Limited ‖ Invesco Trimark Investments ‖ Wellington Global Investment Management Company Ltd ‖ Canada Pension Plan Investment Board ‖ Pictet Asia Ltd ‖ 弘尚资产'],
        ['002781', '奇信股份', '东北证券 ‖ 海通证券 ‖ 华泰证券 ‖ 证券时报 ‖ 上海证券报 ‖ 中国证券报 ‖ 证券日报 ‖ 每日经济新闻 ‖ 第一财经日报 ‖ 和讯网 ‖ 金融界 ‖ 新财富 ‖ 全景网 ‖ e公司 ‖ 机会宝 ‖ 深圳卫视财经频道 ‖ 深圳卫视公共频道'],
        ['300445', '康斯特', '长城国瑞证券 ‖ 鑫翰通航投资 ‖ 云齐资本'],
        ['300554', '三超新材', '西南证券'],
        ['000100', 'TCL集团', 'BlackRock资产管理公司 ‖ 瑞银证券'],
        ['002711', '欧浦智网', '中科沃土基金 ‖ 和君资本 ‖ 星石投资 ‖ 鑫鼎盛期货 ‖ 不繁资本 ‖ 开源资管 ‖ 海通证券 ‖ 光大证券 ‖ 长江证券 ‖ 广发证券 ‖ 安信证券 ‖ 国元证券 ‖ 国海证券 ‖ 新价值投资 ‖ 价值在线 ‖ 陕西国际信托 ‖ 永通重机'],
        ['300450', '先导智能', '安信证券股份有限公司 ‖ 中泰证券股份有限公司 ‖ 上海朴道瑞富投资管理中心 ‖ 泓德基金管理有限公司 ‖ 君禾股权投资基金管理(上海)有限公司 ‖ 知行投资管理有限公司 ‖ 东兴证券股份有限公司 ‖ 中信建投证券股份有限公司 ‖ 北京中青科豪投资有限公司 ‖ 景顺长城基金管理有限公司'],
        ['300355', '蒙草生态', '安信证券 ‖ 国泰基金 ‖ 华泰证券 ‖ 东北证券 ‖ 中信建投 ‖ 中泰证券'],
        ['603168', '莎普爱思', '海通证券'],
        ['002839', '张家港行', '华泰证券 ‖ 平安信托'],
        ['000776', '广发证券', '富邦综合证券股份有限公司 ‖ Athena Capital Management'],
        ]

col_widths = [60, 60, 400]
report = Report('test.pdf')
report.header = '☺狗吃草智投 ☼{}'.format(get_current_date_str())
report.footer = '人工智能投资报告'
report.write_table(header, data, col_widths)
report.build()
