from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

from winner.utils.time_util import used_time


def gcd(pair):
    """两数最大公约数"""
    a, b = pair
    low = min(a, b)
    for i in range(low, 0, -1):
        if a % i == 0 and b % i == 0:
            return i


numbers = [(1963309, 2265973), (2030677, 3814172), (1551645, 2229620), (2039045, 2020802)]


"""单线程运行"""
def no_thread():
    return list(map(gcd, numbers))


"""多线程运行"""
def thread_pool_executor():
    executor = ThreadPoolExecutor(len(numbers))
    return list(executor.map(gcd, numbers))


"""多进程运行"""
def process_pool_executor():
    executor = ProcessPoolExecutor()
    return list(executor.map(gcd, numbers))


"""
run no_thread() used time 0.749469
run thread_pool_executor() used time 0.772979
run process_pool_executor() used time 0.184281
"""
used_time(no_thread)
used_time(thread_pool_executor)
used_time(process_pool_executor)
