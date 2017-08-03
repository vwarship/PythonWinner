import inspect

from tutorial.python import inspect_


def math_add(x, y):
    return x+y


def math_mul(x, y):
    return x*y


if __name__ == '__main__':
    # 使用内省的方法来加载模块里的函数
    funcs = [func for name, func in inspect.getmembers(inspect_, inspect.isfunction)]

    y = [func(2, 3) for func in funcs]
    print(y)    # [5, 6]
