# 生成器
data = [1, 2, 3, 3, 4]
for i in range(10, -1, -1):
    print(i)

# 生成器,返回的结果为一个集合，集合里的元素是无序不重复的。
a = {x for x in data if x not in [4]}
print(a)
# def f1(data):
#     for i in data:
#         yield data[i]
#
#
# for c in f1(data):
#     print(c)


t1 = (1, 2, 3)
t2 = (1, 2)
print(t1 + t2)
print(t1[1])

# 判断列表是否为空(包含一个长度的空字符串)
a = [""]
