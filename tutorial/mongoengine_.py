"""MongoEngine
http://mongoengine.org
Tutorial: http://docs.mongoengine.org/tutorial.html
User Guide: http://docs.mongoengine.org/guide/index.html
"""


from mongoengine import *
from datetime import datetime
from datetime import date


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
# for page in WikiPage.objects():
#     print(page.title, page.create_date)


"""
choices 指定一个属性的取值
default 设置默认值
"""
SEX = ('boy', 'girl')
class User(Document):
    name = StringField(required=True)
    age = IntField()
    sex = StringField(choices=SEX)
    birthday = DateTimeField(default=datetime.now())


"""移除User所有文档"""
User.drop_collection()


"""创建多个User文档"""
users = [('wjj', 36, 'boy', date(1981, 1, 1)),
         ('wrj', 8, 'boy', date(2009, 1, 1)),
         ('ns', 20, 'girl', date(1998, 1, 1))]
for user in users:
    User(*user).save()


"""取文档个数"""
count = User.objects().count()
print(count)    # 3


"""distinct"""
sexs = User.objects().distinct(field='sex')
print(sexs) # ['boy', 'girl']


"""查询"""
User.objects(name='wjj')    # =
User.objects(age__gt=20)    # >
User.objects(age__gte=20)   # >=
User.objects(age__lt=20)    # <
User.objects(age__lte=20)   # <=
User.objects(age__ne=20)    # !=
User.objects(birthday__gte=date(1998, 1, 1))    # >= date
User.objects(sex__in=['boy', 'girl'])   # in
User.objects(sex__nin=['girl']) # nin


"""排序"""
User.objects().order_by("age")  # 升序排列
User.objects().order_by("-age") # 降序排列


"""limit skip"""
User.objects().limit(1)
User.objects().skip(1).limit(1)

