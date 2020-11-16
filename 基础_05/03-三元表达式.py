# -*- coding: utf-8 -*-
# @Time    : 2020/11/11 15:41
# @Author  : sunzhen
# @File    : 03-三元表达式.py
# @Software: PyCharm

def func():
    if 3 == 3:
        return 111
    else:
        return 222


# 比较两个数,返回比较大的数字
def func(x, y):
    if x > y:
        return x
    else:
        return y


res = func(1, 2)
print(res)


# 三元表达式 (可以用在函数内)
# 语法格式: 条件成立时的返回值 if 条件 else 条件不成立时要返回值
x = 1
y = 2
res = x if x > y else y


res = x if x > y else y















