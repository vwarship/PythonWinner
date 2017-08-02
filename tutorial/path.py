import os


"""
dir = /home/wjj
filename = test.txt
"""
dir, filename = os.path.split("/home/wjj/test.txt")


"""
is_exists = True
"""
is_exists = os.path.exists('../tutorial/')


"""
is_dir = True
"""
is_dir = os.path.isdir('../tutorial/')


"""
创建、删除目标
"""
path = 'test'
os.mkdir(path)
os.rmdir(path)


"""
一次创建多级目录
"""
# path = 'test/a/b/c/'
# os.makedirs(path)

