"""
文件
"""
import os


"""按行访问文件"""
file = open('test.txt')
for line in file.readlines():
    print(line)
