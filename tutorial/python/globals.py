def math_add(x, y):
    return x+y


def math_mul(x, y):
    return x*y


if __name__ == '__main__':
    funcs = [globals()[name] for name in globals() if name.startswith('math_')]

    y = [func(2, 3) for func in funcs]
    print(y)    # [5, 6]
