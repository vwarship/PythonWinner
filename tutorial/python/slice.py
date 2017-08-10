"""[start:stop:step]"""
s = 'bicycle'
print(s[2:])    # cycle
print(s[2:5])   # cyc
print(s[2::2])  # cce
print(s[::3])   # bye
print(s[::-1])  # elcycib
print(s[::-2])  # eccb


"""切片对象
wjj 36
wrj  8
"""
datas = ['wjj 36', 'wrj  8']
NAME = slice(0, 3)
AGE = slice(4, 6)
for data in datas:
    print(data[NAME], data[AGE])


"""给切片赋值"""
l = list(range(10)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
l[2:6] = [10,20]    # [0, 1, 10, 20, 6, 7, 8, 9]
del(l[3])    # [0, 1, 10, 6, 7, 8, 9]


"""列表组成的列表"""
weird_board = [['_']*3]*3   # 里面的列表是引用
weird_board[1][1] = 'X'
print(weird_board)  # [['_', 'X', '_'], ['_', 'X', '_'], ['_', 'X', '_']]

weird_board = [['_']*3 for _ in range(3)]
weird_board[1][1] = 'X'
print(weird_board)  # [['_', '_', '_'], ['_', 'X', '_'], ['_', '_', '_']]
