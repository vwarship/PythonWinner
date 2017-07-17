"""
函数
"""


"""阶乘函数"""
def factorial(n):
    return 1 if n < 2 else n * factorial(n-1)


fact = factorial


"""map函数返回一个可迭代对象，第一个参数应用到第二个参数中各个元素上得到的结果"""
print(list(map(factorial, range(1, 11))))   # [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]


"""获得函数的属性
['__annotations__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__',
'__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__globals__', '__gt__',
'__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__',
'__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
"""
dir(factorial)


"""判断对象是否可能调用"""
callable(factorial)


"""添加函数的属性"""
factorial.test = "TEST"
factorial.test

