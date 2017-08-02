"""了解yield的执行"""
def gen_123():
    print(">> gen123")
    yield 1
    print(">> 1")
    yield 2
    print(">> 2")
    yield 3
    print(">> 3")
    print("<< gen123")

for n in gen_123():
    print('-- %d' % n)


"""yield from"""
def f1():
    for i in range(3):
        yield i


def f2():
    yield from f1()

for i in f2():
    print(i)
