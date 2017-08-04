"""
列表推导
"""


hello = "Hello World!"


"""
chars = ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd', '!']
"""
chars = [c for c in hello]


"""
ord(c)    https://docs.python.org/3/library/functions.html?highlight=ord#ord
char_ords = [72, 101, 108, 108, 111, 32, 87, 111, 114, 108, 100, 33]
"""
char_ords = [ord(c) for c in hello]


"""带条件
char_ords = [101, 108, 108, 111, 111, 114, 108]
"""
char_ords = [ord(c) for c in hello if ord(c) > 100]


"""循环嵌套
() 元组
tshirts = [('red', 'S'), ('red', 'M'), ('red', 'L'), ('green', 'S'), ('green', 'M'), ('green', 'L'), ('blue', 'S'), ('blue', 'M'), ('blue', 'L'), ('yellow', 'S'), ('yellow', 'M'), ('yellow', 'L')]
"""
colors = ["red", "green", "blue", "yellow"]
sizes = ["S", "M", "L"]
tshirts = [(color, size) for color in colors for size in sizes]


"""列表推导式与dict构造函数结合使用
dd = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60, 7: 70, 8: 80, 9: 90}
"""
ll = [1, 2, 3, 4, 5, 6, 7, 8, 9]
dd = dict([(n, n*10) for n in ll])


"""构建字典
dd = {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D', 'e': 'E', 'f': 'F', 'g': 'G', 'h': 'H', 'i': 'I', 'j': 'J', 'k': 'K', 'l': 'L', 'm': 'M', 'n': 'N', 'o': 'O', 'p': 'P', 'q': 'Q', 'r': 'R', 's': 'S', 't': 'T', 'u': 'U', 'v': 'V', 'w': 'W', 'x': 'X', 'y': 'Y', 'z': 'Z'}
"""
dd = {char:char.upper() for char in 'abcdefghijklmnopqrstuvwxyz'}


"""构建集合
ss = {'I', 'Z', 'D', 'O', 'M', 'A', 'K', 'W', 'Q', 'H', 'S', 'V', 'C', 'B', 'Y', 'T', 'G', 'J', 'P', 'N', 'L', 'X', 'F', 'R', 'U', 'E'}
"""
ss = {char.upper() for char in 'abcdefghijklmnopqrstuvwxyz'}
