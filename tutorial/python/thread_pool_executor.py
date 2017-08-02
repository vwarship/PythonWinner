import random
from concurrent.futures import ThreadPoolExecutor

from winner.utils.time_util import used_time


def logn(n):
    print(n, end=' ', flush=True)
    # sleep(random.random())
    return n ** 2


def no_thread():
    results = []
    for n in nums:
        r = logn(n)
        results.append(r)

    print("\nresults", results)


def multi_thread():
    executor = ThreadPoolExecutor(8)
    results = executor.map(logn, nums)
    print("\nresults", list(results))


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
used_time(no_thread)

random.seed(random_seed)
used_time(multi_thread)
