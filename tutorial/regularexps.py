"""
正则表达式
"""
import re


"""移除所有html标签"""
html = "<html><head><title>HI</title></head> <body><div>Hello World</div></body></html>"
text = re.compile(r'<[^>]+>').sub('', html) # HI Hello World


"""利用所有非字母字符拆分出单词"""
words = re.compile(r'[^A-Z^a-z]+').split(text)  # ['HI', 'Hello', 'World']
