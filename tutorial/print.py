peoples = [("wjj", "boy", 36), ("wrj", "girlwj", 8)]

# 打印元组
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
