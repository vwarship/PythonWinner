from aip import AipNlp

from tutorial.cloud.baidu import get_key_values


aipNlp = AipNlp(*get_key_values('nlp_demo'))

result = aipNlp.lexer('百度是个搜索公司')
print(result)

# 中文词向量表示
result = aipNlp.wordEmbedding('百度')
print(result)

# 词义相似度
result = aipNlp.wordSimEmbedding('漂亮', '美丽')
print(result)

result = aipNlp.sentimentClassify('百度是一家伟大的公司')
print(result)

result = aipNlp.commentTag('面包很好吃')
print(result)
