# 是一个内置类
# reduce
from functools import reduce

scores = [100, 87, 89, 78]
print(reduce(lambda ele1, ele2: ele1 + ele2, scores))

students = [
    {'name': 'zhangsan', 'age': 18, 'height': 183, 'score': 100},
    {'name': 'lisi', 'age': 19, 'height': 185, 'score': 90},
    {'name': 'wangwu', 'age': 20, 'height': 175, 'score': 80},
    {'name': 'sunliu', 'age': 22, 'height': 176, 'score': 78}

]


def foo(x, y):
    return x + y['age']


# initial 初始值
s = reduce(foo, students, 0)
print(s)
# 使用lambda表达式
z = reduce(lambda x, y: x + y['age'], students, 0)
print(z)
abs()
