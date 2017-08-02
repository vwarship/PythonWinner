# 钻石形的继承体系


class Base(object):
    def __init__(self, x):
        self.x = x


class One(Base):
    def __init__(self, x):
        super().__init__(x)
        self.x += 1


class Two(Base):
    def __init__(self, x):
        super().__init__(x)
        self.x *= 2


class Three(One, Two):
    def __init__(self, x):
        super().__init__(x)
        self.x *= 3

# [<class '__main__.Three'>, <class '__main__.One'>, <class '__main__.Two'>, <class '__main__.Base'>, <class 'object'>]
print(Three.mro())

"""
(5*2+1)*3 = 33 根据MRO反向的顺序计算
"""
t = Three(5)
print(t.x)  # 33