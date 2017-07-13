"""
列表推导
"""

hello = "Hello World!"

# chars = ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd', '!']
chars = [c for c in hello]

# ord(c)    https://docs.python.org/3/library/functions.html?highlight=ord#ord
# char_ords = [72, 101, 108, 108, 111, 32, 87, 111, 114, 108, 100, 33]
char_ords = [ord(c) for c in hello]

# char_ords = [101, 108, 108, 111, 111, 114, 108]
char_ords = [ord(c) for c in hello if ord(c) > 100]

# () 元组
# tshirts = [('red', 'S'), ('red', 'M'), ('red', 'L'), ('green', 'S'), ('green', 'M'), ('green', 'L'), ('blue', 'S'), ('blue', 'M'), ('blue', 'L'), ('yellow', 'S'), ('yellow', 'M'), ('yellow', 'L')]
colors = ["red", "green", "blue", "yellow"]
sizes = ["S", "M", "L"]
tshirts = [(color, size) for color in colors for size in sizes]

