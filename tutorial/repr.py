"""
5 5
"""
print(5, '5')


"""
5 '5'
"""
print(repr(5), repr('5'))
print('%r %r' % (5, '5'))



"""
实现类的repr
"""
class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return '{}({}, {})'.format(self.__class__.__name__, self.x, self.y)

pt = Point(2, 3)
print(pt)
pt2 = eval(repr(pt))
print(pt2)
