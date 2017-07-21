"""
正则表达式
"""
import re
import reprlib


"""移除所有html标签"""
html = "<html><head><title>HI</title></head> <body><div>Hello World</div></body></html>"
text = re.compile(r'<[^>]+>').sub('', html) # HI Hello World


"""利用所有非字母字符拆分出单词"""
words = re.compile(r'[^A-Z^a-z]+').split(text)  # ['HI', 'Hello', 'World']


"""取出所有的单词"""
text = 'If keys, values and items views are iterated over with no intervening modifications to the dictionary, the order of items will directly correspond.'
word_pattern = re.compile('\w+')
words = word_pattern.findall(text)  # ['If', 'keys', 'values', 'and', 'items', 'views', 'are', 'iterated', 'over', 'with', 'no', 'intervening', 'modifications', 'to', 'the', 'dictionary', 'the', 'order', 'of', 'items', 'will', 'directly', 'correspond']


"""生成字符串的简略表示形式（不会超过30个字符）"""
reprlib.repr(text)  # 'If keys, val...y correspond.'

