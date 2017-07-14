"""
函数
"""


"""阶乘函数"""
def factorial(n):
    return 1 if n < 2 else n * factorial(n-1)


fact = factorial


"""map函数返回一个可迭代对象，第一个参数应用到第二个参数中各个元素上得到的结果"""
print(list(map(factorial, range(1, 11))))   # [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]

