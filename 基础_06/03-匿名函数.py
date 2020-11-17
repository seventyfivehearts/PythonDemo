# -*- coding: utf-8 -*-
# @Time    : 2020/11/16 16:45
# @Author  : sunzhen
# @File    : 03-匿名函数.py
# @Software: PyCharm

# 1.有名函数
# func=函数的内存地址
# def func(x, y):
#     return x, y


# 2.lambda定义匿名函数
# a = lambda x, y: x + y    # <function <lambda> at 0x00000214AEAD0280>
# print(a) # 得到函数的内存地址

# 调用方式
# res = (lambda x, y: x + y)(1, 2)
# print(res)

# 方式二: 内存地址加括号

# func = (lambda x, y: x + y)
# res = func(1, 3)
# print(res)


# 匿名用于临时调用一次的场景,更多的是配合其他函数一起使用
lambda x, y: x + y
# 被其他函数调用









