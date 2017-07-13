"""MongoEngine
http://mongoengine.org
Tutorial: http://docs.mongoengine.org/tutorial.html
User Guide: http://docs.mongoengine.org/guide/index.html
"""


from mongoengine import *
from datetime import datetime


# 连接数据库
connect("test")


"""
EmbeddedDocument
ListField
StringField
IntField
max_length
required
"""
class Metadata(EmbeddedDocument):
    tags = ListField(StringField())
    revisions = ListField(IntField())


class WikiPage(Document):
    title = StringField(max_length=100, required=True)
    text = StringField()
    metadata = EmbeddedDocumentField(Metadata)
    create_date = DateTimeField()


"""存储"""
page = WikiPage()
page.title = "Hello, mongoengine!"
page.text = "Simple to use mongoengine."
page.metadata = Metadata(tags=["mongoengine", "mongodb"], revisions=[1])
page.create_date = datetime.now()
page.save()


"""查询"""
for page in WikiPage.objects():
    print(page.title, page.create_date)


"""
choices 指定一个属性的取值
"""
SEX = ('boy', 'girl')
class User(Document):
    name = StringField(required=True)
    age = IntField()
    sex = StringField(choices=SEX)

User(name='wjj', age=36, sex='girl').save()
