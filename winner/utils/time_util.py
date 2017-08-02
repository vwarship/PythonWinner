from time import time


def used_time(func):
    start = time()
    func()
    end = time()
    print('run %s() used time %f' % (func.__name__, end-start))
