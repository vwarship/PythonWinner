import random
from time import sleep, time
from concurrent.futures import ThreadPoolExecutor


def logn(n):
    print(n, end=' ', flush=True)
    # sleep(random.random())
    return n ** 2


def test_thread():
    executor = ThreadPoolExecutor(8)
    results = executor.map(logn, nums)
    print("\nresults", list(results))


def test():
    results = []
    for n in nums:
        r = logn(n)
        results.append(r)

    print("\nresults", results)


def used_time(f):
    begin_time = time()
    f()
    end_time = time()
    print('function %s() used time: %f' % (f.__name__, end_time-begin_time))


"""
CPU密集计算使用多线程不能带来性能上的提高，反而是损失。

0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19
results [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361]
function test() used time: 0.000141
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19
results [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361]
function test_thread() used time: 0.002907
"""
random_seed = 1
nums = range(20)

random.seed(random_seed)
used_time(test)

random.seed(random_seed)
used_time(test_thread)
