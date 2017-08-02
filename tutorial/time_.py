from time import time, sleep, strftime


"""
strftime默认使用当前时间
"""
print(strftime('%H:%M:%S')) # 15:09:56
print(strftime('%Y-%m-%d %H:%M:%S'))    # 2017-07-27 15:09:56


"""
1501139596.673856
"""
print(time())


"""睡眠1秒"""
sleep(1)
