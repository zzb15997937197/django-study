# 拆分参数列表，用*
a = [1, 2]


def count(*args):
    print(args)


count(*a)

# 拆分参数字典, 用**
a = {"a": 1, "b": 2, "c": 3}


def count(a, b, c):
    print(a, b, c)


count(**a)
