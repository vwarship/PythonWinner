from threading import Thread, Lock
import select

from winner.utils.time_util import used_time


"""
Python 受GIL的限制，一次只能运行一个线程，所以做CPU密集计算时，多线程的效率反而下降（线程之间切换）。
run no_thread_with_cpu() used time 1.027218
run multi_thread_with_cpu() used time 1.065897
"""
def factorize(number):
    """因式分解算法"""
    for i in range(1, number+1):
        if number % i == 0:
            yield i


numbers = [3139079, 2214759, 2516637, 2852285]


def no_thread_with_cpu():
    for number in numbers:
        list(factorize(number))


class FactorizeThread(Thread):
    def __init__(self, number):
        super().__init__()
        self.number = number

    def run(self):
        self.factors = list(factorize(self.number))


def multi_thread_with_cpu():
    threads = []
    for number in numbers:
        thread = FactorizeThread(number)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

used_time(no_thread_with_cpu)
used_time(multi_thread_with_cpu)


"""
Python 多线程处理阻塞式I/O操作
run no_thread_with_io() used time 0.514095
run multi_thread_with_io() used time 0.104648
"""
def slow_system_call():
    select.select([], [], [], 0.1)


def no_thread_with_io():
    for _ in range(5):
        slow_system_call()


def multi_thread_with_io():
    threads = []
    for _ in range(5):
        thread = Thread(target=slow_system_call)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

used_time(no_thread_with_io)
used_time(multi_thread_with_io)


"""
多线程操作同一个变量，缺少锁。
应该运行 500000，实际运行 381230
"""
count = 10**5
thread_num = 5


class Counter(object):
    def __init__(self):
        self.count = 0

    def increment(self, n):
        self.count += n


def worker(index, count, counter):
    for _ in range(count):
        # print(index, end=' ', flush=True)
        counter.increment(1)


def run_threads(func, count, counter):
    threads = []
    for i in range(thread_num):
        args = (i, count, counter)
        thread = Thread(target=func, args=args)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()


def print_result():
    print('应该运行 %d，实际运行 %d' % (count * thread_num, counter.count))


counter = Counter()
run_threads(worker, count, counter)
print_result()


"""
加锁
应该运行 500000，实际运行 500000
"""
class LockingCounter(object):
    def __init__(self):
        self.lock = Lock()
        self.count = 0

    def increment(self, n):
        with self.lock:
            self.count += n


counter = LockingCounter()
run_threads(worker, count, counter)
print_result()
