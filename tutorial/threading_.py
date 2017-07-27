from threading import Thread, Lock


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
