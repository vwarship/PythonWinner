"""map(function, iterable)"""
ll = list(map(lambda name: 'Hi ' + name + '!', ['Jack', 'Lili']))
print(ll)   # ['Hi Jack!', 'Hi Lili!']

"""Python3 推荐使用下面的列表推导来完成上面的功能"""
ll = ['Hi ' + name + '!' for name in ['Jack', 'Lili']]
print(ll)   # ['Hi Jack!', 'Hi Lili!']