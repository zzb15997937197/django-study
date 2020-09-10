from django.test import TestCase

# Create your tests here.


EDUCATION_CHOICE = (
    (0, '初中'),
    (1, '高中'),
    (2, '大专'),
    (3, '本科'),
    (4, '硕士'),
    (5, '博士'),
)

# 判断元素是否在choice里
for i in EDUCATION_CHOICE:
    gender = i[0]
    gender_name = i[1]
    print("gender:", gender, "gender_name:", gender_name)

print(dict(EDUCATION_CHOICE))
# {0: '初中', 1: '高中', 2: '大专', 3: '本科', 4: '硕士', 5: '博士'}
dict_1 = {0: '初中', 1: '高中', 2: '大专', 3: '本科', 4: '硕士', 5: '博士'}
print(tuple(dict_1))
data1 = []
for i in dict_1:
    data1.append((i, dict_1[i]))
print(data1)
print(tuple(data1))

a = 1.2
print(int(a))
a = 123.373388
print(round(a, 3))
a = 123
print(float(a))
