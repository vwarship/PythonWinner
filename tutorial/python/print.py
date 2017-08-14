import sys
from pprint import pprint


peoples = [("wjj", "boy", 36), ("wrj", "girlwj", 8)]


"""打印元组"""
for people in peoples:
    print("%s, %s %d" % people)


"""打印对齐表格
name       | sex   | age
wjj        | boy   |  36
wrj        | boy   |   8
"""
print("{:10} | {:5} | {:5} ".format("name", "sex", "age"))
for people in peoples:
    print("{:10} | {:5} | {:^5}".format(*people))


"""
['/Users/wjj/GitHub/PythonWinner/tutorial/python',
 '/Users/wjj/GitHub/PythonWinner',
 '/Library/Frameworks/Python.framework/Versions/3.6/lib/python36.zip',
 '/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6',
 '/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/lib-dynload',
 '/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages']
['/Users/wjj/GitHub/PythonWinner/tutorial/python', '/Users/wjj/GitHub/PythonWinner', '/Library/Frameworks/Python.framework/Versions/3.6/lib/python36.zip', '/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6', '/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/lib-dynload', '/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages']
"""
pprint(sys.path)
print(sys.path)
