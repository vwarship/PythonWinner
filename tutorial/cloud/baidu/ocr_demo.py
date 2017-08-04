from aip import AipOcr
from tutorial.cloud.baidu import get_key_values


# 初始化ApiOcr对象
aipOcr = AipOcr(*get_key_values('ocr_demo'))


# 读取图片
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

# 定义参数变量
options = {
  'detect_direction': 'true',
  'language_type': 'CHN_ENG',
}

"""调用通用文字识别接口
Python SDK OCR的BUG [识别本地图片出错] https://developer.baidu.com/forum/topic/show?topicId=241904
测试本地文件失败，方法是修改aip里的ocr.py函数_validate，替换掉下面的代码
        # 支持url
        if re.match(r'^\w{1,128}://', data['image']):
            data['url'] = data['image']
            del data['image']
            return True

    替换后
        # 支持url
        if isinstance(data['image'], str) and re.match(r'^\w{1,128}://', data['image']):
            data['url'] = data['image']
            del data['image']
            return True

{'log_id': 3114611967, 'direction': 0, 'words_result_num': 51, 'words_result': [{'words': '3502152130'},
{'words': '厦门增铺支思发票Np9。397385'}, {'words': '3502152130'}, {'words': '00397385'}, {'words': '开票日期:2015年07月03日'},
{'words': '购'}, {'words': '称:国网湖北省电力公司物资公司'}, {'words': '密-717>5728-+254045>25899>380'},
{'words': '纳税人识别号:42010269531796X'}, {'words': '49<*2/671091/+<-80428914<8/'}, {'words': '买'},
{'words': '地址、电话:武汉市江岸区胜利街210号027-88566940'}, {'words': '码<4米1-24>+0>2/<+751555165889'},
{'words': '改方开户行及账号:湖北省武汉市中行一兀支行571657521310'}, {'words': '区/>380407<44360472>-0-8044931'},
{'words': '乐0'}, {'words': '原货物或应税劳务、服务名称'}, {'words': '规格型号|单位数量'}, {'words': '单价'}, {'words': '金领'},
{'words': '税率税额弟'}, {'words': '10kv三相隔离开关,630A,20kA,|m-12/630-P(了)-+组'}, {'words': '1024.00'},
{'words': '94208.0017%'}, {'words': '16015.36'}, {'words': '联'}, {'words': '⊙手动双柱立开式,不接地'}, {'words': '抵'},
{'words': '小游哥卡將冫'}, {'words': '￥94208.00'}, {'words': '16015.36'}, {'words': '扣联购买方扣税凭证'}, {'words': '气律军'},
{'words': '价税合计(大写)'}, {'words': '②壹拾壹万零贰佰贰拾叁圆叁角陆分'}, {'words': '(小写)￥110223,36'}, {'words': '销名'},
{'words': '称:德基申(厦门)电气有限公司'}, {'words': '订单编号:4100195105'}, {'words': '纳税人识别号'}, {'words': '350213581257081'},
{'words': '备项目名称:襄阻谷城2015年1o千伏及以k下农网建设工'}, {'words': '地址、电话:厦门市海沧区东大道2879号8#厂房2F0592-5367816'},
{'words': '程'}, {'words': '方开户行及账号:中国银行厦门市分行424760961634'}, {'words': '冫王'}, {'words': '收款人'},
{'words': '复核'}, {'words': '开票人:王小蓉'}, {'words': '销售方:(章)'}, {'words': '2'}]}
"""
img = get_file_content('../images/fapiao1.jpg')
result = aipOcr.basicGeneral(img, options)
print(result)


"""图片是URL，调用通用文字识别接口
/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6 /Users/wjj/GitHub/PythonWinner/cloud/baidu/ocr_demo.py
{'log_id': 600934086, 'direction': 0, 'words_result_num': 38, 'words_result': [{'words': '11000941'}, {'words': '40'},
{'words': '北京增值税专用发票'}, {'words': '№c87554321340062140'}, {'words': '10105292'}, {'words': '此联不作报销、扣税凭证使'},
{'words': '开票日期:2010年03月19日'}, {'words': ' fr : installing compary of chemical industry'},
{'words': '货|纳税人识别号:220301X34KTUv8X'}, {'words': '单地址、电话:东'}, {'words': '匈人位|开户行及帐号:农行西三旗办事处'},
{'words': '改货物或应税劳务名称'}, {'words': '规格型号「单位数量'}, {'words': '金额'}, {'words': '税率税额'},
{'words': '剧 Pedal leaver arm'}, {'words': ' AI 3'}, {'words': '100'}, {'words': '25.00'}, {'words': '2500.0017%'},
{'words': ' ) s / plate loaded squat .'}, {'words': '陷阳'}, {'words': '11018.181818182'}, {'words': '340.00'},
{'words': '记帐联销货方记帐凭证'}, {'words': '价税合计(大写)'}, {'words': '⑧伍仟貳佰陆拾伍圆整'}, {'words': '(小写)￥5265.00'},
{'words': '销名'}, {'words': '称:汉字防伪测试用户'}, {'words': '备正数发票'}, {'words': '货|纳税人识别号:340192 LADXK17BX'},
{'words': '单地址、电话:北京市海淀区知春路61号68744498'}, {'words': '位开户行及帐号:工行12345682342225611'},
{'words': '收款人:刘水石灰'}, {'words': '复核:刘水'}, {'words': '开票人:开票员'}, {'words': '销货单位:(章)'}]}
"""
url = 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1501581328797&di=96270575570866a9895df7f366b9e654&imgtype=0&src=http%3A%2F%2Fimg008.hc360.cn%2Fm3%2FM07%2FB5%2F79%2FwKhQ5lS9DamEQ1jYAAAAALiEQ3U691.jpg'
result = aipOcr.basicGeneral(url, options)
print(result)
