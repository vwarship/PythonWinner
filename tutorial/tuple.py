"""
元组
"""

wjj = ("wjj", 36)

# _ 占位符
peoples = [("wjj", 36), ("wrj", 8)]
for name, _ in peoples:
    print(name)

# 不使用中间变量交换两个变量的值
x = 1
y = 2
y, x = x, y

# 元组拆包
name, age = wjj

# * 元组拆包
def sum(x, y):
    return x+y
t = (2, 3)
sum(*t)

# * 赋值
# 0 1 [2, 3, 4]
a, b, *c = range(5)
# 0 [1, 2, 3] 4
a, *b, c = range(5)
# [0, 1, 2] 3 4
*a, b, c = range(5)
