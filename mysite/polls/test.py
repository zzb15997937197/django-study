# 1.生成一个随机的10位带数字+大写字母的字符串
import random
import json

s1 = ""
for i in range(10):
    # 生成随机数
    index = random.randint(1, 3)
    if index == 1:
        a = random.randrange(97, 122)
    elif index == 2:
        a = random.randrange(65, 90)
    else:
        a = random.randint(0, 9)
    # 将字母表示的ascii码转换为对应的字母。
    print("type:", type(a))
    if a > 64:
        c = chr(a)
        print("c:", c)
    else:
        c = a
    s1 = s1 + str(c)
print(s1)

# json与对象互相转换
# 1.对象转换为json
data = [{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}]
json.dumps(data, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ': '))
print(data)

# 2.json转换为对象

data = '{"a":1,"b":2,"c":3,"d":4,"e":5}'
data_object = json.loads(data)
print("对象为:", data_object)

