dict_data = {"age": 23, "name": "张正兵"}
# 1. items()方法，返回字典的所有键值对，以列表的形式返回可遍历的元组数组
items = dict_data.items()
for i in items:
    print(i)

# 2. key in dict 判断键是否在字典里
if "age" in dict_data:
    print("age is in dict")
else:
    print("age is not in dict")

# 3. 可以直接根据键来拿到对应的值
print(dict_data["age"])

# 4. keys()方法，返回该字典的键列表，包含该字典内的所有键
print("获取所有的key", dict_data.keys(), "类型:", type(dict_data.keys()))

# 5. get(key,default=None)返回指定的key,如果key不存在，那么返回default值。
print(dict_data.get("address", "不存在!"))

# 6. setdefault(key,default=None)设置key的默认值,如果key不存在，那么设置的值为default的值
print(dict_data.setdefault("address", "上海浦东新区"))
print(dict_data)

# 7.values()方法， values方法，返回一个迭代器，可以用list转换为值列表
print(dict_data.values())
#  --> 列表
print(list(dict_data.values()))

# 8. pop(key[,default])方法, 返回被删除的key值,如果指定的key值不存在，那么返回设定的default的值。
pop_result = dict_data.pop("add", "666")
print("pop_result", pop_result, ",dict_data", dict_data)

# 9. popitem()方法，随机返回字典的最后一个键值对。
pop_item = dict_data.popitem()
print("pop_item", pop_item, ",dict_data", dict_data)

# 10. .fromkeys()方法，根据元组序列来生成一个字典
tuple_data = ("name", "age", "address")
print("根据元组生成字典:", dict.fromkeys(tuple_data))

print("当前局部变量", locals())
print("当前全局变量", globals())

dict_data = {"1": 1, "2": 2}
print(dict_data)
print(dict_data.get("1"))

# 取出字典的第二个元素
print("2" in dict_data)

print(tuple(dict_data))

# 元组和字典可以相互转换，转换的是字典的keys
